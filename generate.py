import copy
from dPlanner import Month, Day
from helpers import *
# import tkinter

MM = 5
YY = 2023

FILENAME = "real_MAY.csv"
OUTPUT = "real_MAY_output.csv"
SOLUTIONS = {}
    
def main():
    
    # Load data from FILENAME, then create Month-type object
    people, data = load_data(FILENAME)
    month = Month(YY, MM, Day, people, data)

    # Fill 
    sorted = sort_dates(month.cal)
    # Search for a solution - lowest variance
    max_variance = find_max_variance(sorted, month, SOLUTIONS, data)

    # Search for a solution
    find_solution(sorted, month, SOLUTIONS, max_variance, data)

    # print(month.points, month.find_variance())
    print(SOLUTIONS[max_variance][2], SOLUTIONS[max_variance][2].cal)


if __name__ == "__main__":
    main()