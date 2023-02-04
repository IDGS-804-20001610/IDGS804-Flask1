from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/cinepolis")
def calculate():
    return render_template("cinepolis.html")

@app.route("/ticket", methods=["POST"])
def ticket():
    name = request.form.get("txtName")
    buyers = request.form.get("txtNumBuy")
    card = request.form.get("card")
    tickets = request.form.get("txtNumTick")
    while int(tickets) <= int(buyers) * 7:
        total = 0
        costo = int(tickets) * 12
        if int(tickets) > 6:
            total = costo - (costo * .15)
        elif int(tickets) == 3 | int(tickets) == 4 | int(tickets) == 5:
            total = costo - (costo * .10)
        else:
            total = costo

        if card == "1":
            total = total - (total * .10)
        
        return render_template("cinepolisTicket.html", name = name, total = total, tickets = tickets)
    return ''' <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" href="../static/bootstrap/css/bootstrap.min.css">

    <title>Document</title>
        <style>
            body{
                padding-top: 60px;
                background-image: url("../static/img/background.jpg");
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-size: cover;
            }
            h1 {
                color: white
            }
    </style>
    <link rel="stylesheet" href="../static/bootstrap/css/bootstrap-responsive.min.css">
</head>
<body>

<div class="container">
    <div clas="row">
        <h1>NO PUEDES COMPRAR MÁS DE 7 TICKETS POR PERSONA</h1>
    </div>
</div>
</body>
</html>'''
    
@app.route("/", methods=["POST"])
def exit():
    browserExe= "chrome.exe" 
    os.system("pkill "+ browserExe)

if __name__ == "__main__":
    app.run(debug=True)

