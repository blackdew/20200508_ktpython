from flask import Flask

app = Flask(__name__)
app.env = 'development'
app.debug = True

@app.route('/')
def index():
    return "Welcome, Day 3 class"

app.run()
