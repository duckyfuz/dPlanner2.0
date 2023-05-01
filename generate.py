import calendar
from dPlanner import Day
from helpers import create_cal, load_data

MM = 6
YY = 2023

FILENAME = "data/may.csv"
OUTPUT = "data/output.csv"
    
def main():
    
    # Create a list of Day-type objects
    cal = create_cal(YY, MM, Day)

    # Load data from FILENAME
    people, dict = load_data(FILENAME)

    # Populate date.unvail for each date in cal
    for person in dict:
        for unavail_date in dict[person]["unavail"]:
            cal[unavail_date - 1].add_to_unavail(person)



if __name__ == "__main__":
    main()