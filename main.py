from flask import Flask 

app=Flask(__name__)

@app.route("/hola")

def hola():
    return "holi"

@app.route("/wii")

def wiil():
    return "wii"

app.run()
