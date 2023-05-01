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

    # dates = get_dates(month.cal)

    # random.shuffle(dates)
    # for date in dates:
    #     for incoming in list(month.points.keys()):
    #         # print(date, incoming)
    #         if month.cal[date - 1].swap(incoming, month) == False:
    #             continue
    #         # print(month.points)
    #         break

    # print(month.points)

    # Fill up all 2 pointers
    one_pointers, two_pointers, one_half_pointers = sort_dates(month.cal)
    count = 0
    max_variance = 0
    while True:
        fill_by_points(one_pointers, two_pointers,one_half_pointers, month)
        count += 1
        if count == 100:
            max_variance += 0.0001
            print(f"Increasing max_variance to {max_variance:.4g}")
            count = 0
        if month.find_variance() <= max_variance:
            break

    print(month.points, month.find_variance())


if __name__ == "__main__":
    main()