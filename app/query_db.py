import sqlite3
import zlib
from event import Event
from member import Member
from result import Result
from poy import PlayerOfTheYear


# INSERTS
#-------------------
INSER_INTO_EVENT = '''INSERT INTO Event(event_id, event_title, event_location, event_date, event_start_tee_time, event_end_tee_time) VALUES(NULL, ?, ?, ?, ?, ?)'''

INSERT_INTO_MEMBER = '''INSERT INTO Member(member_id, member_f_name, member_l_name, member_handicap) VALUES(NULL, ?, ?, ?);'''

INSERT_INTO_RESULT = '''INSERT INTO Result(event_id, member_id, score) VALUES(?, ?, ?);'''

INSERT_INTO_EVENT_IMAGE = '''INSERT INTO EVENTIMAGE(event_id, image_data) VALUES(?, ?);'''

INSERT_INTO_POY = '''INSERT INTO PLAYEROFTHEYEAR(member_id, year, score) VALUES(?, ?, ?);'''
#-------------------


# SELECTS
#-------------------
SELECT_ALL_EVENTS = '''SELECT * FROM Event'''

SELECT_EVENT_X = '''SELECT * FROM EVENT WHERE event_id = ?'''

SELECT_ALL_EVENT_IMAGES_FOR_EVENT = '''SELECT * FROM EVENTIMAGE WHERE event_id = ?'''

SELECT_UPCOMING_EVENT = '''SELECT * FROM EVENT WHERE event_date >= date('now') ORDER BY event_date ASC;'''

SELECT_ALL_MEMBERS = '''SELECT * FROM Member'''

SELECT_MEMBER_X = '''SELECT * FROM MEMBER WHERE member_id = ?'''


SELECT_ALL_RESULTS = '''SELECT * FROM Result'''

SELECT_RESULT_X_FROM_MEMBER_ID = '''SELECT * FROM Result WHERE member_id = ?'''
SELECT_RESULT_X_FOR_EVENT = '''SELECT * FROM Result WHERE event_id = ?'''

SELECT_ALL_POYS = '''SELECT * FROM PlayerOfTheYear'''

#-------------------


# UPDATES
# ------------------
UPDATE_EVENT_BY_EVENT_ID= 'UPDATE Event SET event_title=?, event_location=?, event_date=?, event_start_tee_time=?, event_end_tee_time=? WHERE event_id=?;'

UPDATE_MEMBER_BY_MEM_ID = 'UPDATE Member SET member_f_name=?, member_l_name=?, member_handicap=? WHERE member_id=?';

UPDATE_RESULT_BY_EVENT_ID_AND_MEM_ID = 'UPDATE Result SET member_id=?, event_id=?, score=? WHERE member_id=? AND event_id=?';

UPDATE_POY = 'UPDATE PlayerOfTheYear SET member_id=?, year=?, score=? WHERE member_id=? AND year=?'
# -------------------

# DELETES
# ----------------
DELETE_RESULT_BY_EVENT_ID_AND_MEM_ID = 'DELETE FROM Result WHERE member_id =? AND event_id = ?'

DELETE_MEMBER = 'DELETE FROM Member WHERE member_id = ?';

DELETE_EVENT = 'DELETE FROM Event WHERE event_id = ?'

DELETE_POY = 'DELETE FROM PlayerOfTheYear WHERE member_id = ? AND year = ?;'

#----------------




def get_connection(filepath):
    connection = None
    connection = sqlite3.connect(filepath)
    return connection

def insert_into_event(connection, title, location, date, start_tee, end_tee):
    cursor = connection.cursor()
    cursor.execute(INSER_INTO_EVENT, (title, location, date, start_tee, end_tee))
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

def insert_into_event_image(connection, event_id, image_data):
    cursor = connection.cursor()
    cursor.execute(INSERT_INTO_EVENT_IMAGE, (event_id, image_data))
    connection.commit()
    cursor.close()


def insert_into_poy(connection, member_id, year, score):
    cursor = connection.cursor()
    cursor.execute(INSERT_INTO_POY, (member_id, year, score))
    connection.commit()
    cursor.close()


def get_all_events(connection):
    cursor = connection.cursor()
    cursor.execute(SELECT_ALL_EVENTS)
    rows = cursor.fetchall()

    events = []
    if rows:
        for row in rows:
            event = create_event_from_sql_result(row)
            events.append(event)
    cursor.close()
    return events


def get_event(connection, identifier):
    cursor = connection.cursor()
    cursor.execute(SELECT_EVENT_X, (identifier,))
    row = cursor.fetchone()

    event = None
    if row:
        event = create_event_from_sql_result(row)
    cursor.close()
    return event


def get_upcoming_event(connection):
    cursor = connection.cursor()
    cursor.execute(SELECT_UPCOMING_EVENT)
    rows = cursor.fetchall()

    event = None
    if rows:
        # Get the first element, this will be the upcoming event.
        event = create_event_from_sql_result(rows[0])
    cursor.close()
    return event


def get_all_event_images(connection, identifier):
    cursor = connection.cursor()
    cursor.execute(SELECT_ALL_EVENT_IMAGES_FOR_EVENT, (identifier));
    rows = cursor.fetchall()

    decompressed_blobs = []
    image = ''
    for image_data in rows:
        image = image_data[1]
        decompressed_blobs.append(image);
    cursor.close()
    return decompressed_blobs



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

# Returns all player of the years.
def get_all_poy(connection):
    cursor = connection.cursor()
    cursor.execute(SELECT_ALL_POYS)
    rows = cursor.fetchall()

    results = {}
    if rows:
        for row in rows:
            member_id = row[0] # member_id is stored at first index in result.
            member = get_member(connection, member_id) # now go get that member from the database.
            score = row[2]
            year = row[1] # extract the year.
            poy = PlayerOfTheYear(member, year, score)

            # check to see if a key already exists
            # for a specific year in
            if year in results:
                # Get the array of players for that year.
                results[year].append(poy)
            else: # If no key exists for that year add it.
                poys = [poy]
                results[year] = poys # Add an array object
        cursor.close()

        return results



def update_event(connection, identifier, event):
    update_query = UPDATE_EVENT_BY_EVENT_ID
    # Just use update with all the fields even
    # if only one was updated.
    new_event_title = event.title
    new_event_location = event.location
    new_event_date = event.date
    new_event_start_tee = event.start_tee_time
    new_event_end_tee = event.end_tee_time

    cursor = connection.cursor()
    cursor.execute(update_query, (new_event_title, new_event_location, new_event_date, new_event_start_tee, new_event_end_tee, identifier))
    connection.commit()
    cursor.close()


def update_member(connection, identifier, member):
    update_query = UPDATE_MEMBER_BY_MEM_ID

    new_member_f_name = member.firstname
    new_member_l_name = member.lastname
    new_member_handicap = member.handicap

    cursor = connection.cursor()
    cursor.execute(update_query, (new_member_f_name, new_member_l_name, new_member_handicap, identifier))
    connection.commit()
    cursor.close

def update_result(connection, result, member_id_key, event_id_key):
    update_query = UPDATE_RESULT_BY_EVENT_ID_AND_MEM_ID

    # This properties are the
    # updated properties.
    member_id = result.member_id
    event_id = result.event_id
    score = result.score

    cursor = connection.cursor()
    cursor.execute(update_query, (member_id, event_id, score, member_id_key, event_id_key))
    connection.commit()
    cursor.close()

def update_poy(connection, old_member_id, new_member_id, year, score):
    update_query = UPDATE_POY
    cursor = connection.cursor()
    cursor.execute(update_query, (new_member_id, year, score, old_member_id, year))
    connection.commit()
    cursor.close()


def delete_poy(connection, member_id, year):
    delete_query = DELETE_POY
    cursor = connection.cursor()
    cursor.execute(delete_query, (member_id, year))
    connection.commit()
    cursor.close()



def delete_result(connection, member_id, event_id):
    delete_query = DELETE_RESULT_BY_EVENT_ID_AND_MEM_ID
    cursor = connection.cursor()
    cursor.execute(delete_query, (member_id, event_id,))
    connection.commit()
    cursor.close()

def delete_member(connection, member_id):
    delete_query = DELETE_MEMBER
    cursor = connection.cursor()
    cursor.execute(delete_query, (member_id,))
    connection.commit()
    cursor.close()

def delete_event(connection, event_id):
    delete_query = DELETE_EVENT
    cursor = connection.cursor()
    cursor.execute(delete_query, (event_id,))
    connection.commit()
    cursor.close()


def create_event_from_sql_result(result):
    if result:
        event_id =          result[0]
        event_title =       result[1]
        event_location =    result[2]
        event_date =        result[3]
        event_start_tee =   result[4]
        event_end_tee =     result[5]
        event = Event(event_id, event_title, event_location, event_start_tee, event_end_tee, event_date)
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
