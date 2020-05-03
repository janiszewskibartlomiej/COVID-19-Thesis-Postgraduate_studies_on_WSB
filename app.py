from flask import Flask, render_template
from data_processing import DataProcessing
from graphs import Graphs
from map_of_the_world import CreatingMap

app = Flask(__name__)


@app.route('/')
def index():
    CreatingMap().map_of_the_world()
    return render_template('index.html')


@app.route('/graph=<int:id>')
def graph(id):
    if id == 0:
        return render_template('./graphs/world.html')

    data = DataProcessing().all_cases_per_day_where_country_id_equal(country_id=id)
    df = DataProcessing().get_dateframe(data=data)
    get_graph = Graphs().get_graph(dataframe=df, country_id=id, write=True)
    return render_template('./graphs/' + get_graph[1] + '.html')

@app.route('/graph-diff=<int:id>')
def graph_diff(id):
    if id == 0:
        return render_template('.graphs/world-diff.html')

    data = DataProcessing().all_cases_per_day_where_country_id_equal(country_id=id)
    df = DataProcessing().get_dateframe_diff(data=data)
    get_graph = Graphs().get_graph(dataframe=df, country_id=id, write=True, diff=True)
    return render_template('./graphs/' + get_graph[1] + '.html')

@app.route('/graphs')
def choice_two_graphs():
    countries = DataProcessing().get_id_and_name_of_country()
    return render_template('join-graphs.html', countries=countries)


@app.route('/join=<int:first_id>&with=<int:second_id>')
def join_two_graphs(first_id, second_id):
    get_graphs = Graphs().join_two_graphs(first_country_id=first_id, second_country_id=second_id)
    return render_template('./graphs/' + get_graphs[1] + '.html')


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='192.168.8.108', port=9000, debug=True)
