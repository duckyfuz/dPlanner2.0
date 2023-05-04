import copy
import calendar
from helpers import is_valid


class Month:
    """
    Class containing a list of Day-type objects, a dictionary to keep track of points, and a function initialize_points()
    """

    # Initialise a Month-type object by creating a list of Day-type objects and generating a dictionary with the initial values for points
    def __init__(self, YY, MM, Day, people, data):

        # Initialise .points dictionary
        self.points = self.initialize_points(people, data)

        # Create .cal list, and ammend each day based on the reward points (EVERYBODY is indicated as available for every single day)
        self.cal = []
        for week in calendar.monthcalendar(YY, MM):
            i = 0
            for date in week:
                if date == 0:
                    continue
                rwd = 1 if i in [0, 1, 2, 3] else 1.5 if i == 4 else 2
                self.cal.append(Day(date, rwd, people))
                i += 1

        # Modify each Day-type object in .cal list to account for unavailable days
        self.populate_avail(data)

        self.len = len(self.cal)

    def populate_avail(self, data):
        """
        Iterate through each person and ammend .cal list to reflect availability
        """

        for person in data:
            for unavailable_date in data[person]["unavailable"]:
                self.cal[unavailable_date - 1].remove_from_avail(person)

    def initialize_points(self, people, data):
        """
        Iterate through each person and update .points dictionary with each person's INITIAL points (.points dicionary will be updated by functions belonging to each Day-type object)
        """

        points = {}
        for person in people:
            points[person] = data[person]["points"]

        return dict(sorted(points.items(), key=lambda item: item[1]))

    def find_variance(self):
        """
        Calculate the variance of the .points dictionary (v cool)
        """

        data = []
        for person in self.points:
            data.append(self.points[person])

        return sum([(x - (sum(data) / len(data))) ** 2 for x in data]) / len(data)

    def __str__(self):

        return f"""
        Points: {self.points}
        Variance: {self.find_variance()}
      """

    def __repr__(self):

        return f"""
        Points: {self.points}
        Variance: {self.find_variance()}
      """

    def __eq__(self, other):

        if self.len != len(other.cal):
            return False

        for i in range(self.len):
            if self.cal[i] != other.cal[i]:
                return False

        return True


class Day:
    """
    Class containing the deets for each day
    """

    # Initialise a Day-type object by updating the date, duty personnel (.pax), points rewarded (.rwd), whether an extra is carried out on the day, and generateing a list of people availiable on the day (EVERYBODY is availiable, will be updated by .populate_avail() in Month-type object) - consider shifting .populate_avail() into Day-object
    def __init__(self, date, rwd, people, pax=None, extra=False):

        self.date, self.pax,  = date, pax
        self.rwd, self.extra = rwd, extra

        self.avail = copy.deepcopy(people)

    def swap(self, incoming, month):
        """
        Assign "incoming" to the date and update .points in Month-object
        """

        # Return False if "incoming" is unavailable
        if not is_valid(month.cal, self.date, incoming) or self.extra == True:
            return False

        # If somebody is already assigned on the date, deduct their points
        if self.pax != None:
            month.points[self.pax] -= self.rwd

        # Assign "incoming" to the date and add points accordingly
        self.pax = incoming
        month.points[incoming] += self.rwd

        # Sort .points in Month-object by points
        month.points = dict(
            sorted(month.points.items(), key=lambda item: item[1]))

        return True

    def convert_to_extra(self, incoming, month):
        """
        Convert the day to an extra and update .points in Month-object
        """

        self.extra = True
        month.points[incoming] -= self.rwd
        self.rwd = 0

        # Sort .points dictionary by points
        month.points = dict(
            sorted(month.points.items(), key=lambda item: item[1]))

    def remove_from_avail(self, pax):
        """
        What does the name suggest uh
        """

        self.avail.remove(pax)

    def __str__(self):

        return f"""
        Date: {self.date} | On Duty: {self.pax} | Point(s): {self.rwd} | Extra: {self.extra}
        {self.avail}
      """

    def __repr__(self):

        return f"""
        Date: {self.date} | On Duty: {self.pax} | Point(s): {self.rwd} | Extra: {self.extra}
        {self.avail}
      """

    def __eq__(self, other):

        if self.date != other.date or self.pax != other.pax or self.rwd != other.rwd or self.extra != other.extra:
            return False

        return True