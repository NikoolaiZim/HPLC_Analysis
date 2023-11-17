from dash import Dash, dcc, html, dash_table, Output, Input
import pandas as pd

from src.components import ids
from scipy.signal import find_peaks
from ..data.loader import DataSchema
from src.data import loader


def render(app: Dash, data: pd.DataFrame) -> html.Div():

    @app.callback(
        Output(ids.PEAK_TABLE, "data"),
        Input(ids.PROMINENCE_INPUT, 'value'),
        Input(ids.SLIDER_INTERVALL, 'value'),
    )
    def update_table(value, intervall):
        df_local_max = loader.update_peak_values(data, value)
        df_local_max = df_local_max[(df_local_max[DataSchema.TIME] >= intervall[0]) & (df_local_max[DataSchema.TIME] <= intervall[1])]
        return df_local_max.to_dict('records')
    
    fig = dash_table.DataTable(
            id=ids.PEAK_TABLE,
            data=update_table(50, [data["R.Time (min)"].min(), data["R.Time (min)"].max()],),
            columns=[{'name': i, 'id': i} for i in data[["R.Time (min)","Intensity"]].columns],
            page_size=10,
            style_table={"width": "90%",
                            "margin-left": "auto",
                            "margin-right": "auto"},
            style_cell={'textAlign': 'left'},
        )
    
    return html.Div(fig, style={"justify-content": "center",
        "title:": "Peak values"})
    

