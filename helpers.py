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


def sort_dates(cal):
    two_pointers, one_half_pointers, one_pointers = [], [], []
    for day in cal:
        if day.rwd == 1:
            one_pointers.append(day.date)
        elif day.rwd == 2:
            two_pointers.append(day.date)
        else:
            one_half_pointers.append(day.date)
    return [one_pointers, two_pointers, one_half_pointers]


def fill_duties(sorted, month):
    one_pointers, two_pointers, one_half_pointers = sorted
    random.shuffle(one_pointers)
    random.shuffle(two_pointers)
    random.shuffle(one_half_pointers)
    for date in two_pointers:
        for incoming in list(month.points.keys()):
            if month.cal[date - 1].swap(incoming, month) == False:
                continue
            break
    for date in one_half_pointers:
        for incoming in list(month.points.keys()):
            if month.cal[date - 1].swap(incoming, month) == False:
                continue
            break
    for date in one_pointers:
        for incoming in list(month.points.keys()):
            if month.cal[date - 1].swap(incoming, month) == False:
                continue
            break

    # Calibrate
    for _ in range(100):
        calibrate(month)


def calibrate(month):
    for outgoing in reversed(list(month.points.keys())):
        outgoing_duties = []
        for day in month.cal:
            if day.pax != outgoing:
                continue
            if day.extra == True:
                continue
            outgoing_duties.append(day.date)
        random.shuffle(outgoing_duties)
        swapped = False
        for outgoing_duty in outgoing_duties:
            for incoming in list(month.points.keys()):
                if month.cal[outgoing_duty - 1].swap(incoming, month) == False:
                    continue
                else: 
                    swapped = True
                    break
            if swapped == True:
                break
        if swapped == True:
                break