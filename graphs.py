import plotly.graph_objects as go
from data_processing import DataProcessing
from connect_to_db import ConnectToDb


class Graphs(DataProcessing):

    def __init__(self):
        super().__init__()

    def get_name_and_3code_country(self, country_id):
        select = ConnectToDb().select_one_record(
            query='SELECT name, alpha_3_code from countries WHERE country_id = ?',
            parameter=(country_id,))
        return select

    def creating_figure_with_data(self, figure, dataframe, alpha_3_code, title_of_graph=' ', dash='solid'):
        figure.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Confirmed'],
                                    mode='lines',
                                    name='Confirmed ' + alpha_3_code,
                                    line=dict(color='red', width=2, dash=dash)))

        figure.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Deaths'],
                                    mode='lines',
                                    name='Deaths ' + alpha_3_code,
                                    line=dict(color='black', width=2, dash=dash)))

        figure.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Recovered'],
                                    mode='lines',
                                    name='Recovered ' + alpha_3_code,
                                    line=dict(color='springgreen', width=2, dash=dash)))
        figure.update_layout(title=dict(text=title_of_graph, y=0.94,
                                        x=0.47, xanchor='center', yanchor='top', font_size=32,
                                        font=dict(family='Verdana, Sherif', color='blue')))
        figure.update_layout(xaxis_title='Date',
                             yaxis_title='Total Value of cases', font_size=20, font_family='Times new roman',
                             clickmode='event+select', hovermode='x')
        return figure

    def get_graph(self, dataframe, country_id=0, write=False):
        if country_id > 0:
            country = Graphs().get_name_and_3code_country(country_id=country_id)
            title_of_graph = f'Cases of the {country[0]}'
            alpha_3_code = country[1]

        elif country_id == 0:
            title_of_graph = 'Cases of the World'
            alpha_3_code = 'WOR'

        fig = go.Figure()
        figure = Graphs().creating_figure_with_data(figure=fig, dataframe=dataframe, alpha_3_code=alpha_3_code,
                                                    title_of_graph=title_of_graph)

        title_file = title_of_graph.split(" ")[-1]

        if write:
            Graphs().write_html_graph(figure=figure, title=title_file)

        return figure

    def write_graph_to_html(self, figure, title):
        path = f'./templates/graphs/{title.lower()}.html'
        figure.write_html(path)

    def cases_of_the_world(self, write=False):
        data = DataProcessing().total_cases_per_day()
        df = DataProcessing().creating_dateframe(data=data)
        if write:
            write = True
        world = Graphs().get_graph(dataframe=df, country_id=0, write=write)
        return world

    def cases_of_the_poland(self):
        data = DataProcessing().all_cases_per_day_where_country_id_equal(country_id=179)
        df = DataProcessing().creating_dateframe(data=data)
        poland = Graphs().get_graph(dataframe=df, country_id=179, write=True)
        return poland

    def join_two_graphs(self, first_country_id, second_country_id):

        if first_country_id == 0:
            first_country = ('World', 'WOR')
            first_data = DataProcessing().total_cases_per_day()

        else:
            first_country = Graphs().get_name_and_3code_country(country_id=first_country_id)
            first_data = DataProcessing().all_cases_per_day_where_country_id_equal(country_id=first_country_id)

        first_df = DataProcessing().creating_dateframe(data=first_data)
        first_alpha_3_code = first_country[1]
        fig = go.Figure()
        figure = Graphs().creating_figure_with_data(figure=fig, dataframe=first_df, alpha_3_code=first_alpha_3_code,
                                                    dash='solid')
        if second_country_id == 0:
            second_country = ('World', 'WOR')
            second_data = DataProcessing().total_cases_per_day()

        else:
            second_country = Graphs().get_name_and_3code_country(country_id=second_country_id)
            second_data = DataProcessing().all_cases_per_day_where_country_id_equal(country_id=second_country_id)

        second_df = DataProcessing().creating_dateframe(data=second_data)
        second_alpha_3_code = second_country[1]
        title_graph = f'Cases of {first_country[0]} vs {second_country[0]}'
        graph = Graphs().creating_figure_with_data(figure=figure, dataframe=second_df, alpha_3_code=second_alpha_3_code,
                                                   title_of_graph=title_graph, dash='dash')
        title_file = title_graph.split(' ')[2:]
        title_file = '_'.join(title_file)
        self.write_html_graph(figure=graph, title=title_file)


if __name__ == '__main__':
    Graphs().cases_of_the_world(write=True)
    Graphs().cases_of_the_poland()

    Graphs().join_two_graphs(first_country_id=179, second_country_id=0)
