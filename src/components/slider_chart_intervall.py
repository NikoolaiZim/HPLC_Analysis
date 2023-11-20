import pandas as pd
from dash import Dash, html, dcc
from src.components import ids

# Slider used to update the table view of the peak values
def render(App: Dash, data: pd.DataFrame):
    return html.Div([
        dcc.RangeSlider(
            id=ids.SLIDER_INTERVALL,
            min=data["R.Time (min)"].min(),
            max=data["R.Time (min)"].max(),
            step=int(data["R.Time (min)"].max()/20),
            value=[data["R.Time (min)"].min(), data["R.Time (min)"].max()],
        )
    ])
