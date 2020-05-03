import os

import plotly.graph_objects as go
from data_processing import DataProcessing


class Graphs(DataProcessing):

    def __init__(self):
        super().__init__()

    def write_graph_to_html(self, figure, title):
        path = f'./templates/graphs/{title}.html'
        figure.write_html(path)

    def creating_figure_with_data(self, figure, dataframe, alpha_3_code, title_of_graph=' ', dash='solid', diff=False):
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
        title_y = 'Total Value of cases'
        if diff:
            title_y = 'Value of cases per day'
        figure.update_layout(xaxis_title='Date',
                             yaxis_title=title_y, font_size=20, font_family='Times new roman',
                             clickmode='event+select', hovermode='x')
        return figure

    def get_graph(self, dataframe, country_id=0, write=False, diff=False):
        if country_id > 0:
            country = Graphs().get_name_and_3code_country(country_id=country_id)

            if diff:
                title_of_graph = f'Cases of the {country[0]} per day'
            else:
                title_of_graph = f'Cases of the {country[0]}'

            alpha_3_code = country[1]

        elif country_id == 0:
            if diff:
                title_of_graph = 'Cases of the World per day'
            else:
                title_of_graph = 'Cases of the World'

            alpha_3_code = 'WOR'

        fig = go.Figure()

        if diff:
            diff = True
        else:
            diff = False
        figure = Graphs().creating_figure_with_data(figure=fig, dataframe=dataframe, alpha_3_code=alpha_3_code,
                                                    title_of_graph=title_of_graph, diff=diff)

        if diff:
            title_file = title_of_graph.split(" ")[-3]
            title_file_lower = title_file.lower() + '-diff'
        else:
            title_file = title_of_graph.split(" ")[-1]
            title_file_lower = title_file.lower()

        if write:
            Graphs().write_graph_to_html(figure=figure, title=title_file_lower)

        return figure, title_file_lower


    def join_two_graphs(self, first_country_id, second_country_id):
        if first_country_id == 0:
            first_country = ('World', 'WOR')
            first_data = DataProcessing().total_cases_per_day()

        else:
            first_country = Graphs().get_name_and_3code_country(country_id=first_country_id)
            first_data = DataProcessing().all_cases_per_day_where_country_id_equal(country_id=first_country_id)

        first_df = DataProcessing().get_dateframe(data=first_data)
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

        second_df = DataProcessing().get_dateframe(data=second_data)
        second_alpha_3_code = second_country[1]
        title_graph = f'Cases of {first_country[0]} vs {second_country[0]}'
        graph = Graphs().creating_figure_with_data(figure=figure, dataframe=second_df, alpha_3_code=second_alpha_3_code,
                                                   title_of_graph=title_graph, dash='dash')
        title_file_split = title_graph.split(' ')[2:]
        title_file = '-'.join(title_file_split)
        title_file_lower = title_file.lower()
        self.write_graph_to_html(figure=graph, title=title_file_lower)

        return graph, title_file_lower


if __name__ == '__main__':
    Graphs().join_two_graphs(first_country_id=0, second_country_id=179)
    Graphs().join_two_graphs(first_country_id=85, second_country_id=179)

    data = DataProcessing().all_cases_per_day_where_country_id_equal(country_id=179)
    df = DataProcessing().get_dateframe_diff(data=data)
    df2 = DataProcessing().get_dateframe(data=data)
    df.to_csv(path_or_buf='tests/poland-diff.csv', encoding='utf-8')
    x = Graphs().get_graph(dataframe=df, country_id=179, write=True, diff=True)
    x[0].show()

    y = Graphs().get_graph(dataframe=df2, country_id=179, write=True, diff=False)
    y[0].show()
