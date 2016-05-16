import os
import json

DEFAULT_CONFIG_LOCATION = '/etc/hitw/'
CONFIG_FILE = 'config'

def write_db_filepath(filepath):
    db_location_info = '{"db_location":"' + filepath + '"}\n'

    f = get_config_file()
    f.write(db_location_info)
    f.close()



# Retunrs the filepath of the database.
def get_db_filepath():
    filepath = DEFAULT_CONFIG_LOCATION + CONFIG_FILE
    with open(DEFAULT_CONFIG_LOCATION + CONFIG_FILE, 'r') as config_file:
        json_data = json.load(config_file)
        config_file.close()
    return parse_db_location(json_data)


def parse_db_location(json):
    return json['db_location']



# Returns a opened file reference to read/write configurations.
def get_config_file():
    # Check and see if the directory already exists.
    if not os.path.exists(DEFAULT_CONFIG_LOCATION):
        os.makedirs(DEFAULT_CONFIG_LOCATION)
    f = open(DEFAULT_CONFIG_LOCATION + CONFIG_FILE, 'a')
    return f;
