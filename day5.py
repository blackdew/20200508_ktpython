from flask import Flask, render_template
import re
import requests
from bs4 import BeautifulSoup

app = Flask(__name__, template_folder='templates')
app.env = "development"
app.debug = True

@app.route('/')
def index():
    return "Welcome, class day 5"

@app.route('/movies')
def movies():
    url = 'https://movie.daum.net/boxoffice/weekly'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    soup = soup.select('.desc_boxthumb')

    movies = []
    for tag in soup:
        title = tag.strong.a.get_text()
        rating = tag.em.get_text()
        text = tag.select('.list_state')[0].get_text()
        visitors = re.findall('주간관객 (\d+)명', text)
        opened = re.findall('([0-9\.]+) 개봉', text)
        movies.append({
            'title': title,
            'rating': rating,
            'visitors': visitors,
            'opended': opened
        })

    return render_template('movies.html', soup=movies)

app.run(port=5000)