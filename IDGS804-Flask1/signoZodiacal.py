from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/form")
def next():
    return render_template("zodiacForm.html")

@app.route("/results", methods=["POST"])
def show():
    name = request.form.get("txtName")
    lastName1 = request.form.get("txtLastName1")
    lastName2 = request.form.get("txtLastName2")
    day = request.form.get("txtDay")
    month = request.form.get("txtMonth")
    year = request.form.get("txtYear")
    sex = request.form.get("sex")
    age = 0

    answer1 = request.form.get("question1")
    answer2 = request.form.get("question2")
    answer3 = request.form.get("question3")
    answer4 = request.form.get("question4")
    answer5 = request.form.get("question5")

    if int(month) > 2:
        age = 2022 - int(year)
    elif int(month) <= 2:
        if int(day) > 8:
            age = 2022 - int(year)
        elif int(day) <= 8:
            age = 2023 - int(year)

    if answer1 == "4":
        answer1 = 1
    else: 
        answer1 = 0

    if answer2 == "1":
        answer2 = 1
    else: 
        answer2 = 0

    if answer3 == "3":
        answer3 = 1
    else: 
        answer3 = 0

    if answer4 == "1":
        answer4 = 1
    else: 
        answer4 = 0

    if answer5 == "2":
        answer5 = 1
    else: 
        answer5 = 0

    results = answer1 + answer2 + answer3 + answer4 + answer5

    zodiac = ""
    image = ""
    anio = int(year)
    while anio > 1911:
        anio -= 12
        if anio == 1900:
            zodiac = "RATA"
            image = "../static/img/rata.jpg"
        elif anio == 1901:
            zodiac = "BUEY"
            image = "../static/img/buey.png"
        elif anio == 1902:
            zodiac = "TIGRE"
            image = "../static/img/tigre.png"
        elif anio == 1903:
            zodiac = "CONEJO"
            image = "../static/img/conejo.avif"
        elif anio == 1904:
            zodiac = "DRAGÓN"
            image = "../static/img/dragon.png"
        elif anio == 1905:
            zodiac = "SERPIENTE"
            image = "../static/img/serpiente.jpg"
        elif anio == 1906:
            zodiac = "CABALLO"
            image = "../static/img/caballo.png"
        elif anio == 1907:
            zodiac = "CABRA"
            image = "../static/img/cabra.png"
        elif anio == 1908:
            zodiac = "MONO"
            image = "../static/img/mono.png"
        elif anio == 1909:
            zodiac = "GALLO"
            image = "../static/img/gallo.png"
        elif anio == 1910:
            zodiac = "PERRO"
            image = "../static/img/perro.png"
        elif anio == 1911:
            zodiac = "CERDO"
            image = "../static/img/cerdo.png"

    return render_template("zodiacResults.html", name = name, lastName1 = lastName1, 
        lastName2 = lastName2, age = age, zodiac = zodiac, image = image, results = results)

if __name__ == "__main__":
    app.run(debug=True)
