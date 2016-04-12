import json

class Result():

    _event_id = 0;
    _member_id = 0;
    _score = 0;

    def __init__():
        pass

    def __init__(self, event_id, member_id, score):
        self._event_id = event_id
        self._member_id = member_id
        self._score = score

    def jsonify(self):
        data = { 'event_id' : self._event_id,
                 'member_id' : self._member_id,
                 'score' : self._score }
        return json.dumps(data)

    @property
    def event_id(self, id):
        self._event_id = id

    @property
    def member_id(self, id):
        self._member_id = id

    @property
    def score(self, score):
        self._score = score


    @property
    def event_id(self):
        return self._event_id

    @property
    def member_id(self):
        return self._member_id

    @property
    def score(self):
        return self._score
