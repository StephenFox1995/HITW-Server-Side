from flask import Flask, Response, render_template, redirect, url_for

from flask import request
from event import Event
from member import Member
from result import Result
import query_db
import config






app = Flask(__name__)
def current_db_location():
    return config.get_db_filepath()


# Reponse codes.
SUCCESS_CODE = 200 # Success
FAILURE_CODE = 500 # Internal Server Error
MISSING_PARAM_CODE = 422 # Missing param error


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/see_events_page/', methods=['GET'])
def see_events_page():
    return render_template('events.html')

@app.route('/see_members_page/', methods=['GET'])
def see_members_page():
    return render_template('members.html')


@app.route('/results_for_event/<identifier>', methods=['GET'])
def results_for_event(identifier):
    if not identifier:
        return Response(status=MISSING_PARAM_CODE)
    # Set this so the client can consume
    return redirect(url_for('results', id=identifier))


@app.route('/results/<int:id>', methods=['GET'])
def results(id):
    return render_template('results.html', event_id=id)


@app.route('/add_member/', methods=['POST'])
def add_member():
    if request.json:
        json = request.json
        firstname = json.get("firstname")
        lastname = json.get("lastname")
        handicap = json.get("handicap")

        if not firstname:
            return Response(status=MISSING_PARAM_CODE)
        if not lastname:
            return Response(status=MISSING_PARAM_CODE)
        if not handicap:
            return Response(status=MISSING_PARAM_CODE)
        else:
            connection = query_db.get_connection(current_db_location())
            if connection is not None:
                query_db.insert_into_member(connection, firstname, lastname, handicap)
                connection.close()
                return Response(status=SUCCESS_CODE)
            else: # Connection to database failed
                return Response(status=FAILURE_CODE)
    return Response(status=FAILURE_CODE)



@app.route('/add_event/', methods=['POST'])
def add_event():
    if request.json:
        json = request.json

        title = json.get("title")
        location = json.get("location")
        time = json.get("time")
        date = json.get("date")

        if not title:
            return Response(status=MISSING_PARAM_CODE)
        if not location:
            return Response(status=MISSING_PARAM_CODE)
        if not time:
            return Response(status=MISSING_PARAM_CODE)
        if not date:
            return Response(status=MISSING_PARAM_CODE)
        else:
            connection = query_db.get_connection(current_db_location())
            if connection is not None:
                query_db.insert_into_event(connection, title, location, date, time)
                connection.close()
                return Response(status=SUCCESS_CODE)
            else: # Connection to database failed
                return Response(status=FAILURE_CODE)
    # Failure
    return Response(status=FAILURE_CODE)



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
            return Response(status=MISSING_PARAM_CODE)
        if not member_id:
            return Response(status=MISSING_PARAM_CODE)
        if not score:
            return Response(status=MISSING_PARAM_CODE)
        else:
            connection = query_db.get_connection(current_db_location())
            if connection is not None:
                query_db.insert_into_result(connection, event_id, member_id, score)
                connection.close()
                return Response(status=SUCCESS_CODE)
            else: # Connection to database failed
                return Response(status=FAILURE_CODE)
    # Failure
    return Response(status=FAILURE_CODE)







@app.route('/get_all_events/', methods=['GET'])
def get_all_events():
    connection = query_db.get_connection(current_db_location())

    json = '{"events": ['

    if connection is not None:
        events = query_db.get_all_events(connection)
        connection.close()
        if len(events) > 0:
            for count, event in enumerate(events, start=1):
                if event:
                    json += event.jsonify()
                    # Add comma after json object created
                    # up until the last one, then add }
                    if count is not len(events):
                        json += ',' + "\r\n"
                    else:
                        json += ' ] }'
        else:
            json = empty_json_for_array("events")
        return Response(status=SUCCESS_CODE, response=json, mimetype='application/json')
    # Failure
    return Response(status=FAILURE_CODE)


@app.route('/get_event/<identifier>', methods=['GET'])
def get_event(identifier):
    if not identifier:
        return Response(status=MISSING_PARAM_CODE)

    json = '{ "event:" {'
    connection = query_db.get_connection(current_db_location())
    if connection is not None:
        event = query_db.get_event(connection, identifier)
        connection.close()
        if event:
            json = event.jsonify()
        else:
            json = empty_json_for_object("event")
        return Response(status=SUCCESS_CODE, response=json, mimetype='application/json')
    # Failure
    return Response(status=FAILURE_CODE)


@app.route('/get_all_members/', methods=['GET'])
def get_all_members():
    connection = query_db.get_connection(current_db_location())

    json = '{ "members": [ '
    if connection is not None:
        members = query_db.get_all_members(connection)
        connection.close()
        if len(members) > 0:
            for count, member in enumerate(members, start=1):
                if member:
                    json += member.jsonify()

                # Add comma after json object created
                # up until the last one, then add }
                if count is not len(members):
                    json += ',' + "\r\n"
                else:
                    json += ' ] }'
        else:
            json = empty_json_for_array("members")
        return Response(status=SUCCESS_CODE, response=json, mimetype='application/json')
    # Failure
    return Response(status=FAILURE_CODE)


@app.route('/get_member/<identifier>', methods=['GET'])
def get_member(identifier):
    if not identifier:
        return Response(status=MISSING_PARAM_CODE)

    json = '{ "member:" {'
    connection = query_db.get_connection(current_db_location())
    if connection is not None:
        member = query_db.get_member(connection, identifier)
        connection.close()
        if member:
            json = member.jsonify()
        else:
            json = empty_json_for_object("member")
        return Response(status=SUCCESS_CODE, response=json, mimetype='application/json')
    # Failure
    return Response(status=FAILURE_CODE)


@app.route('/get_all_results/', methods=['GET'])
def get_all_results():
    connection = query_db.get_connection(current_db_location())

    json = '{ "results": [ '
    if connection is not None:
        results = query_db.get_all_results(connection)
        connection.close()
        if len(results) > 0:
            for count, result in enumerate(results, start=1):
                if result:
                    json += result.jsonify()

                # Add comma after json object created
                # up until the last one, then add }
                if count is not len(results):
                    json += ',' + "\r\n"
                else:
                    json += ' ] }'
        else:
            json = empty_json_for_array("results")
        return Response(status=SUCCESS_CODE, response=json, mimetype='application/json')
    # Failure
    return Response(status=FAILURE_CODE)


@app.route('/get_all_results_for_event/<identifier>', methods=['GET'])
def get_all_results_for_event(identifier):
    if not identifier:
        return Response(status=MISSING_PARAM_CODE)

    connection = query_db.get_connection(current_db_location())

    json = '{ "results": [ '
    if connection is not None:
        results = query_db.get_all_results_for_event(connection, identifier)
        connection.close()
        if len(results) > 0:
            for count, result in enumerate(results, start=1):
                if result:
                    json += result.jsonify()

                # Add comma after json object created
                # up until the last one, then add }
                if count is not len(results):
                    json += ',' + "\r\n"
                else:
                    json += ' ] }'
        else: # There are no records in the database for that indentifier.
            json = empty_json_for_array("results")
        return Response(status=SUCCESS_CODE, response=json, mimetype='application/json')

    # Failure
    return Response(status=FAILURE_CODE)


@app.route('/get_all_results_for_member/<identifier>', methods=['GET'])
def get_all_results_for_member(identifier):
    if not identifier:
        return Response(status=MISSING_PARAM_CODE)

    connection = query_db.get_connection(current_db_location())

    json = '{ "results": [ '
    if connection is not None:
        results = query_db.get_all_results_for_member(connection, identifier)
        connection.close()
        if len(results) > 0:
            for count, result in enumerate(results, start=1):
                if result:
                    json += result.jsonify()

                # Add comma after json object created
                # up until the last one, then add }
                if count is not len(results):
                    json += ',' + "\r\n"
                else:
                    json += ' ] }'
        else: # There are no records in the database for that indentifier.
            json = empty_json_for_array("results")
        return Response(status=SUCCESS_CODE, response=json, mimetype='application/json')

    # Failure
    return Response(status=FAILURE_CODE)


@app.route('/edit_event/<identifier>', methods=['PUT', 'DELETE'])
def edit_event(identifier):
    event = None
    if not identifier:
        return Response(status=MISSING_PARAM_CODE)

    if request.json:
        json = request.json
        event = event_obj_from_json(json, identifier)
        if not event:
            return Response(status=MISSING_PARAM_CODE)

    connection = query_db.get_connection(current_db_location())
    if connection is not None:
        if request.method == 'PUT':
            query_db.update_event(connection, identifier, event)
            connection.close()
            return Response(status=SUCCESS_CODE)
        elif request.method == 'DELETE':
            query_db.delete_event(connection, identifier)
            return Response(status=SUCCESS_CODE)
    # Failure
    return Response(status=FAILURE_CODE)


@app.route('/edit_member/<identifier>', methods=['PUT', 'DELETE'])
def edit_member(identifier):
    member = None

    if not identifier:
        return Response(status=MISSING_PARAM_CODE)

    # JSON content for PUT method
    if request.json:
        json = request.json
        member = member_obj_from_json(json, identifier)
        if not member:
            return Response(status=MISSING_PARAM_CODE)


    connection = query_db.get_connection(current_db_location())
    if connection is not None:
        if request.method == 'PUT':
            query_db.update_member(connection, identifier, member)
            connection.close()
            return Response(status=SUCCESS_CODE)
        elif request.method == 'DELETE':
            query_db.delete_member(connection, identifier);
            return Response(status=SUCCESS_CODE)
    # Failure
    return Response(status=FAILURE_CODE)



# Update or delete a result from the database.
@app.route('/edit_result/', methods=['PUT', 'DELETE'])
def edit_result():
    result = None
    # As this function can take an PUT and DELETE
    # request, json content can't be garaunteed.
    # For this reason, keep executing the code
    # as it may be a DELETE.
    if request.json:
        json = request.json
        result = result_obj_from_json(json)
        if not result:
            return Response(status=MISSING_PARAM_CODE)


    member_id_key = request.args.get("mem_id")
    event_id_key = request.args.get("event_id")

    if not member_id_key or not event_id_key:
        return Response(status=MISSING_PARAM_CODE)

    connection = query_db.get_connection(current_db_location())
    if connection is None:
        return Response(status=FAILURE_CODE)

    if request.method == 'PUT':
        query_db.update_result(connection, result, member_id_key, event_id_key)
        connection.close()
        return Response(status=SUCCESS_CODE)
    elif request.method == 'DELETE':
        query_db.delete_result(connection, member_id_key, event_id_key)
        connection.close()
        return Response(status=SUCCESS_CODE)

    # Failure
    return Response(status=FAILURE_CODE)




# Attempts to create new Event object
# from json, if any of the fields
# needed to initialise the json are missing
# None will be returned.
def event_obj_from_json(json, identifier):
    title = json.get("title")
    location = json.get("location")
    time = json.get("time")
    date = json.get("date")
    if not title or not location or not time or not date:
        return None

    return Event(identifier, title, location, time, date)

# Attempts to create new Member object
# from json, if any of the fields
# needed to initialise the json are missing
# None will be returned.
def member_obj_from_json(json, identifier):
    firstname = json.get("firstname")
    lastname = json.get("lastname")
    handicap = json.get("handicap")
    if not firstname or not lastname or not handicap:
        return None
    return Member(identifier, firstname, lastname, handicap)


# Attempts to create new Result object
# from json, if any of the fields
# needed to initialise the json are missing
# None will be returned.
def result_obj_from_json(json):
    member_identifier = json.get("member_id")
    event_identifier = json.get("event_id")
    score = json.get("score")

    if not member_identifier or not event_identifier or not score:
        return None

    result = Result(event_identifier, member_identifier, score)
    return result




def empty_json_for_array(array):
    return '{ ' + '"' + array + '"'': null}'

def empty_json_for_object(object):
    return '{ ' + '"' + object + '"'': null}'



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6565, debug=True)
