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

def update_peak_values(data: pd.DataFrame, prominence: int):
    peaks, _ = find_peaks(data[DataSchema.INTENSITY],
                        prominence=prominence, 
                        width=3, 
                        height=32000)

    saddlepoint_time, saddlepoint_intensity = get_saddle_point(data,1320,1327)

    local_max_dict = {data[DataSchema.TIME][_] : data[DataSchema.INTENSITY][_] for _ in peaks}

    local_max_dict[saddlepoint_time] = saddlepoint_intensity

    df_local_max = pd.DataFrame(dict(local_max_dict.items()), columns=['R.Time (min)', 'Intensity'])
        
    df_local_max["measurement"] = 1

    return df_local_max

def get_saddle_point(data: pd.DataFrame, lower_limit, upper_limit):
    
    delta_dict = {}
    for index, row in data.iterrows():
        if index > lower_limit and index < upper_limit:
            
            current_time = data.iloc[index+1]["R.Time (min)"]
            current_row_values = row[['R.Time (min)', 'Intensity']]
            next_row_values = data.iloc[row.name + 1][['R.Time (min)', 'Intensity']]
       
            delta_current = abs((next_row_values - current_row_values)["Intensity"])

            delta_dict[index+1] = delta_current

        else:
            continue
        
    saddlepoint_index = min(delta_dict, key=delta_dict.get)
    saddlepoint_time = data.iloc[saddlepoint_index-1]["R.Time (min)"]
    saddlepoint_intensity = data.iloc[saddlepoint_index-1]["Intensity"]
    
    return saddlepoint_time, saddlepoint_intensity


