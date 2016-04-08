from flask import Flask, Response
from flask import request
import query_db


app = Flask(__name__)


CURRENT_DB_LOCATION = "/Users/stephenfox/Desktop/sqldb"

# ------------------
# RESPONSE CODES
# ------------------
#
# Success code : 300
# Failure code : 301
#
# ------------------


@app.route('/add_member/', methods=['POST'])
def add_member():
    if request.json:
        json = request.json

        firstname = json.get("firstname")
        lastname = json.get("lastname")
        handicap = json.get("handicap")

        if not firstname:
            return Response(status=301)
        if not lastname:
            return Response(status=301)
        if not handicap:
            return Response(status=301)
        else:
            connection = query_db.get_connection(CURRENT_DB_LOCATION)
            if connection is not None:
                query_db.insert_into_member(connection, firstname, lastname, handicap)
                connection.close()
                return Response(status=300)
            else: # Connection to database failed
                return Response(status=301)
    return Response(status=301)


# Adds an event to the database.
# Success code : 300
# Failure code : 301
@app.route('/add_event/', methods=['POST'])
def add_event():
    if request.json:
        json = request.json

        title = json.get("title")
        location = json.get("location")
        time = json.get("time")
        date = json.get("date")

        if not title:
            return Response(status=301)
        if not location:
            return Response(status=301)
        if not time:
            return Response(status=301)
        if not date:
            return Response(status=301)
        else:
            connection = query_db.get_connection(CURRENT_DB_LOCATION)
            if connection is not None:
                query_db.insert_into_event(connection, title, location, time, date)
                connection.close()
                return Response(status=300)
            else: # Connection to database failed
                return Response(status=301)
    # Failure
    return Response(status=301)



@app.route('/add_result/', methods=['POST'])
def add_result():
    if request.json:
        json = request.json

        # TODO: Check that the member actually exists.
        # TODO: Check there already isnt result for the user for a given event.
        event_id = json.get("event_id")
        member_id = json.get("member_id")
        score = json.get("score")

        if not event_id:
            return Response(status=301)
        if not member_id:
            return Response(status=301)
        if not score:
            return Response(status=301)
        else:
            connection = query_db.get_connection(CURRENT_DB_LOCATION)
            if connection is not None:
                query_db.insert_into_result(connection, event_id, member_id, score)
                connection.close()
                return Response(status=300)
            else: # Connection to database failed
                return Response(status=301)
    # Failure
    return Response(status=301)



@app.route('/get_all_events', methods=['GET'])
def get_all_events():
    connection = query_db.get_connection(CURRENT_DB_LOCATION)

    json = '{"events": ['

    if connection is not None:
        events = query_db.get_all_events(connection)
        connection.close()
        if events:
            for count, event in enumerate(events, start=1):
                if event:
                    json += event.jsonify()
                    # Add comma after json object created
                    # up until the last one, then add }
                    if count is not len(events):
                        json += ',' + "\r\n"
                    else:
                        json += ' ] }'
            return Response(status=300, response=json, mimetype='application/json')
    # Failure
    return Response(status=301)


@app.route('/get_event/<identifier>', methods=['GET'])
def get_event(identifier):
    connection = query_db.get_connection(CURRENT_DB_LOCATION)

    if connection is not None:
        if identifier:
            event = query_db.get_event(connection, identifier)
            connection.close()
            if event:
                json = event.jsonify() + '\r\n'
                return Response(status=300, response=json, mimetype='application/json')
    # Failure
    return Response(status=301)


@app.route('/get_all_members/', methods=['GET'])
def get_all_members():
    connection = query_db.get_connection(CURRENT_DB_LOCATION)

    json = '{ "members": [ '
    if connection is not None:
        members = query_db.get_all_members(connection)
        connection.close()
        if members:
            for count, member in enumerate(members, start=1):
                if member:
                    json += member.jsonify()

                # Add comma after json object created
                # up until the last one, then add }
                if count is not len(members):
                    json += ',' + "\r\n"
                else:
                    json += ' ] }'
            return Response(status=300, response=json, mimetype='application/json')
    # Failure
    return Response(status=301)


@app.route('/get_member/<identifier>', methods=['GET'])
def get_member(identifier):
    connection = query_db.get_connection(CURRENT_DB_LOCATION)

    if connection is not None:
        if identifier:
            member = query_db.get_member(connection, identifier)
            connection.close()
            if member:
                json = member.jsonify() + '\r\n'
                return Response(status=300, response=json, mimetype='application/json')
    # Failure
    return Response(status=301)


@app.route('/get_all_results/', methods=['GET'])
def get_all_results():
    connection = query_db.get_connection(CURRENT_DB_LOCATION)

    json = '{ "results": [ '
    if connection is not None:
        results = query_db.get_all_results(connection)
        connection.close()
        if results:
            for count, result in enumerate(results, start=1):
                if result:
                    json += result.jsonify()

                # Add comma after json object created
                # up until the last one, then add }
                if count is not len(results):
                    json += ',' + "\r\n"
                else:
                    json += ' ] }'
            return Response(status=300, response=json, mimetype='application/json')
    # Failure
    return Response(status=301)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6565, debug=True)
