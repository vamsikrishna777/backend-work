from flask import Flask
from flask import jsonify
app = Flask("application")
print("test")

@app.route("/")
def hello():
       return jsonify({"meesage": "test", "flag": True})


app.run(debug=True)

