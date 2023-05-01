import calendar
from dPlanner import Day
from helpers import create_cal

MM = 6
YY = 2023
    
def main():
    
    # Create a list of Day-type objects
    cal = create_cal(YY, MM, Day)
    cal[0].add_to_unavail('Tom')


if __name__ == "__main__":
    main()