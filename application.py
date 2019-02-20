from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    now = datetime.datetime.now()
    is_new_year = now.month == 1 and now.day == 1
    return render_template("index.html", is_new_year=is_new_year)
