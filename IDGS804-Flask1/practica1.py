
from flask import Flask
from flask import request

app=Flask(__name__)

@app.route("/operation",methods=["GET", "POST"])
def operation():
    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        value = request.form.get("operation");
        if value == "1":
            return "<h1>The result of the plus is: {} </h1>".format(str(int(num1) + int(num2)));
        if value == "2": 
            return "<h1>The result of the minus is: {} </h1>".format(str(int(num1) - int(num2)));
        if value == "3":
            return "<h1>The result of the multiplication is: {} </h1>".format(str(int(num1) * int(num2)));
        if value == "4": 
            return "<h1>The result of the division is: {} </h1>".format(str(int(num1) / int(num2)));
        return "<h1>The result of the plus is: {} </h1>".format(str(int(num1) + int(num2)));
    else:
        return '''
            <form action="/suma" method="POST">
                <label>First Number: </label>
                <input type="text" name="num1"/><br><br>

                <label>Second Number: </label>
                <input type="text" name="num2"/><br><br>

                <legend>Select what type of operation do you want to do:</legend>

                    <div>
                        <input type="radio" id="plus" name="operation" value="1">
                        <label for="plus">Plus</label>
                    </div>

                    <div>
                        <input type="radio" id="minus" name="operation" value="2">
                        <label for="minus">Minus</label>
                    </div>

                    <div>
                        <input type="radio" id="multi" name="operation" value="3">
                        <label for="multi">Multiplication</label>
                    </div>

                    <div>
                        <input type="radio" id="divi" name="operation" value="4">
                        <label for="divi">Division</label>
                    </div>

                <input type="submit" value="Calcular"/>
            </form>
            '''

if __name__ == "__main__":
    app.run(debug=True, port=3000)
    