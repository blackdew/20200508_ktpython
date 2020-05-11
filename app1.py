import os
from flask import Flask

app = Flask(__name__, static_folder="static")
app.env = 'development'
app.debug = True

def get_template(filename):
    with open(f'./web/{filename}', 'r', encoding='utf8') as f:
        content = f.read()
    return content

def get_menu():
    menus = []
    for filename in os.listdir('./content'):
        menus.append(f"<li><a href='/{filename}'>{filename}</a></li>")
    return '\n'.join(menus)

@app.route('/')
def main():
    # menus = []
    # for filename in os.listdir('./content'):
    #     menus.append(f"<li><a href='/{filename}'>{filename}</a></li>")

    template = get_template('index.html')
    return template.format(menu=get_menu())

# @app.route('/<path1>/<path2>')
# def content(path1, path2):
#     return f"{path1} {path2}"

@app.route('/<title>')
def html(title):
    template = get_template('template.html')
    with open(f"./content/{title}", 'r', encoding="utf8") as f:
        content = f.read()

    return template.format(title, content)

app.run(port=5001)