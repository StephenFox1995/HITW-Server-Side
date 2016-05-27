import json
from datetime import datetime

class Event(object):


    def __init__(self, identifier, title, location, start_tee_time, end_tee_time, date):
        self._identifier = identifier
        self._location = location
        self._start_tee_time = start_tee_time
        self._end_tee_time = end_tee_time
        self._date = date
        self._title = title



    def jsonify(self):
        data = {'identifier': self._identifier,
                'title':self._title,
                'location' : self._location,
                'startTeeTime': self._start_tee_time,
                'endTeeTime' : self._end_tee_time,
                'date': self._date }
        return json.dumps(data)


    @property
    def title(self):
        return self._title

    @property
    def location(self):
        return self._location

    @property
    def start_tee_time(self):
        return self._start_tee_time

    @property
    def end_tee_time(self):
        return self._end_tee_time

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    def identifier(self):
        return self._identifier


    # Returns date format as dd-mm-yyyy
    @staticmethod
    def date_format_ddmmyyyy(date):
        return datetime.strptime(date, '%Y-%m-%d').strftime('%d-%m-%Y')

    # Returns date format as yyyy-mm-dd
    @staticmethod
    def date_format_yyyymmdd(date):
        return datetime.strptime(date, '%d-%m-%Y').strftime('%Y-%m-%d')
