import plotly.graph_objects as go
from data_processing import DataProcessing


class DataGraph(DataProcessing):

    def __init__(self):
        super().__init__()

    def creating_graph(self, dataframe, title_of_graph, country_id=False):
        if country_id:
            name = DataProcessing.select_one_record('SELECT name from coutries WHERE country_id = ?', country_id)
            title_of_graph = f'Cases of the {name}'

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
                          yaxis_title='Total Value of cases', font_size=20, font_family='Times new roman')

        path = f'./templates/graphs/{title_of_graph.split(" ")[-1]}.html'
        fig.write_html(path)


if __name__ == '__main__':
    data = DataProcessing().total_cases_per_day()
    dataframe = DataProcessing().creating_dateframe(data=data)
    DataGraph().creating_graph(dataframe=dataframe, title_of_graph='Cases of the World')
