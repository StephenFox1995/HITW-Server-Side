import os
import json



# Returns a flag which determines if the user id
# is the id of the admin user.
def is_admin(auth_attempt_id):
    print auth_attempt_id
    print  get_auth_id()
    if auth_attempt_id == get_auth_id():
        return True
    else:
        return False


# Gets the authorized id of the admin user.
def get_auth_id():
    return get_auth_user_id()


# Returns the user id of the admin stored on disk.
def get_auth_user_id():
    DEFAULT_AUTH_LOCATION = '/etc/hitw/'
    AUTH_FILE = 'hitw_auth'

    filepath = DEFAULT_AUTH_LOCATION + AUTH_FILE
    with open(DEFAULT_AUTH_LOCATION + AUTH_FILE, 'r') as auth_file:
        json_data = json.load(auth_file)
        auth_file.close()
    return parse_auth_user(json_data)


def parse_auth_user(json):
    return json['auth_user_id'];
