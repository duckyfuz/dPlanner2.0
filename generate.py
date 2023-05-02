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
    count = 0
    max_variance = 0.0
    while True:
        fill_duties(sorted, month)
        count += 1
        if count == 100:
            max_variance += 0.001
            print(f"Increasing max_variance to {max_variance:.3g}")
            count = 0
        if month.find_variance() <= max_variance:
            break
    max_variance = month.find_variance()
    SOLUTIONS[max_variance] = [copy.deepcopy(month)]

    while input("Look for an alternative? ") in ["Y", "y", ""]:
        for _ in range(100):
            fill_duties(sorted, month)
            if month.find_variance() <= max_variance:
                max_variance = month.find_variance()

                try:
                    SOLUTIONS[month.find_variance()]
                except KeyError:
                    SOLUTIONS[month.find_variance()] = []

                month_copy = copy.deepcopy(month)

                if month_copy in SOLUTIONS[month.find_variance()]:
                    print("It's a dupelicate :(")
                else:
                    print(f"New solution found! Variance: {max_variance}")
                    SOLUTIONS[month.find_variance()].append(month_copy)


    # print(month.points, month.find_variance())
    print(SOLUTIONS)


if __name__ == "__main__":
    main()