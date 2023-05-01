import calendar
import csv
import random


def is_valid(cal, date, incoming):
    """
    Check if incoming is valid, DOES NOT CHECK FOR EXTRAS
    """
    # Check that incoming is not the same as outgoing
    if incoming == cal[date - 1].pax:
        return False
    
    # Check that incoming is avail on the date
    if incoming not in cal[date - 1].avail:
        return False
    
    # Check the day before
    if date != 1:
        if incoming == cal[date - 2].pax:
            return False
    
    # Check the day after
    if date != len(cal):
        if incoming == cal[date].pax:
            return False

    return True


# def create_cal(YY, MM, Day, people):
#     # Create a Day class for each day in the calender
#     cal = []
#     for week in calendar.monthcalendar(YY, MM):
#         i = 0
#         for date in week:
#             if date == 0:
#                 continue
#             rwd = 1 if i in [0,1,2,3] else 1.5 if i == 4 else 2
#             cal.append(Day(date, rwd, people))
#             i += 1
#     return(cal)


def load_data(filename):
    """
    Takes filename as input and returns a list of people and a dictionary with keys "unavailable", "points", 'to_clear' and 'leftover_duties'
    """
    
    # Open filename, skip headers line
    f = open(filename)
    reader = csv.reader(f)
    header = next(reader)

    data = {}

    # Iterate for each person in f
    for row in reader:
        
        # Clean up unavail dates
        if row[3] != 'NULL':

            unavailable = list(row[3].split("/"))
            unavailable_dates = set()

            for str in unavailable:
                if not "-" in str:
                    unavailable_dates.add(int(str))
                    continue
                start, end = str.split("-")
                for i in range (int(start), int(end) + 1):
                    unavailable_dates.add(i)
                
        else:
            unavailable_dates = []
            
        # Ask user for input, only accept >= 0
        to_clear = 0
        if int(row[2]) > 0:
            while True: 
                try: 
                    to_clear = int(input(f"{row[0]} has {row[2]} extra(s). How many to to_clear this month? "))
                except:
                    continue
                if to_clear < 0:
                    continue
                break
        
        # Add clean values into data{}
        data[row[0]] = {"unavailable": unavailable_dates, 
                        "points": int(row[1]), 
                        "to_clear": to_clear, 
                        "leftover_duties": int(row[2]) - to_clear}

    # Close file
    f.close()

    return list(data.keys()), data


def create_points(people, data):
    points = {}
    for person in people:
        points[person] = data[person]["points"]
    return points

     
# def fill_cal(cal, ascending_points, points):
#     for date in cal:
#         for pax in ascending_points:
#             incoming = pax[0]
#             if date.schedue(incoming, points, cal):
#                 print(incoming, date.rwd, points[incoming])
#                 break
#         ascending_points = sorted(points.items(), key=lambda x:x[1])


def find_variance(points):
    data = []
    for person in points:
       data.append(points[person])

    n = len(data)
    mean = sum(data) / n

    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    
    return variance