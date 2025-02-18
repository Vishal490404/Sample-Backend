from flask import Flask, jsonify

app1 = Flask(__name__)

@app1.get('/')
def simpleGet():
    return jsonify({"message" : "Hello"})


if __name__ == '__main__':
    app1.run(host="0.0.0.0", port=9563)