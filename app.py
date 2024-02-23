from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/helloworld", methods=['GET'])
def helloworld():
    if (request.method == 'GET'):
        data = {"data": "Hello mom lol"}
        return jsonify(data)
    

if __name__ == '__main__':
    app.run(debug=True)