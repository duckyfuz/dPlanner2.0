import calendar

def create_cal(YY, MM, Day):
    # Create a Day class for each day in the calender
    print(calendar.monthcalendar(YY, MM))
    cal = []
    for week in calendar.monthcalendar(YY, MM):
        i = 0
        for date in week:
            if date == 0:
                continue
            rwd = 1 if i in [1,2,3,4] else 1.5 if i == 5 else 2
            cal.append(Day(date, rwd))
            i += 1
    return(cal)

