
from flask import Flask


app=Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/hola")
def hola():
    return "Hello IDGS804"

if __name__ == "__main__":
    app.run(debug=True)