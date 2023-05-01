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

    # Create Month-object
    month = Month(YY, MM, Day, people, data)

    incoming = "2LT KENNETH"
    print(month.points)
    print(month.cal[0].schedue(incoming, month.points, month.cal))
    print(month.points)
    
    print(month.find_variance())

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