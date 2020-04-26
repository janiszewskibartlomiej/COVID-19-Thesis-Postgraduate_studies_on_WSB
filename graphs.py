import plotly.graph_objects as go
from data_processing import DataProcessing
from connect_to_db import ConnectToDb


class Graphs(DataProcessing):

    def __init__(self):
        super().__init__()

    def creating_one_graph(self, dataframe, title_of_graph=None, country_id=None, id=False):
        if id:
            name = ConnectToDb().select_one_record(query='SELECT name from countries WHERE country_id = ?',
                                                   parameter=country_id)
            title_of_graph = f'Cases of the {name[0]}'

        fig = go.Figure()


        fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Confirmed'],
                                 mode='lines',
                                 name='Confirmed',
                                 line=dict(color='red', width=2, dash='solid')))

        fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Deaths'],
                                 mode='lines',
                                 name='Deaths',
                                 line=dict(color='black', width=2, dash='solid')))

        fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Recovered'],
                                 mode='lines',
                                 name='Recovered',
                                 line=dict(color='springgreen', width=2, dash='solid')))
        fig.update_layout(title=dict(text=title_of_graph, y=0.94,
                                     x=0.47, xanchor='center', yanchor='top', font_size=32,
                                     font=dict(family='Verdana, Sherif', color='blue')))
        fig.update_layout(xaxis_title='Date',
                          yaxis_title='Total Value of cases', font_size=20, font_family='Times new roman',
                          clickmode='event+select', hovermode='x'
                          )

        title_file = title_of_graph.split(" ")[-1]
        path = f'./templates/graphs/{title_file.lower()}.html'
        fig.write_html(path)

    def cases_of_the_world(self):
        data = DataProcessing().total_cases_per_day()
        df = DataProcessing().creating_dateframe(data=data)
        world = Graphs().creating_one_graph(dataframe=df, title_of_graph='Cases of the World')
        return world

    def cases_of_the_poland(self):
        data = DataProcessing().all_cases_per_day_where_country_id_equal(country_id=(179,))
        df = DataProcessing().creating_dateframe(data=data)
        poland = Graphs().creating_one_graph(dataframe=df, country_id=(179,), id=True)
        return poland


if __name__ == '__main__':
    Graphs().cases_of_the_world()
    Graphs().cases_of_the_poland()
