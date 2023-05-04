import copy
import csv
import random


def is_valid(cal, date, incoming):
    """
    Check if incoming is valid, DOES NOT CHECK FOR EXTRAS
    """

    # Check that incoming is not the same as outgoing and that incoming is avail on the date
    if incoming == cal[date - 1].pax or incoming not in cal[date - 1].avail:
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
    Return a dictionary containig data: "unavailable", "points", 'to_clear' and 'leftover_duties'
    """
    
    # Open filename, skip headers line
    f = open(filename)
    reader = csv.reader(f)
    header = next(reader)

    data = {}

    # Iterate for each person
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
            
        # Ask user to suggest the amount of extras to clear
        to_clear = 0

        if int(row[2]) > 0:
            while True: 
                try: 
                    to_clear = int(input(f"{row[0]} has {row[2]} extra(s). How many to to_clear this month? "))
                except:
                    continue
                if to_clear < 0 or to_clear > int(row[2]):
                    continue
                break
        
        # Add clean values into dictionary
        data[row[0]] = {"unavailable": unavailable_dates, 
                        "points": int(row[1]), 
                        "to_clear": to_clear, 
                        "leftover_duties": int(row[2]) - to_clear}

    # Close file
    f.close()

    return list(data.keys()), data


def sort_dates(cal): # ADD PUBLIC HOL INPUT PORTION
    """
    Sort all dates by their points
    """

    two_pointers, one_half_pointers, one_pointers = [], [], []
    for day in cal:
        if day.rwd == 1:
            one_pointers.append(day.date)
        elif day.rwd == 2:
            two_pointers.append(day.date)
        else:
            one_half_pointers.append(day.date)
    return [one_pointers, two_pointers, one_half_pointers]


def fill_duties(sorted, month, data):
    """
    Fill up the month with extra duties, then normal duties, then calibrate to decrease variance
    """

    # Shuffle dates
    one_pointers, two_pointers, one_half_pointers = sorted
    random.shuffle(one_pointers)
    random.shuffle(two_pointers)
    random.shuffle(one_half_pointers)

    # Assign extras
    extras = {}

    for pax in data:
        if data[pax]["to_clear"] == 0 and data[pax]["leftover_duties"] == 0:
            continue
        extras[pax] = [data[pax]["to_clear"], data[pax]["leftover_duties"]]

    for loser in extras:
        for i in range(extras[loser][0]):
            for date in two_pointers:
                if month.cal[date - 1].swap(loser, month) == True:
                    month.cal[date - 1].convert_to_extra(loser, month)
                    break

    # Assign normal duties
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

    # Calibrate 50 times
    for _ in range(50):
        calibrate(month)


def calibrate(month):
    """
    Take a duty from the pax with the most points and give it the the pax with the least points
    """

    # Iterate through every pax, starting from the one with the least points
    for outgoing in reversed(list(month.points.keys())):

        # Create a list of the duties schedued for "outgoing"
        outgoing_duties = []

        for day in month.cal:

            # Skip duties assigned to others and extra duties
            if day.pax != outgoing or day.extra == True:
                continue
            outgoing_duties.append(day.date)

        # Shuffle "outgoing" de duties
        random.shuffle(outgoing_duties)

        # Find somebody to take over "outgoing"
        swapped = False

        for outgoing_duty in outgoing_duties:

            for incoming in list(month.points.keys()):

                if month.cal[outgoing_duty - 1].swap(incoming, month) == True:
                    swapped = True
                    break

                continue 
                    
            if swapped == True:
                break

        if swapped == True:
            break


def find_max_variance(sorted, month, SOLUTIONS, data):
    """
    Generate one solution with the lowest variance possible (might not be the lowest)
    """

    # Start from 0
    max_variance = 0
    count = 0

    # Repeat while increasing max_variance every 10 tries
    while True:

        clean_month = copy.deepcopy(month)
        fill_duties(sorted, clean_month, data)

        count += 1

        if count >= 10:
            max_variance += 0.01
            count = 0

        # Break the loop after finding a solution
        if clean_month.find_variance() <= max_variance:
            break

    # Calculate the varience of the solution
    max_variance = clean_month.find_variance()

    # Add a copy of the solution into the SOLUTIONS list
    SOLUTIONS[max_variance] = [copy.deepcopy(clean_month)]

    # Print a message (kinda useless tbh)
    print(f"max_variance set at {max_variance:.3g}")

    return(max_variance)


def find_solution(sorted, month, SOLUTIONS, max_variance, data):
    """
    Search for another unique solution with variance equal to or lower than the previous
    """

    # Repeat until user is satisfied
    while True:

        # Press Enter to find another solution, press Ctrl-D to end loop
        try: 
            input("Press Enter for another solution, Ctrl-D to move on. ")
        except EOFError:
            break

        # Repeat until another solution is found
        while True:

            clean_month = copy.deepcopy(month)
            fill_duties(sorted, clean_month, data)

            # When a probable solution is found
            if clean_month.find_variance() <= max_variance:

                prev_var = max_variance
                max_variance = clean_month.find_variance()

                # Create new dictionary key if a lower variance is found
                try:
                    SOLUTIONS[clean_month.find_variance()]
                except KeyError:
                    SOLUTIONS[clean_month.find_variance()] = []

                # Add a copy of the solution into SOLUTIONS list ONLY IF it is unique
                if clean_month in SOLUTIONS[clean_month.find_variance()]:
                    print("Duplicate found")
                else:
                    print(f"New solution found!")
                    if max_variance < prev_var:
                        print(f"max_variance decreased to {max_variance:.3g}")
                    SOLUTIONS[clean_month.find_variance()].append(copy.deepcopy(clean_month))
                    break
    

def write_to_csv(mm, yy, OUTPUT, SOLUTIONS, max_variance, data):
    """
    Create n amount of whatsapp-ready message(s)
    """

    # Ask user for number n
    while True:
        try: 
            n = int(input("How many would you like to view? "))
            break
        except:
            continue
    
    n = 1 # REMOVE THIS AFTER DONE
    
    # Repeat n times
    for _ in range(n):

        month = SOLUTIONS[max_variance][_]
        
        # Open a new file to write in
        with open(OUTPUT, 'w', newline='') as f:

            writer = csv.writer(f)

            # Write introductory lines
            writer.writerow(["Hello all", ""])
            writer.writerow(["These are the duties for the " + str(mm) + "th month of " + str(yy) + ":"])
            writer.writerow([])

            # Iterate through each day and add a new line for each day
            for day in month.cal:
                writer.writerow([f"{day.date}. {day.pax}"])
                # writer.writerow([str(day.date) + ". " + day.pax])
            writer.writerow([])

            # Add introcutory line
            writer.writerow(["As of now", ""])

            # This portion was copied from fill_data(), might want to clean up later
            extras = {} 
            for pax in data:
                if data[pax]["to_clear"] == 0 and data[pax]["leftover_duties"] == 0:
                    continue
                extras[pax] = data[pax]["to_clear"] + data[pax]["leftover_duties"]

            for day in month.cal:
                if day.extra == False:
                    continue
                extras[day.pax] -= 1

            # Iterate through each person and add a new line for each person with outstanding extras
            for pax in extras:
                if extras[pax] == 0:
                    continue
                elif extras[pax] == 1:
                    writer.writerow([f"{pax} still has {extras[pax]} outstanding extra to clear."])
                else:      
                    writer.writerow([f"{pax} still has {extras[pax]} outstanding extras to clear."])

            writer.writerow([])
            writer.writerow(["At the end of the month", ""])
            for pax in month.points:
                writer.writerow([pax + ": " + str(month.points[pax]) + "pts"])