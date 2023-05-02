import copy
from dPlanner import Month, Day
from helpers import *

MM = 5
YY = 2023

FILENAME = "real_MAY.csv"
OUTPUT = "real_MAY_output.csv"
SOLUTIONS = {}
    
def main():
    
    # Load data from FILENAME
    people, data = load_data(FILENAME)
    # Create Month-object
    month = Month(YY, MM, Day, people, data)

    # Fill 
    sorted = sort_dates(month.cal)
    # Find max_variance
    max_variance = find_max_variance(sorted, month, SOLUTIONS)
    # Search for a solution
    find_solution(sorted, month, SOLUTIONS, max_variance)


    # print(month.points, month.find_variance())
    print(SOLUTIONS)


if __name__ == "__main__":
    main()