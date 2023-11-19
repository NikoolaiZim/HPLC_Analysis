from dash import Dash, html, dcc, Input, Output 


from src.components import ids  

def render(app: Dash):

    @app.callback(
        Output(ids.RESET_BUTTON, 'n_clicks'),
        Input(ids.RESET_BUTTON, 'n_clicks')
    )
    def update(reset):
        return 0

    button = html.Button(
                className="button",
                id=ids.RESET_BUTTON,
                children="Reset Graph",
            )

    return html.Div(button)
        
