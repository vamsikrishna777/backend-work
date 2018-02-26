from flask import Flask
from flask import jsonify
app = Flask("application")
print("test")

@app.route("/")
def hello():
       return jsonify({"meesage": "test", "flag": True})

if __name__ == '__main__':
       app.run(debug=True)

