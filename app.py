from flask import Flask, render_template
from data_processing import DataProcessing
from graphs import Graphs
from map_of_the_world import CreatingMap

app = Flask(__name__)


@app.route('/')
def index():
    CreatingMap().map_of_the_world()
    return render_template('index.html')


@app.route('/poland')
def graph_poland():
    return render_template('./graphs/poland.html')


@app.route('/graph=<int:id>', methods=['GET', 'POST'])
def graph(id):
    if id == 0:
        return render_template('./graphs/world.html')

    data = DataProcessing().all_cases_per_day_where_country_id_equal(country_id=id)
    df = DataProcessing().creating_dateframe(data=data)
    get_graph = Graphs().get_graph(dataframe=df, country_id=id, write=True)
    return render_template('./graphs/' + get_graph[1] + '.html')


@app.route('/join=<int:first_id>&with=<int:second_id>')
def join_graphs(first_id, second_id):
    get_graphs = Graphs().join_two_graphs(first_country_id=first_id, second_country_id=second_id)
    return render_template('./graphs/' + get_graphs[1] + '.html')


if __name__ == '__main__':
    app.run(debug=True)
