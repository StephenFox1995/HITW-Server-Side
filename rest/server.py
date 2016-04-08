from flask import Flask, Response
from flask import request
import query_db


app = Flask(__name__)

# Adds an member to the database.
# Success code : 300
# Failure code : 301
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
            connection = query_db.get_connection("/Users/stephenfox/Desktop/sqldb")
            if connection is not None:
                query_db.insert_into_member(connection, firstname, lastname, handicap)
            else:
                return Response(status=301)
    else:
        return Response(status=301)
    return Response(status=300)


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
            connection = query_db.get_connection("/Users/stephenfox/Desktop/sqldb")

            if connection is not None:
                query_db.insert_into_event(connection, title, location, time, date)
            else:
                return Response(status=301)

    else:
        return Response(status=301)
    return Response(status=300)


@app.route('/add_result/', methods=['POST'])
def add_result():
    if request.json:
        json = request.json

        # TODO: Check that the member actually exists.
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
            connection = query_db.get_connection("/Users/stephenfox/Desktop/sqldb")

            if connection is not None:
                query_db.insert_into_result(connection, event_id, member_id, score)
            else:
                return Response(status=301)

    else:
        return Response(status=301)
    return Response(status=300)


@app.route('/get_all_events', methods=['GET'])
def get_all_events():
    connection = query_db.get_connection("/Users/stephenfox/Desktop/sqldb")
    query_db.get_all_events(connection)

    return Response(status=301)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6565, debug=True)
