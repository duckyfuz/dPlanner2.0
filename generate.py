import copy
from dPlanner import Month, Day
from helpers import *

MM = 5
YY = 2023

FILENAME = "real_MAY.csv"
OUTPUT = "real_MAY_output.csv"
SOLUTIONS = []
    
def main():
    
    # Load data from FILENAME
    people, data = load_data(FILENAME)

    # Create Month-object
    month = Month(YY, MM, Day, people, data)

    # Fill up all 2 pointers
    one_pointers, two_pointers, one_half_pointers = sort_dates(month.cal)

    for date in two_pointers:
        for incoming in list(month.points.keys()):
            print(date, incoming)
            if month.cal[date - 1].swap(incoming, month) == False:
                continue
            print(month.points)
            break

    for date in one_half_pointers:
        for incoming in list(month.points.keys()):
            print(date, incoming)
            if month.cal[date - 1].swap(incoming, month) == False:
                continue
            print(month.points)
            break

    for date in one_pointers:
        for incoming in list(month.points.keys()):
            print(date, incoming)
            if month.cal[date - 1].swap(incoming, month) == False:
                continue
            print(month.points)
            break

    print(month.points)

    # print(month.cal)


# def solve(month, date = 1):

#     if date > month.len:
#         SOLUTIONS.append(month)
#         # print("Current Solutions Repo:")

#         # print(month.cal)
#         # print(SOLUTIONS)
#         print(SOLUTIONS)
#         return
    
#     for incoming in month.cal[date - 1].avail:
#         month = copy.deepcopy(month)
#         print(month)
#         if month.cal[date - 1].swap(incoming, month.points, month.cal) == False:
#             continue
#         solve(month, date + 1)


if __name__ == "__main__":
    main()