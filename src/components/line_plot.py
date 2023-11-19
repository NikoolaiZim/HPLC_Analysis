import pandas as pd
from dash.exceptions import PreventUpdate
import plotly.express as px
from dash import Dash, dcc, html, State, Input, Output, callback, ctx
import plotly.graph_objects as go
from ..data.loader import DataSchema
from src.data import loader
from . import ids
from assets.styles.layout_config import layout_parameters, update_parameters
from src.components import input_saddle_point as sd



def render(app: Dash, data: pd.DataFrame) -> html.Div():

    @app.callback(
        Output(ids.LINE_PLOT, "figure"),
        [Input(ids.PROMINENCE_INPUT, 'value'),
         Input(ids.LINE_PLOT, "selectedData"),
         Input(ids.RESET_BUTTON, "n_clicks"),
         Input(ids.SADDLE_POINT_BUTTON, "n_clicks"),
         ],
         State("store", "data"),
    )
    def update_fig(prominence, selectedData, n_clicks_reset, n_clicks_saddle_point, stored_data):
        df_local_saddle_point = pd.DataFrame(columns=['R.Time (min)', 'Intensity', 'Peak Type'])
        df_local_max = loader.update_peak_values(data, prominence)
        x_range_orig = [data["R.Time (min)"].min(), data["R.Time (min)"].max()]
        y_range_orig = [data["Intensity"].min(), data["Intensity"].max() + 15000]
        

        try:
            if ctx.triggered_id == ids.RESET_BUTTON:
                x_selectedRange = x_range_orig
                y_selectedRange = y_range_orig
            elif ctx.triggered_id == ids.PROMINENCE_INPUT:
                x_selectedRange = x_range_orig
                y_selectedRange = y_range_orig
            elif ctx.triggered_id == ids.SADDLE_POINT_BUTTON:
                x_selectedRange = x_range_orig
                y_selectedRange = y_range_orig
                df_local_saddle_point = sd.calculate_saddle_point(data, n_clicks_saddle_point, stored_data)
            else:
                x_selectedRange = selectedData["range"]["x"]
                y_selectedRange = selectedData["range"]["y"]
        except:
            if type(selectedData) is list or selectedData is None:
                x_selectedRange = x_range_orig
                y_selectedRange = y_range_orig

            else:
                x_selectedRange = selectedData["range"]["x"]
                y_selectedRange = selectedData["range"]["y"]

        fig = go.Figure(
            layout=go.Layout(xaxis={"range": x_selectedRange, "title": "Retention time [min]"},
                             yaxis={"range": y_selectedRange, "title": "Intensity [mAU]"}),
            data=[go.Scatter(
                x=data[DataSchema.TIME],
                y=data[DataSchema.INTENSITY],
                mode="lines",
                line={"color": "black"}
            ),
                go.Scatter(
                x=df_local_max[DataSchema.TIME],
                y=df_local_max[DataSchema.INTENSITY],
                mode="markers",
                marker={"color": "#00bcff"},
            ),
                go.Scatter(
                x=df_local_saddle_point[DataSchema.TIME],
                y=df_local_saddle_point[DataSchema.INTENSITY],
                mode="markers",
                marker={"color": "#00bcff"},
            ),
            ],
        )

        fig.update_layout(
            **layout_parameters,
            autosize=True,
            showlegend=False,
            plot_bgcolor='white'
        )

        fig.update_scenes(**update_parameters)

        return fig

    fig = dcc.Graph(id=ids.LINE_PLOT,
                    figure=update_fig(
                        prominence=500, 
                        selectedData=None, 
                        n_clicks_reset=None, 
                        n_clicks_saddle_point=None,
                        stored_data=None),
                    style={'width': '100%', 'height': '30%'})

    return html.Div(fig)
