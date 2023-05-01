import copy
from dPlanner import Month, Day
from helpers import *

MM = 5
YY = 2023

FILENAME = "real_MAY.csv"
OUTPUT = "real_MAY_output.csv"
    
def main():
    
    # Load data from FILENAME
    people, data = load_data(FILENAME)

    # Create a list of Day-type objects and remove unavail pax
    month = Month(YY, MM, Day, people, data)

    # Create points dictionary
    points = create_points(people, data)

    print(month.cal)

    # Calc. variance (aim for a variance of 0)
    variance = find_variance(points)

    # Find all possible solutions
    # solutions = solve(month, 1)

    # for day in cal:
    #     print(day.pax)
    # print(points)


# def solve(month, date, initial = True):
#     if initial == True:
#         solutions = []
#     initial = False

#     if date > len(cal):
#         print("last")
#         return cal

#     for person in cal[date - 1].avail:
#         cal[date - 1] 
#         cal = copy.deepcopy(cal)
#         solve(cal, date + 1)

#     print(cal[date - 1])
#     print(cal[date - 1].avail)


#     return solutions


if __name__ == "__main__":
    main()