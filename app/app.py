from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/")
def inicio():
    return render_template("public/index.html")