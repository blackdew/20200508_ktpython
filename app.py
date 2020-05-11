from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    f = open('./web/index.html', 'r', encoding='utf8')
    content = f.read()
    f.close()
    return content

app.run()