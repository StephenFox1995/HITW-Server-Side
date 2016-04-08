import sqlite3
from event import Event

# Inserts
#-------------------
INSER_INTO_EVENT = '''INSERT INTO Event(event_id, event_title, event_location, event_date, event_time) VALUES(NULL, ?, ?, ?, ?);'''

INSERT_INTO_MEMBER = '''INSERT INTO Member(member_id, member_f_name, member_l_name, member_handicap) VALUES(NULL, ?, ?, ?);'''

INSERT_INTO_RESULT = '''INSERT INTO Result(event_id, member_id, score) VALUES(?, ?, ?);'''
#-------------------


# Selects
#-------------------
SELECT_ALL_EVENTS = '''SELECT * FROM Event;'''

SELECT_X_EVENTS = '''SELECT * FROM EVENT WHERE event_id = ?;'''
#-------------------


def get_connection(filepath):
    connection = None
    connection = sqlite3.connect(filepath)
    return connection

def insert_into_event(connection, title, location, date, time):
    cursor = connection.cursor()
    cursor.execute(INSER_INTO_EVENT, (title, location, date, time))
    connection.commit()

def insert_into_member(connection, firstname, lastname, handicap):
    cursor = connection.cursor()
    cursor.execute(INSERT_INTO_MEMBER, (firstname, lastname, handicap))
    connection.commit()

def insert_into_result(connection, event_id, player_id, score):
    cursor = connection.cursor()
    cursor.execute(INSERT_INTO_RESULT, (event_id, player_id, score))
    connection.commit()

def get_all_events(connection):
    cursor = connection.cursor()
    cursor.execute(SELECT_ALL_EVENTS)
    rows = cursor.fetchall()

    events = []
    if rows:
        for row in rows:
            event_id = row[0]
            event_title = row[1]
            event_location = row[2]
            event_time = row[3]
            event_date = row[4]
            event = Event(event_id, event_title, event_location, event_time, event_date)
        print event.jsonify()
    return events
