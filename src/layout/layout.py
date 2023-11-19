from dash import Dash, html
import pandas as pd


from src.components import input_prominence, line_plot, slider_chart_intervall, table_peaks, button_reset


def create_layout(app: Dash, data: pd.DataFrame) -> html.Div():
    return html.Div(
        className="app-div",
        style={"width": "100%", "height": "2000px",
               "background-color": "#f8f9fa"},
        children=[

            html.Div(children=[html.H1(app.title,
                                       style={"color": "#00bcff"},
                                       ),
                               html.Img(src=app.get_asset_url('images/logo.png'),
                                        style={"width": "150px"},),],
                     style={"display": "flex",
                            "justify-content": "space-between",
                            "heigth": "50px",
                            "margin-right": "40px"},),
            html.Hr(),
            html.H3("Measurement 1 - Triphenylamine"),
            line_plot.render(app, data),
            html.Div(button_reset.render(app),
                     style={"display": "flex",
                            "justify-content": "flex-end",
                            "margin-right": "150px",
                            "margin-top": "10px", }),
            html.Hr(),
            html.H5("Define Time Intervall"),
            html.Div(html.Div(slider_chart_intervall.render(app, data),
                              style={"width": "70%"}),
                     style={"display": "flex", "justify-content": "center"}),
            html.Hr(),
            html.H5("Define Peak Prominence"),
            html.Div(
                input_prominence.render(app),
                style={"title:": "Peak Prominence",
                       "justify-content": "center",
                       }
            ),
            html.Hr(),
            html.H5("Sample Peaks"),
            html.Div(
                table_peaks.render(app, data),
                style={"title:": "Peak values",
                       "justify-content": "center",
                       }
            ),
        ],
    )
