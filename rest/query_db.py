import sqlite3


INSER_INTO_EVENT = '''INSERT INTO Event(event_id, event_title, event_location, event_date, event_time) VALUES(NULL, ?, ?, ?, ?);'''

INSERT_INTO_MEMBER = '''INSERT INTO Member(member_id, member_f_name, member_l_name, member_handicap) VALUES(NULL, ?, ?, ?);'''

INSERT_INTO_RESULT = '''INSERT INTO Result(event_id, player_id, score) VALUES(NULL, ?, ?, ?);'''


def get_connection(filepath):
    connection = None
    connection = sqlite3.connect(filepath)
    return connection

def insert_into_event(connection, title, location, date, time):
    cursor = connection.cursor()
    cursor.execute(INSER_INTO_EVENT, (title, location, date, time))

def insert_into_member(connection, firstname, lastname, handicap):
    cursor = connection.cursor()
    cursor.execute(INSERT_INTO_MEMBER, (firstname, lastname, handicap))

def insert_into_result(connection, event_id, player_id, score):
    cursor = connection.cursor()
    cursor.execute(INSERT_INTO_RESULT, (event_id, player_id, score))
