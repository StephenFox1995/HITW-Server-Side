from member import Member

class PlayerOfTheYear(object):

    def __init__(self, member, year, score):
        self._member = member
        self._year = year
        self._score = score

    @property
    def member(self):
        return self._member

    @property
    def year(self):
        return self._year

    @property
    def score(self):
        return self._score
