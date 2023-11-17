import pandas as pd
from functools import reduce
from typing import Callable
from scipy.signal import find_peaks


Preprocessor = Callable[[pd.DataFrame], pd.DataFrame]

class DataSchema:
    TIME = "R.Time (min)"
    INTENSITY = "Intensity"
    DATE = "Date"
    MONTH = "Month"
    YEAR = "Year"

def create_year_column(df: pd.DataFrame) -> pd.DataFrame:
    df[DataSchema.YEAR] = df[DataSchema.DATE].dt.year.astype(str)
    return df

def create_month_column(df: pd.DataFrame) -> pd.DataFrame:
    df[DataSchema.MONTH] = df[DataSchema.DATE].dt.month.astype(str)
    return df

def compose(*functions: Preprocessor) -> Preprocessor:
    return reduce(lambda f, g: lambda x: g(f(x)), functions)

def load_transaction_data(path: str) -> pd.DataFrame:
    data = pd.read_excel(path, sheet_name="DATA",
                         dtype={
                             DataSchema.TIME: float,
                             DataSchema.INTENSITY: float
                         },
                         parse_dates=[DataSchema.DATE])

    preprocessor = compose(
        create_year_column,
        create_month_column,)

    return preprocessor(data)

def update_peak_values(data: pd.DataFrame, value: int):
    peaks, _ = find_peaks(data[DataSchema.INTENSITY],
                        prominence=value, 
                        width=3, 
                        height=32000)

    local_max = {data[DataSchema.TIME][_] : data[DataSchema.INTENSITY][_] for _ in peaks}

    df_local_max = pd.DataFrame(list(local_max.items()), columns=['R.Time (min)', 'Intensity'])
    
    df_local_max["measurement"] = 1

    return df_local_max