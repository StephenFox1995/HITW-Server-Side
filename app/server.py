from flask import Flask, Response, render_template, redirect, url_for

from flask import request
from event import Event
from member import Member
from result import Result
from datetime import datetime
import image_util
import query_db
import config
import auth
import json





# Reponse codes.
SUCCESS_CODE = 200 # Success
FAILURE_CODE = 500 # Internal Server Error
MISSING_PARAM_CODE = 422 # Missing param error
PERMISSION_DENIED = 403 # Persmission denied.

IMAGE_BASE_DIRECTORY = '/Users/stephenfox/Desktop/hitw_images/'


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/events_list/', methods=['GET'])
def see_events_page():
    return render_template('eventslist.html')

@app.route('/members_list/', methods=['GET'])
def see_members_page():
    return render_template('memberslist.html')

@app.route('/admin/', methods=['GET'])
def admin_page():
    return render_template('login.html')

# Player of the year.
@app.route('/poy/', methods=['GET'])
def poy():
    return render_template('poy.html')



@app.route('/results_for_event/<identifier>', methods=['GET'])
def results_for_event(identifier):
    if not identifier:
        return Response(status=MISSING_PARAM_CODE)
    # Set this so the client can consume
    return redirect(url_for('results', id=identifier))

@app.route('/results/<int:id>', methods=['GET'])
def results(id):
    return render_template('results.html', event_id=id)


#----------------------------------------------------------------
# ADD MEMBER
#----------------------------------------------------------------
@app.route('/add_member/', methods=['POST'])
def add_member():
    if request.json:
        json = request.json
        access_token = json.get("accessToken")

        # Check that this is an admin user.
        if auth.is_admin(access_token) is False:
            return Response(status=PERMISSION_DENIED)

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


#----------------------------------------------------------------
# ADD EVENT
# Events are added with the following parameters:
#   title -         The title of the event.
#   location -      Location of the event.
#   startTeeTime -  The starting tee time.
#   endTeeTime -    The ending tee time.
#   date -          The date of the event, the format of the date
#                   must be dd-mm-yyyy.
#----------------------------------------------------------------
@app.route('/add_event/', methods=['POST'])
def add_event():
    if request.json:
        json = request.json

        access_token = json.get("accessToken")

        # Check that this is an admin user.
        if auth.is_admin(access_token) is False:
            return Response(status=PERMISSION_DENIED)

        title = json.get("title")
        location = json.get("location")
        start_tee = json.get("startTeeTime")
        end_tee = json.get("endTeeTime")
        date = json.get("date")

        formatted_date = None
        # Check date format.
        if datetime.strptime(date, '%d-%m-%Y'):
            formatted_date = Event.date_format_yyyymmdd(date)
        else:
            return Response(FAILURE_CODE)


        if not title:
            return Response(status=MISSING_PARAM_CODE)
        if not location:
            return Response(status=MISSING_PARAM_CODE)
        if not start_tee:
            return Response(status=MISSING_PARAM_CODE)
        if not date:
            return Response(status=MISSING_PARAM_CODE)
        else:
            connection = query_db.get_connection(current_db_location())
            if connection is not None:
                query_db.insert_into_event(connection, title, location, formatted_date, start_tee, end_tee)
                connection.close()
                return Response(status=SUCCESS_CODE)
            else: # Connection to database failed
                return Response(status=FAILURE_CODE)
    # Failure
    return Response(status=FAILURE_CODE)


#----------------------------------------------------------------
#  ADD RESULT
#----------------------------------------------------------------
@app.route('/add_result/', methods=['POST'])
def add_result():
    if request.json:
        json = request.json

        access_token = json.get("accessToken")
        # Check that this is an admin user.
        if auth.is_admin(access_token) is False:
            return Response(status=PERMISSION_DENIED)

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




#----------------------------------------------------------------
# ADD PLAYER OF THE YEAR
#----------------------------------------------------------------
@app.route('/add_poy/', methods=['POST'])
def add_poy():
    if request.json:
        json = request.json

        access_token = json.get('accessToken')

        # Check that this user is admin.
        if auth.is_admin(access_token) is False:
            return Response(status=PERMISSION_DENIED)

        member_id = json.get('member_id')
        year = json.get('year')
        score = json.get('score')

        if not member_id:
            return Response(status=MISSING_PARAM_CODE)
        else:
            connection = query_db.get_connection(current_db_location())
            if connection is not None:
                query_db.insert_into_poy(connection, member_id, year, score)
                connection.close()
                return Response(status=SUCCESS_CODE)
            else:
                return Response(status=FAILURE_CODE)
    else:
        return Response(status=FAILURE_CODE)


#----------------------------------------------------------------
# ADD EVENT IMAGE
#----------------------------------------------------------------
# {"event_image":
#   {
#       "image_type": "png",
#       "event_id": 2,
#       "image_data": "23i92i330ejqd"
#
# }}
#
@app.route('/add_event_image/', methods=['POST'])
def add_event_image():


    if request.json:
        json = request.json

        access_token = json.get("accessToken")

        # Check that this is an admin user.
        if auth.is_admin(access_token) is False:
            return Response(status=PERMISSION_DENIED)

        # Get json objects
        image_encoding = json.get("image_encoding")
        event_id = json.get("event_id")
        image_base64_data = json.get("image_data")

        # Images should be stored in a directory
        # under IMAGE_BASE_DIRECTORY > event id > filename.
        # Where the filename is the actual id of the image given by the database.
        # e.g. files will be stored IMAGE_BASE_DIRECTORY/EVENT_ID/2.jpeg,
        #                           IMAGE_BASE_DIRECTORY/EVENT_ID/3.jpeg etc...

        # Create parent directory where the image file will reside.
        image_parent_dir = IMAGE_BASE_DIRECTORY + str(event_id) + '/'

        # Get database connection
        connection = query_db.get_connection(current_db_location())


        # If there is not image type, encode as jpg.
        if image_encoding is None:
            # Insert into the database and retrieve the id for the image.
            # The id will be used as the image filename.
            image_filename = query_db.insert_into_event_image(connection, event_id, image_parent_dir, 'JPEG')
            image_util.jpeg_and_write_image(image_parent_dir, image_filename, image_base64_data)
        return Response(status=SUCCESS_CODE)
    else:
        return Response(status=FAILURE_CODE)




#----------------------------------------------------------------
# GET UPCOMING EVENT
#----------------------------------------------------------------
@app.route('/get_upcoming_event/', methods=['GET'])
def get_upcoming_event():
    connection = query_db.get_connection(current_db_location())
    if connection is not None:

        event = query_db.get_upcoming_event(connection)
        connection.close()

        if event:
            # Get the event date and change the date format back to dd-mm-yyyy.
            unformatted_date = event.date
            formatted_date = Event.date_format_ddmmyyyy(unformatted_date)
            event.date = formatted_date
            json = event.jsonify()
        else:
            json = empty_json_for_object("event")
        return Response(status=SUCCESS_CODE, response=json, mimetype='application/json')
    # Failure
    return Response(status=FAILURE_CODE)


#----------------------------------------------------------------
# GET ALL EVENTS
#----------------------------------------------------------------
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
                    # Get the event date and change the date format back to dd-mm-yyyy.
                    unformatted_date = event.date
                    formatted_date = Event.date_format_ddmmyyyy(unformatted_date)
                    event.date = formatted_date
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


#----------------------------------------------------------------
# GET EVENT
#----------------------------------------------------------------
@app.route('/get_event/<identifier>', methods=['GET'])
def get_event(identifier):
    if not identifier:
        return Response(status=MISSING_PARAM_CODE)

    connection = query_db.get_connection(current_db_location())
    if connection is not None:
        event = query_db.get_event(connection, identifier)
        connection.close()
        if event:
            # Get the event date and change the date format back to dd-mm-yyyy.
            unformatted_date = event.date
            formatted_date = Event.date_format_ddmmyyyy(unformatted_date)
            event.date = formatted_date
            json = event.jsonify()
        else:
            json = empty_json_for_object("event")
        return Response(status=SUCCESS_CODE, response=json, mimetype='application/json')
    # Failure
    return Response(status=FAILURE_CODE)


#----------------------------------------------------------------
# GET EVENT IMAGE
#----------------------------------------------------------------
@app.route('/get_event_image/<image_id>', methods=['GET'])
def get_event_image(image_id):
    if not image_id:
        return Response(status=MISSING_PARAM_CODE)

    connection = query_db.get_connection(current_db_location())
    if connection is not None:
        image_details = query_db.get_event_image_details(connection, image_id)

        # Get the directory the image is located.
        image_directory = image_details[0]
        image_encoding = image_details[1]
        image_id = image_details[2]
        event_id = image_details[3]

        # Get the extension for the image encoding
        image_extension = image_util.enconding_extensions(image_encoding)

        image_file = image_directory + str(image_id) + image_extension
        image_base64_encoding = image_util.get_image_base64(image_file, image_encoding)

        if image_base64_encoding:
            json = '{"image_id": "%d", "event_id": "%d", "image_data": "%s"}' % (image_id, event_id, image_base64_encoding)
            return Response(status=SUCCESS_CODE, response=json, mimetype='application/json')
        else:
            return Response(status=FAILURE_CODE)
    else:
        return Response(status=SUCCESS_CODE)


#----------------------------------------------------------------
# GET ALL EVENT IMAGES IDS
#----------------------------------------------------------------
@app.route('/get_image_ids_for_event/<int:event_id>', methods=['GET'])
def get_image_ids_for_event(event_id):
    if not event_id:
        return Response(status=MISSING_PARAM_CODE)

    json = '{ "image_ids": ['
    connection = query_db.get_connection(current_db_location())
    if connection is not None:
        identifiers = query_db.get_event_image_ids(connection, event_id)

        for count, image_id in enumerate(identifiers, start=1):
            json += str(image_id)
            if count is not len(identifiers):
                 json += ','
            else:
                json += ']}'
        return Response(status=SUCCESS_CODE, response=json, mimetype='application/json')
    else:
        return Response(status=FAILURE_CODE)







#----------------------------------------------------------------
# GET ALL MEMBERS
#----------------------------------------------------------------
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


#----------------------------------------------------------------
# GET MEMBER
#----------------------------------------------------------------
@app.route('/get_member/<identifier>', methods=['GET'])
def get_member(identifier):
    if not identifier:
        return Response(status=MISSING_PARAM_CODE)

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

#----------------------------------------------------------------
# GET ALL RESULTS
#----------------------------------------------------------------
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

#----------------------------------------------------------------
# GET ALL RESULTS FOR EVENT
#----------------------------------------------------------------
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


#----------------------------------------------------------------
# GET ALL RESULTS FOR MEMBER
#----------------------------------------------------------------
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


#----------------------------------------------------------------
# GET ALL PLAYERS OF THE YEAR
#----------------------------------------------------------------
@app.route('/get_all_poys/', methods=['GET'])
def get_all_poy():
    connection = query_db.get_connection(current_db_location())

    if connection is not None:
        results = query_db.get_all_poy(connection)
        connection.close()
        if len(results) > 0:
            # Firstly add all the years the json will contain.
            json = '{ "years": ['
            for index, (key, value) in enumerate(results.items()):
                if index == len(results) - 1:
                    json += ('"' + str(key) + '"')
                else:
                    json += ('"' + str(key) + '",')

            # Now add all the values for the years listed in the json above
            json += '], "poys": [{'
            for index, (key, value) in enumerate(results.items()):
                year = key
                poys = value

                json += '"' + str(year) + '":['

                for count, poy in enumerate(poys, start=1):
                    json += '{ "member":'

                    if count < len(poys):
                        json += poy.member.jsonify() + ','
                        json += '"score":' + str(poy.score) + '},'
                    else:
                        json += poy.member.jsonify() + ','
                        json += '"score":' + str(poy.score) + '}]' # End array for this year.

                if index == len(results) - 1:
                    json += '}]' # End the array object for all years
                else:
                    json += '}, {'
        json += '}' # End poys:

        return Response(status=SUCCESS_CODE, response=json, mimetype='application/json');


#----------------------------------------------------------------
# EDIT EVENT
#----------------------------------------------------------------
@app.route('/edit_event/<identifier>', methods=['PUT', 'DELETE'])
def edit_event(identifier):
    if not identifier:
        return Response(status=MISSING_PARAM_CODE)

    if request.json:
        json = request.json

        access_token = json.get("accessToken")
        # Check that this is an admin user.
        if auth.is_admin(access_token) is False:
            return Response(status=PERMISSION_DENIED)

        connection = query_db.get_connection(current_db_location())
        if connection is not None:
            if request.method == 'PUT': # Edit existing event.
                event = event_obj_from_json(json, identifier)
                if not event:
                    return Response(status=MISSING_PARAM_CODE)


                # Check date format.
                if datetime.strptime(event.date, '%d-%m-%Y'):
                    formatted_date = Event.date_format_yyyymmdd(event.date)
                    event.date = formatted_date
                else:
                    return Response(FAILURE_CODE)

                query_db.update_event(connection, identifier, event)
                connection.close()
                return Response(status=SUCCESS_CODE)

            elif request.method == 'DELETE': # Delete existing event
                query_db.delete_event(connection, identifier)
                connection.close()
                return Response(status=SUCCESS_CODE)
    # Failure
    return Response(status=FAILURE_CODE)


#----------------------------------------------------------------
# EDIT MEMBER
#----------------------------------------------------------------
@app.route('/edit_member/<identifier>', methods=['PUT', 'DELETE'])
def edit_member(identifier):
    if not identifier:
        return Response(status=MISSING_PARAM_CODE)

    if request.json:
        json = request.json

        access_token = json.get("accessToken")
        # Check that this is an admin user.
        if auth.is_admin(access_token) is False:
            return Response(status=PERMISSION_DENIED)

        connection = query_db.get_connection(current_db_location())
        if connection is not None:
            if request.method == 'PUT': # Edit member
                member = None
                member = member_obj_from_json(json, identifier)
                if not member:
                    return Response(status=MISSING_PARAM_CODE)
                query_db.update_member(connection, identifier, member)
                connection.close()
                return Response(status=SUCCESS_CODE)

            elif request.method == 'DELETE': # Delete member
                query_db.delete_member(connection, identifier)
                return Response(status=SUCCESS_CODE)
    # Failure
    return Response(status=FAILURE_CODE)


#----------------------------------------------------------------
# EDIT RESULT
#----------------------------------------------------------------
# Update or delete a result from the database.
@app.route('/edit_result/', methods=['PUT', 'DELETE'])
def edit_result():
    result = None

    if request.method == 'PUT':
        json = request.json

        access_token = json.get("accessToken")
        # Check that this is an admin user.
        if auth.is_admin(access_token) is False:
            return Response(status=PERMISSION_DENIED)

        result = result_obj_from_json(json)
        # All fields of the result object should be filled.
        if not result:
            return Response(status=MISSING_PARAM_CODE)

        connection = query_db.get_connection(current_db_location())
        if connection is None:
            return Response(status=FAILURE_CODE)

        query_db.update_result(connection, result, member_id_key, event_id_key)
        connection.close()
        return Response(status=SUCCESS_CODE)

    elif request.method == 'DELETE':
        json = request.json
        member_id = json.get("member_id")
        event_id = json.get("event_id")

        if not member_id or not event_id:
            return Response(status=MISSING_PARAM_CODE)

        connection = query_db.get_connection(current_db_location())
        if connection is None:
            return Response(status=FAILURE_CODE)

        query_db.delete_result(connection, member_id, event_id)
        connection.close()
        return Response(status=SUCCESS_CODE)

    else:
        # Failure
        return Response(status=FAILURE_CODE)


# Updates or deletes a player of the year record bases on the http method.
# @param identifier The identifier of the record to change.
#        Please note if the record has a new identifier that this
#        should be sent with the json part of the request.
@app.route("/edit_poy/<member_id>", methods=['PUT', 'DELETE'])
def edit_poy(member_id):
    if request.method == 'PUT':
        json = request.json
        access_token = json.get('accessToken')

        new_member_id = json.get('member_id')
        year =      json.get('year')
        score =     json.get('score')

        # Check that this is an admin user.
        if auth.is_admin(access_token) is False:
            return Response(status=PERMISSION_DENIED)

        connection = query_db.get_connection(current_db_location())
        if connection is None:
            return Response(status=FAILURE_CODE)

        query_db.update_poy(connection, member_id, new_member_id, year, score)
        connection.close()
        return Response(status=SUCCESS_CODE)

    elif request.method == 'DELETE':
        json = request.json
        access_token = json.get('accessToken')
        year =         json.get('year')

        # Check that this is an admin user.
        if auth.is_admin(access_token) is False:
            return Response(status=PERMISSION_DENIED)

        connection = query_db.get_connection(current_db_location())
        if connection is None:
            return Response(status=FAILURE_CODE)

        query_db.delete_poy(connection, member_id, year)
        connection.close()
        return Response(status=SUCCESS_CODE)

    else: # Failure
        return Response(status=FAILURE_CODE)


#----------------------------------------------------------------
# DELETE IMAGE
#----------------------------------------------------------------
@app.route("/delete_image", methods=["DELETE"])
def removeImage():
    if request.method == 'DELETE':
        json = request.json
        access_token = json.get('accessToken')
        event_id = json.get('event_id')
        image_id = json.get('image_id')

        # Check that this is an admin user.
        if auth.is_admin(access_token) is False:
            return Response(status=PERMISSION_DENIED)
        connection = query_db.get_connection(current_db_location())
        if connection is None:
            return Response(status=FAILURE_CODE)
        else:
            query_db.delete_event_image(connection, image_id)
            connection.close()

            # Remove image from disk aswell.
            image_parent_dir = IMAGE_BASE_DIRECTORY + str(event_id) + '/'
            image_util.delete_image(image_parent_dir, str(image_id) + '.jpg')
            return Response(status=SUCCESS_CODE)

#----------------------------------------------------------------
# IS ADMIN
#----------------------------------------------------------------
@app.route("/isAdmin/", methods=["POST"])
def login():

    if request.json:
        json = request.json
        fb_id = json.get('fb_id')

        # Check to see if that fb id is the
        # id of the admin stored on disk.
        data = ''
        if auth.is_admin(fb_id) == True:
            data = '{"isAdmin" : true }'
        else:
            data = '{"isAdmin" : false }'
        return Response(status=SUCCESS_CODE, response=data, mimetype='application/json')
    else:
        # Failure
        return Response(status=FAILURE_CODE)




# Attempts to create new Event object
# from json, if any of the fields
# needed to initialise the json are missing
# None will be returned.
def event_obj_from_json(json, identifier):
    title =             json.get("title")
    location =          json.get("location")
    start_tee_time =    json.get("startTeeTime")
    end_tee_time =      json.get('endTeeTime')
    date =              json.get("date")
    if not title or not location or not start_tee_time or not date:
        return None
    return Event(identifier, title, location, start_tee_time, end_tee_time, date)


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


def jsonify_event_image_data(event_image_data):
    data = { 'image' : event_image_data }
    return json.dumps(data)


def empty_json_for_array(array):
    return '{ ' + '"' + array + '"'': null}'

def empty_json_for_object(object):
    return '{ ' + '"' + object + '"'': null}'


def current_db_location():
    return config.get_db_filepath()
