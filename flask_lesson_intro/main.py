from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())


@app.route('/alarm_clock')
def alarm_clock():
    text = get_data()[0]['text']
    title = get_data()[0]['title']
    return render_template("alarm_clock.html", text=text, title = title)


@app.route('/headphones')
def headphones():
    text = get_data()[1]['text']
    title = get_data()[1]['title']
    return render_template("headphones.html", text=text, title=title)


@app.route('/ipod')
def ipod():
    text = get_data()[2]['text']
    title = get_data()[2]['title']
    return render_template("ipod.html", text=text, title=title)


@app.route('/calculator')
def calculator():
    text = get_data()[3]['text']
    title = get_data()[3]['title']
    return render_template("calculator.html", text=text, title=title)


@app.route('/coffeemaker')
def coffeemaker():
    text = get_data()[4]['text']
    title = get_data()[4]['title']
    return render_template("coffeemaker.html", text=text, title=title)


@app.route('/battery_charger')
def battery_charger():
    text = get_data()[4]['text']
    title = get_data()[4]['title']
    return render_template("battery_charger.html", text=text, title=title)
   

@app.route('/author')
def author():
    return render_template("author.html")


if __name__ == "__main__":
    app.run(debug=True)
