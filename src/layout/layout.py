from dash import Dash, html
import pandas as pd

from src.components import input_prominence, line_plot, slider_chart_intervall, table_peaks, button_reset


def create_layout(app: Dash, data: pd.DataFrame) -> html.Div():
    return html.Div(
        className="app-div",
        style={"width": "100%", "height": "2000px",
               "background-color": "#f8f9fa"},
        children=[
            html.H1(app.title),
            html.Hr(),
            html.H3("Measurement 1 - Triphenylamine"),
            line_plot.render(app, data),
            html.Hr(),
            html.H5("Define Time Intervall"),
            html.Div(slider_chart_intervall.render(app, data),),
            html.Hr(),
            button_reset.render(app),
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
