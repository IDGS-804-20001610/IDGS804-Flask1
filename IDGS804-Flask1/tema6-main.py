
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/data")
def data():
    name = "Amanda"
    list1 = ["uno", "dos", "tres", "cuatro"]
    return render_template("datos.html", name = name, list1 = list1)

if __name__ == "__main__":
    app.run(debug=True)