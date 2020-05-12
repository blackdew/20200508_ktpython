from flask import Flask, request

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
    if not num.isnumeric():
        return "not number"

    # (어제 배움) html form으로 부터 받을 때는 => request.form를 사용
    # querystring 으로 부터 받을 때는 => request.args를 사용
    print(request.args)
    print(request.args.get('order'))

    trees = []
    if request.args.get('order') == 'desc':
        for i in range(int(num)):
            trees.append("*" * (int(num) - i))
    else:
        for i in range(int(num)):
            trees.append("*" * (i + 1))

    return '<br>'.join(trees)

# 텍스트박스로 영어 텍스트를 입력받아서 
# 그 안에 있는 단어들을 카운팅합니다.
@app.route("/word_count", methods=['get', 'post'])
def word_count():
    with open('./web/word_count.html', 'r', encoding='utf8') as f:
        template = f.read()

    result = ''
    if request.method == 'POST':
        result = request.form.get('text')
        result = result.split(' ')

        # 단어를 key로 하고, 갯수를 value로 하는 word_dict
        word_dict = {}

        # result로 부터 word를 하나씩 꺼내서 (반복)
        for w in result:
            # word_dict에 단어가 있는지 확인
            if w not in word_dict:
                # 없으면 word_dict에 "단어" key 와 "0" value 추가 
                word_dict[w] = 0
            
            # word_dict의 '단어'에 +1
            word_dict[w] += 1

        result = str(word_dict)

    return template.format(result=result)

app.run()
