from flask import Flask

app = Flask(__name__)
app.env = 'development'
app.debug = True

@app.route('/')
def index():
    return "Welcome, Day 3 class"

# 사용자로부터 숫자를 N을 입력 받아서,
# *로 N줄의 트리를 만듭니다.
@app.route('/tree/<num>')
def tree(num):
    trees = []
    for i in range(int(num)):
        trees.append("*" * (i + 1))

    return '<br>'.join(trees)

app.run()
