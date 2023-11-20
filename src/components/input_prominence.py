import pandas as pd
from dash import Dash, html, dcc
from src.components import ids

# The prominence value is used in the calculation of the peaks within the loader function "update_peak_values"
def render(App: Dash) -> html.Div():
    fig =  dcc.Input(
            id=ids.PROMINENCE_INPUT,
            type='number',
            value=500
        ),   

    return html.Div(fig)

