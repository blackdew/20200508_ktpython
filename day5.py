from flask import Flask

app = Flask(__name__, template_folder='templates')
app.env = "development"
app.debug = True

@app.route('/')
def index():
    return "Welcome, class day 5"

app.run()