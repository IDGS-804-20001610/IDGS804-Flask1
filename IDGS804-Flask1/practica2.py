
from flask import Flask, render_template, request
import math

app=Flask(__name__)

@app.route("/distance")
def operations():
    return render_template("distance.html")

@app.route("/result", methods=["POST"])
def result():
    x1 = request.form.get("txtNum1")
    y1 = request.form.get("txtNum2")
    x2 = request.form.get("txtNum3")
    y2 = request.form.get("txtNum4")
    res = math.sqrt(math.pow((int(x2) - int(x1)),2) + math.pow((int(y2) - int(y1)),2))
    return render_template("resultd.html", x1 = x1, y1 = y1, x2 = x2, y2 = y2,  res = res)

if __name__ == "__main__":
    app.run(debug=True)