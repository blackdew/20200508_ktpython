from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
app.env = 'development'
app.debug = True

@app.route('/')
def index():
    # return "Welcome, class day 4"
    return render_template('index.html', message="my message")

app.run()