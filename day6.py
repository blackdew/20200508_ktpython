from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
app.env = 'development'
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

app.run()