import json

class Event():

    _title = ""
    _location = ""
    _time = ""
    _date = ""
    _identifier = None

    def __init__(self, identifier, title, location, time, date):
        self._identifier = identifier
        self._location = location
        self._time = time
        self._date = date
        self._title = title


    def jsonify(self):
        data = {'identifier': self._identifier, 'title':self._title, 'location' : self._location, 'time': self._time, 'date': self._date }
        return json.dumps(data)


    @property
    def title(self):
        return self._title

    @property
    def location(self):
        return self._location


    @property
    def time(self):
        return self._time


    @property
    def date(self):
        return self._date

    def identifier(self):
        return self._identifier
