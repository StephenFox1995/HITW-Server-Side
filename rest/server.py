from flask import Flask, Response

app = Flask(__name__)

@app.route("/users/", methods=['GET'])
def get_users():
    return Response(response=jsondata, mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6565, debug=True)
