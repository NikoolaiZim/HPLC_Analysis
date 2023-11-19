from dash import Dash,html
from dash_bootstrap_components.themes import BOOTSTRAP, LUX
from src.layout.layout import create_layout
from src.data.loader import load_transaction_data

DATA_PATH = "./data/HPLC_DATA.xlsx"    

def main() -> None:
    data = load_transaction_data(DATA_PATH)
    app = Dash(external_stylesheets=[LUX])
    app.title = " HPLC Data Analysis"
    app.layout = create_layout(app, data)
    app.run()
    

if __name__ == "__main__":
    main() 