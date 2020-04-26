from flask import Flask, render_template
from map_of_the_world import CreatingMap
from graphs import Graphs

app = Flask(__name__)


@app.route('/')
def index():
    CreatingMap().map_of_the_world()
    return render_template('index.html')


@app.route('/poland')
def graph_poland():
    Graphs().cases_of_the_poland()
    return render_template('./graphs/poland.html')


@app.route('/world')
def graph_world():
    Graphs().cases_of_the_world()
    return render_template('./graphs/world.html')


if __name__ == '__main__':
    app.run(debug=True)
