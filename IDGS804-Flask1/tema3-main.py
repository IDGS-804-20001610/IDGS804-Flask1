
from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

#Pasamos un string
@app.route("/username/<string:username>")
def username(username):
    return "Hello " +  username

#Pasamos un int
@app.route("/number/<int:n>")
def number(n):
    return "Number: {}".format(n);

#Pasamos más de un parámetro
@app.route("/user/<int:id>/<string:username>")
def user(id, username):
    return "ID: {} nombre: {}".format(id,username)

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return "RESULTADO DE LA SUMA {} + {} = ".format(n1, n2) + (n1+n2);

if __name__ == "__main__":
    app.run(debug=True,port=3000)