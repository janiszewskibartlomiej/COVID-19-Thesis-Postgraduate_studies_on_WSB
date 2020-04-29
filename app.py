from flask import Flask, render_template, render_template_string
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


@app.route('/graph=<int:id>', methods=['GET', 'POST'])
def graph(id):
    get_graph = Graphs().join_two_graphs(first_country_id=179, second_country_id=20)
    return render_template('./graphs/'+get_graph+'.html')


@app.route('/world.html')
def graph_world_html():
    return render_template('./graphs/world.html')


@app.route('/germany_vs_poland')
def graph_germany_vs_poland():
    return render_template('./graphs/germany_vs_poland.html')


if __name__ == '__main__':
    app.run(debug=True)
