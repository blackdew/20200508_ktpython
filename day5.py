from flask import Flask, render_template, request
import re
import requests
from bs4 import BeautifulSoup

app = Flask(__name__, template_folder='templates')
app.env = "development"
app.debug = True

@app.route('/')
def index():
    return "Welcome, class day 5"

@app.route('/movies', methods=['get', 'post'])
def movies():
    if request.method == "GET":
        return render_template("movies.html")

    def get_movies(week_date=''):
        url = 'https://movie.daum.net/boxoffice/weekly'
        query = {'startDate': week_date}
        res = requests.get(url, params=query)
        soup = BeautifulSoup(res.content, 'html.parser')

        movies = [dict(
            title=tag.strong.a.get_text(),
            rating=tag.em.get_text(),
            visitors=re.findall('주간관객 (\d+)명', tag.get_text()),
            opened=re.findall('([0-9\.]+) 개봉', tag.get_text()),
        ) for tag in soup.select('.desc_boxthumb')]
        return movies

    from datetime import date, timedelta
    weeks = request.form.get('weeks')
    week_list = []
    for i in range(int(weeks)):
        week_list.append(date.today() - timedelta(weeks=i))
    print(week_list)
    movies = get_movies()
    return render_template('movies.html', soup=movies)

app.run(port=5000)