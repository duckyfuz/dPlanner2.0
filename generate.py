from dPlanner import Month, Day
from helpers import *
# import tkinter

MM, YY = 5, 2023

FILENAME = "real_MAY.csv"
OUTPUT = "output/"
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
        
    write_to_csv(MM, YY, OUTPUT, SOLUTIONS, max_variance, data)

if __name__ == "__main__":
    main()