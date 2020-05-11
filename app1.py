from flask import Flask

app = Flask(__name__, static_folder="static")
app.env = 'development'
app.debug = True

def get_template(filename):
    with open(f'./web/{filename}', 'r', encoding='utf8') as f:
        content = f.read()
    return content

@app.route('/')
def main():
    template = get_template('index.html')
    return template

@app.route('/html')
def html():
    template = get_template('template.html')
    return template.format('HTML', "HTML is ...")

@app.route('/css')
def css():
    template = get_template('template.html')
    return template.format('CSS', "CSS is ...")


app.run(port=5001)