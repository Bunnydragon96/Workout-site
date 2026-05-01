##Creating an exercise routine website using HTMl and Jinja blocks.
##Johnel Cunningham Rivera @1/29/2026

from flask import Flask, render_template

app = Flask(__name__)

##List pages of easy, medium, full, and pushup triangle.
@app.route("/")
def start_page():
    return render_template("base.html")

@app.route("/easy")
def easy_workout():
    return render_template("123exercise-easy.html")

@app.route("/medium")
def medium_workout():
    return render_template("123exercise-medium.html")

@app.route("/full")
def full_workout():
    return render_template("123exercise-full.html")

@app.route("/triangle")
def triangle_workout():
    return render_template("pushuptriangle.html")

if __name__ == "__main__":
    app.run()