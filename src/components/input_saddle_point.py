import dash
from dash import Dash, Input, Output, html, State, dcc, ctx
from dash.exceptions import PreventUpdate
import pandas as pd
from src.components import ids
from src.data import loader


def render(App: Dash, data: pd.DataFrame) -> html.Div():
    div = html.Div(
        children=[
            dcc.Store(id='store'),
            html.Div([html.Div("Lower Boundary:", style={"margin-right": "10px"}),
                      html.Div(id=ids.LOWER_BOUNDARY_INPUT)]),
            html.Div(
                [html.Div("Upper Boundary:", style={"margin-right": "10px"}),
                 html.Div(id=ids.UPPER_BOUNDARY_INPUT)]),
            html.Button("Calculate Saddle Point",
                        id=ids.SADDLE_POINT_BUTTON,
                        n_clicks=0,
                        style={"margin-right": "150px"}),
        ],
        style={"display": "flex",
               "justify-content": "space-between", }
    )

    @App.callback(
        [Output(ids.LOWER_BOUNDARY_INPUT, "children"),
         Output(ids.UPPER_BOUNDARY_INPUT, "children"),
         Output('store', 'data')],
        [Input(ids.RESET_BUTTON, "n_clicks"),
        Input(ids.LINE_PLOT, "clickData")],
        [State('store', 'data')]
    )
    def define_boundaries(n_clicks, clickData, stored_data):
        if ctx.triggered_id == ids.RESET_BUTTON:
            return None, None, None

        if clickData is None:
            raise PreventUpdate
        else:
            x_value = clickData["points"][0]["x"]
            if stored_data is None:
                # If the store is empty, initialize it as a list with the x value
                return dash.no_update, dash.no_update, [x_value]
            else:
                # If the store already contains data, append the x value to it
                stored_data.append(x_value)
                if len(stored_data) == 2:
                    lower_boundary = stored_data[0]
                    upper_boundary = stored_data[1]
                    # Perform your calculation here
                    return lower_boundary, upper_boundary, stored_data

    @App.callback(Output(ids.CONFIRM_SP_EVALUATION, 'displayed'),
                Input(ids.SADDLE_POINT_BUTTON, 'n_clicks'),
                State('store', 'data'))
    def display_confirm(value, stored_data):
        if value > 0 and stored_data != None and len(stored_data) == 2:
            return False
        return True
    
    return div



def calculate_saddle_point(data: pd.DataFrame, n_clicks: int, stored_data: list) -> pd.DataFrame():
    if n_clicks == 0:
        raise PreventUpdate
    elif stored_data is None or len(stored_data) < 2:
        raise PreventUpdate
    else:
        lower_boundary = stored_data[0]
        upper_boundary = stored_data[1]

        return loader.get_saddle_point(data, lower_boundary, upper_boundary)
