import sqlite3
import sys
# Creates all the tabe within the database.

CREATE_EVENT_TABLE_STMT = '''CREATE TABLE 'Event' (
	event_id INTEGER PRIMARY KEY NOT NULL,
	event_title VARCHAR,
	event_location VARCHAR NOT NULL,
	event_date DATE NOT NULL,
	event_time TIME NOT NULL
);'''

CREATE_MEMBER_TABLE_STMT = '''CREATE TABLE 'Member' (
	member_id INTEGER PRIMARY KEY  NOT NULL,
	member_f_name VARCHAR NOT NULL,
	member_l_name VARCHAR NOT NULL,
	member_handicap VARCHAR NOT NULL
);'''

CREATE_RESULT_TABLE_STMT = '''CREATE TABLE 'Result' (
	event_id INTEGER,
	member_id INTEGER,
    score INTEGER,
	FOREIGN KEY(event_id) REFERENCES EVENT(event_id),
	FOREIGN KEY(member_id) REFERENCES Member(member_id)
);'''


# TRIGGERS
# --------------
# Removes all results for a member if that member was deleted from the database
DELETE_MEMBER_FROM_RESULTS_TRIGGER = '''CREATE TRIGGER delete_member_from_result
BEFORE DELETE ON Member
FOR EACH ROW
BEGIN
    DELETE FROM Result WHERE member_id = OLD.id;
END'''


def parse_args():
    return sys.argv[1]

def create_event_table(connection):
    try:
        cursor = None
        cursor = connection.cursor()
        cursor.execute(CREATE_EVENT_TABLE_STMT)
    except sqlite3.Error, e:
        print "ERORR: There was an error creating table 'Event'"
    else:
        print "TABLE: 'Event' created successfully"


def create_member_table(connection):
    try:
        cursor = None
        cursor = connection.cursor()
        cursor.execute(CREATE_MEMBER_TABLE_STMT)
    except sqlite3.Error, e:
        print "ERORR: There was an error creating table 'Member'"
    else:
        print "TABLE: 'Member' created successfully"


def create_result_table(connection):
    try:
        cursor = None
        cursor = connection.cursor()
        cursor.execute(CREATE_RESULT_TABLE_STMT)
    except sqlite3.Error, e:
        print "ERORR: There was an error creating table 'Result'"
    else:
        print "TABLE: 'Result' created successfully"




def create_triggers(connection):
	try:
		cursor = connection.cursor()
		cursor.execute(DELETE_MEMBER_FROM_RESULTS_TRIGGER)
	except sqlite3.Error, e:
		print 'ERROR: There was a errror creating triggers.'
	else:
		print 'Trigges created successfully.'





# Creates the database and all the tables needed.
def create_sqlite_db(filepath):
	connection = None
	connection = sqlite3.connect(filepath)
	create_event_table(connection)
	create_member_table(connection)
	create_result_table(connection)
	create_triggers(connection)
	connection.close()




# Parse the filepath so the db can be create there.
db_filepath = parse_args()

# Now create the sqlite db at that filepath.
create_sqlite_db(db_filepath)
