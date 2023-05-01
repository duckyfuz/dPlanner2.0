import calendar
from dPlanner import Day
from helpers import create_cal, load_data

MM = 5
YY = 2023

FILENAME = "real_MAY.csv"
OUTPUT = "real_MAY_output.csv"
    
def main():
    
    # Load data from FILENAME
    people, dict = load_data(FILENAME)

    # Create a list of Day-type objects
    cal = create_cal(YY, MM, Day, people)

    # Populate date.avail for each date in cal
    for person in dict:
        for unavail_date in dict[person]["unavail"]:
            cal[unavail_date - 1].remove_from_avail(person)

    # for i in cal:
    #     print(i)



if __name__ == "__main__":
    main()