import calendar
import csv
import random

def create_cal(YY, MM, Day, people):
    # Create a Day class for each day in the calender
    cal = []
    for week in calendar.monthcalendar(YY, MM):
        i = 0
        for date in week:
            if date == 0:
                continue
            rwd = 1 if i in [0,1,2,3] else 1.5 if i == 4 else 2
            cal.append(Day(date, rwd, people))
            i += 1
    return(cal)


def load_data(filename):
    """
    Takes filename as input, returns people[] and dict{}  
    people[]: List of names (randomised)  
    dict{}: Dictionary that links names to another dictionary with keys "unavail", "points", 'extras' and 'leftovers'
    """
    
    # Open filename, skip headers line
    f = open(filename)
    reader = csv.reader(f)
    header = next(reader)

    # Initiate people[] and dict{}
    people = []
    dict = {}

    # Iterate through reader
    for row in reader:

        # Add name to people[]
        people.append(row[0])

        # Convert unavail dates to list of integers (Empty list if there are no unavail dates)
        if row[3] == 'NULL':
            unavailInt = []

        else:

            # Split row[3] into list values and convert the str values into int values
            unavail = list(row[3].split("/"))
            unavailInt = set()
            for str in unavail:
                if "-" in str:
                    start, end = str.split("-")
                    for i in range (int(start), int(end) + 1):
                        unavailInt.add(i)
                    continue
                unavailInt.add(int(str))

        clear = 0
        if int(row[2]) > 0:
            clear = int(input(f"{row[0]} has {row[2]} extra(s). How many to clear this month? "))
        
        # Add clean values into dict{}
        dict[row[0]] = {"unavail": unavailInt, 
                        "points": int(row[1]), 
                        "extras": clear, 
                        "leftovers": int(row[2]) - clear}

    # # Shuffle people[] to ensure fairness
    # random.shuffle(people)

    # Close file
    f.close()

    return people, dict
