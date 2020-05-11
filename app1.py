import os
from flask import Flask, request, redirect

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

    return template.format(title, content, get_menu())

@app.route('/create', methods=['get', 'post'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('descript')
        with open(f'./content/{title}', 'w', encoding='utf8') as f:
            f.write(content)
        return redirect(f'/{title}')

    template = get_template('create.html')
    return template.format(menu=get_menu())

@app.route('/<title>/delete')
def delete(title):
    # 해당 컨텐츠를 삭제를 하고 
    os.remove(f'./content/{title}')
    # 메인으로 이동
    return redirect('/')

@app.route('/login')
def login():
    template = get_template('login.html')
    return template.format(menu=get_menu())

app.run(port=5001)