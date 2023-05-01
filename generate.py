import calendar
from dPlanner import Day
from helpers import create_cal, load_data, create_points_and_sort, fill_cal, find_variance

MM = 5
YY = 2023

FILENAME = "real_MAY.csv"
OUTPUT = "real_MAY_output.csv"
    
def main():
    
    # Load data from FILENAME
    people, data = load_data(FILENAME)

    # Create a list of Day-type objects
    cal = create_cal(YY, MM, Day, people)

    # Populate date.avail for each date in cal
    for person in data:
        for unavailable_date in data[person]["unavailable"]:
            cal[unavailable_date - 1].remove_from_avail(person)

    # Create points dictionary
    points, ascending_points = create_points_and_sort(people, data)

    # Fill cal and update 
    fill_cal(cal, ascending_points, points)
    # Update ascending_points
    ascending_points = sorted(points.items(), key=lambda x:x[1])

    # Calc. variance (aim for a variance of 0)
    variance = find_variance(points)
    
    for person in reversed(ascending_points):
        print(person)

    # for day in cal:
    #     print(day.pax)

    # print(points)


if __name__ == "__main__":
    main()