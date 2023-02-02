
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/operations")
def operations():
    return render_template("operations.html")

@app.route("/result", methods=["POST"])
def result():
    n1 = request.form.get("txtNum1")
    n2 = request.form.get("txtNum2")
    res = int(n1) * int(n2)
    return render_template("result.html", n1 = n1, n2 = n2, res = res)

if __name__ == "__main__":
    app.run(debug=True)