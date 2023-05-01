import copy


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
            
    def swap(self, incoming):
        self.pax == incoming
        
    def withdraw(self, amount):
        self.balance -= amount

    def remove_from_avail(self, pax):
        self.avail.remove(pax)