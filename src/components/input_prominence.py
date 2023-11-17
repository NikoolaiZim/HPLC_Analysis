import pandas as pd
from dash import Dash, html, dcc

from src.components import ids

def render(App: Dash) -> html.Div():
    fig =  dcc.Input(
            id=ids.PROMINENCE_INPUT,
            type='number',
            value=50
        ),   

    return html.Div(fig)

