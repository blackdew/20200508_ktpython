from flask import Flask

app = Flask(__name__, static_folder="static")
app.env = 'development'
app.debug = True

@app.route('/')
def main():
    f = open('./web/index.html', 'r', encoding='utf8')
    content = f.read()
    f.close()
    return content

@app.route('/html')
def html():
    with open('./web/template.html', 'r', encoding='utf8') as f:
        content = f.read()
    return content.format('HTML', "HTML is ...")

@app.route('/css')
def css():
    with open('./web/template.html', 'r', encoding='utf8') as f:
        content = f.read()
    return content.format('CSS', "CSS is ...")


app.run(port=5001)