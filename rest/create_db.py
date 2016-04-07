
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
	player_id INTEGER,
	FOREIGN KEY(event_id) REFERENCES EVENT(event_id),
	FOREIGN KEY(player_id) REFERENCES PLAYER(player_id)
);'''


def parse_args():
    return sys.argv[1]

def create_event_table(connection):
    print "CREATING TABLE: 'Event'"
    print CREATE_EVENT_TABLE_STMT
    try:
        cursor = None
        cursor = connection.cursor()
        cursor.execute(CREATE_EVENT_TABLE_STMT)
    except lite.Error, e:
        print "ERORR: There was an error creating table 'Event'"

    print "TABLE: 'Event' created successfully"

def create_member_table(connection):
    print "CREATING TABLE: 'Member'"
    print CREATE_EVENT_TABLE_STMT
    try:
        cursor = None
        cursor = connection.cursor()
        cursor.execute(CREATE_MEMBER_TABLE_STMT)
    except lite.Error, e:
        print "ERORR: There was an error creating table 'Member'"

    print "TABLE: 'Member' created successfully"



def create_result_table(connection):
    print "CREATING TABLE: 'Result'"
    print CREATE_EVENT_TABLE_STMT
    try:
        cursor = None
        cursor = connection.cursor()
        cursor.execute(CREATE_RESULT_TABLE_STMT)
    except lite.Error, e:
        print "ERORR: There was an error creating table 'Member'"

    print "TABLE: 'Result' created successfully"



# Creates the database and all the tables needed.
def create_sqlite_db(filepath):
    connection = None
    connection = sqlite3.connect(filepath)
    create_event_table(connection)
    create_member_table(connection)
    create_result_table(connection)






# Parse the filepath so the db can be create there.
db_filepath = parse_args()

# Now the sqlite db at that filepath.
create_sqlite_db(db_filepath)
