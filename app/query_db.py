import sqlite3
from event import Event
from member import Member
from result import Result

# Inserts
#-------------------
INSER_INTO_EVENT = '''INSERT INTO Event(event_id, event_title, event_location, event_date, event_time) VALUES(NULL, ?, ?, ?, ?);'''

INSERT_INTO_MEMBER = '''INSERT INTO Member(member_id, member_f_name, member_l_name, member_handicap) VALUES(NULL, ?, ?, ?);'''

INSERT_INTO_RESULT = '''INSERT INTO Result(event_id, member_id, score) VALUES(?, ?, ?);'''
#-------------------


# Selects
#-------------------
SELECT_ALL_EVENTS = '''SELECT * FROM Event;'''

SELECT_EVENT_X = '''SELECT * FROM EVENT WHERE event_id = ?;'''


SELECT_ALL_MEMBERS = '''SELECT * FROM Member;'''

SELECT_MEMBER_X = '''SELECT * FROM MEMBER WHERE member_id = ?;'''


SELECT_ALL_RESULTS = '''SELECT * FROM Result'''

SELECT_RESULT_X_FROM_MEMBER_ID = '''SELECT * FROM Result WHERE member_id = ?;'''
SELECT_RESULT_X_FOR_EVENT = '''SELECT * FROM Result WHERE event_id = ?;'''
#-------------------


def get_connection(filepath):
    connection = None
    connection = sqlite3.connect(filepath)
    return connection

def insert_into_event(connection, title, location, date, time):
    cursor = connection.cursor()
    cursor.execute(INSER_INTO_EVENT, (title, location, date, time))
    connection.commit()
    cursor.close()

def insert_into_member(connection, firstname, lastname, handicap):
    cursor = connection.cursor()
    cursor.execute(INSERT_INTO_MEMBER, (firstname, lastname, handicap))
    connection.commit()
    cursor.close()

def insert_into_result(connection, event_id, player_id, score):
    cursor = connection.cursor()
    cursor.execute(INSERT_INTO_RESULT, (event_id, player_id, score))
    connection.commit()
    cursor.close()

def get_all_events(connection):
    cursor = connection.cursor()
    cursor.execute(SELECT_ALL_EVENTS)
    rows = cursor.fetchall()

    events = []
    if rows:
        for row in rows:
            event = create_event_from_result(row)
            events.append(event)
    cursor.close()
    return events


def get_event(connection, identifier):
    cursor = connection.cursor()
    cursor.execute(SELECT_EVENT_X, (identifier,))
    row = cursor.fetchone()

    event = None
    if row:
        event = create_event_from_result(row)
    cursor.close()
    return event


def get_all_members(connection):
    cursor = connection.cursor()
    cursor.execute(SELECT_ALL_MEMBERS)
    rows = cursor.fetchall()

    members = []
    if rows:
        for row in rows:
            member = create_member_from_result(row)
            members.append(member)
    cursor.close()
    return members

def get_member(connection, identifier):
    cursor = connection.cursor()
    cursor.execute(SELECT_MEMBER_X, (identifier,))
    row = cursor.fetchone()

    member = None
    if row:
        member = create_member_from_result(row)
    cursor.close()
    return member

def get_all_results(connection):
    cursor = connection.cursor()
    cursor.execute(SELECT_ALL_RESULTS)
    rows = cursor.fetchall()

    results = []
    if rows:
        for row in rows:
            result = create_resultObject_from_result(row)
            results.append(result)
    cursor.close()
    return results

def get_all_results_for_event(connection, identifier):
    cursor = connection.cursor()
    cursor.execute(SELECT_RESULT_X_FOR_EVENT, (identifier,))
    rows = cursor.fetchall()

    results = []
    if rows:
        for row in rows:
            result = create_resultObject_from_result(row)
            results.append(result)
    cursor.close()
    return results

def get_all_results_for_member(connection, identifier):
    cursor = connection.cursor()
    cursor.execute(SELECT_RESULT_X_FROM_MEMBER_ID, (identifier,))
    rows = cursor.fetchall()

    results = []
    if rows:
        for row in rows:
            result = create_resultObject_from_result(row)
            results.append(result)
    cursor.close()
    return results



def update_event(connection, identifier, event):
    update_query = gen_unbinded_event_update_query()
    # Just use update with all the fields even
    # if only one was updated.
    new_event_title = event.title
    new_event_location = event.location
    new_event_date = event.date
    new_event_time = event.time

    cursor = connection.cursor()
    cursor.execute(update_query, (new_event_title, new_event_location, new_event_date, new_event_time, identifier))
    connection.commit()
    cursor.close()



def gen_unbinded_event_update_query():
    return 'UPDATE Event SET event_title=?, event_location=?, event_date=?, event_time=? WHERE event_id=?;'


def create_event_from_result(result):
    if result:
        event_id =       result[0]
        event_title =    result[1]
        event_location = result[2]
        event_time =     result[3]
        event_date =     result[4]
        event = Event(event_id, event_title, event_location, event_time, event_date)
        return event


def create_member_from_result(result):
    if result:
        member_id =       result[0]
        member_f_name =   result[1]
        member_l_name =   result[2]
        member_handicap = result[3]
        member = Member(member_id, member_f_name, member_l_name, member_handicap)
        return member

def create_resultObject_from_result(result):
    if result:
        result_o_event_id =  result[0]
        result_o_member_id = result[1]
        result_score =       result[2]
        result_o = Result(result_o_event_id, result_o_member_id, result_score)
        return result_o
