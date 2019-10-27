from flask import Flask, render_template
first = Flask(__name__)


@first.route('/base')
def get_base():
    return render_template('base.html')


@first.route('/home')
def get_home():
    return render_template('home.html')


@first.route('/vegetables')
def get_vegetables():
    return render_template('vegetables.html',list_of_vegetables =  ['beans', 'carrot', 'beetroot', 'cucumber'])


@first.route('/fruits')
def get_fruits():
    return render_template('fruits.html')


if __name__ == "__main__":
    first.run(debug=True)