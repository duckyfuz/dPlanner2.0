import copy
import calendar
import random
from helpers import is_valid


class Month:
    def __init__(self, YY, MM, Day, people, data):
        # Create a Day class for each day in the calender
        self.cal = []
        self.points = self.initialize_points(people, data)
        for week in calendar.monthcalendar(YY, MM):
            i = 0
            for date in week:
                if date == 0:
                    continue
                rwd = 1 if i in [0,1,2,3] else 1.5 if i == 4 else 2
                self.cal.append(Day(date, rwd, people))
                i += 1
        self.len = len(self.cal)
        self.populate_avail(data)

    def populate_avail(self, data):
        for person in data:
            for unavailable_date in data[person]["unavailable"]:
                self.cal[unavailable_date - 1].remove_from_avail(person)

    def initialize_points(self, people, data):
        points = {}
        for person in people:
            points[person] = data[person]["points"]
        points = dict(sorted(points.items(), key=lambda item: item[1]))
        return points
    
    def find_variance(self):
        data = []
        for person in self.points:
            data.append(self.points[person])    
        n = len(data)
        mean = sum(data) / n
        deviations = [(x - mean) ** 2 for x in data]
        variance = sum(deviations) / n
        return variance
    
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
        days = len(self.cal)
        if days != len(other.cal):
            return False
        for i in range(days):
            if self.cal[i] != other.cal[i]:
                return False
        return True


class Day:
    def __init__(self, date, rwd, people, pax = None, extra = False):
        self.date, self.pax,  = date, pax
        self.rwd, self.extra = rwd, extra
        self.avail = copy.deepcopy(people)
            
    def swap(self, incoming, month):
        if not is_valid(month.cal, self.date, incoming):
            return False
        if self.pax != None:
            outgoing = self.pax
            month.points[outgoing] -= self.rwd
        if self.extra == True:
            return False
        self.pax = incoming
        month.points[incoming] += self.rwd
        month.points = dict(sorted(month.points.items(), key=lambda item: item[1]))
        return True
    
    def convert_to_extra(self, incoming, month):
        self.extra = True
        month.points[incoming] -= self.rwd
        self.rwd = 0
        month.points = dict(sorted(month.points.items(), key=lambda item: item[1]))

    def remove_from_avail(self, pax):
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
        if not self.date == other.date:
            return False
        if not self.pax == other.pax:
            return False
        if not self.rwd == other.rwd:
            return False
        if not self.extra == other.extra:
            return False
        return True