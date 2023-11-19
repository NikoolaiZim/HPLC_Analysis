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
        df_local_max = df_local_max[(df_local_max[DataSchema.TIME] >= intervall[0]) & (
            df_local_max[DataSchema.TIME] <= intervall[1])]
        df = df_local_max.rename(columns={
            "R.Time (min)": "Retention Time [min]",
            "Intensity": "Intensity [AU × 10⁻³]",
            "Peak Type": "Peak Type"
        })
        return df.to_dict('records')

    df = update_table(500, [data["R.Time (min)"].min(),
                      data["R.Time (min)"].max()],)

    fig = dash_table.DataTable(
        id=ids.PEAK_TABLE,
        data=df,
        columns=[{'name': i, 'id': i} for i in [
            "Retention Time [min]", "Intensity [AU × 10⁻³]", "Peak Type"]],
        page_size=10,
        style_table={"width": "90%",
                     "margin-left": "auto",
                     "margin-right": "auto"},
        style_cell={'textAlign': 'left'},
    )

    return html.Div(fig, style={"justify-content": "center",
                                "title:": "Peak values"})
