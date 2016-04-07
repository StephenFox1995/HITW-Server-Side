from flask import Flask, Response
from flask import request
import query_db


app = Flask(__name__)


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
            query_db.insert_into_member(connection, firstname, lastname, handicap)
    else:
        return Response(status=301)
    return Response(status=300)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6565, debug=True)
