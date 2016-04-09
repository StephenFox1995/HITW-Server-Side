import json

class Member():

    _identifier = 0
    _firstname = ""
    _lastname = ""
    _handicap = 0

    def __init__(self, identifier, firstname, lastname, handicap):
        self._identifier = identifier
        self._firstname = firstname
        self._lastname = lastname


    def jsonify(self):
        data = { 'identifier' : self._identifier,
                 'firstname' : self._firstname,
                 'lastname' : self._lastname,
                 'handicap' : self._handicap }
        return json.dumps(data)


    @property
    def identifier(self):
        return self._identifier

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname

    @property
    def score(self):
        return self._score
