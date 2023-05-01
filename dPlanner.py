import copy
from helpers import is_valid

class Day:
    def __init__(self, date, rwd, people, pax = None, extra = False):
        self.date, self.pax,  = date, pax
        self.rwd, self.extra = rwd, extra
        self.avail = copy.deepcopy(people)

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
    
    def __str__(self):
      return f"""
        Date: {self.date}
        On Duty: {self.pax}
        Point(s): {self.rwd}
        Extra: {self.extra}
        Avail: {self.avail}
      """  
            
    def swap(self, incoming, points, cal):
        if not is_valid(cal, self.date, incoming):
            return False
        
        outgoing = self.pax
        self.pax = incoming

        points[outgoing] -= self.rwd
        points[incoming] += self.rwd

        return True
    
    def schedue(self, incoming, points, cal):
        if not is_valid(cal, self.date, incoming):
            return False
        
        if self.pax != None:
            raise Exception(f"{self.pax} is schedued for this date. Use .swap() instead.")

        self.pax = incoming
        points[incoming] += self.rwd
    
        return True

    def remove_from_avail(self, pax):
        self.avail.remove(pax)