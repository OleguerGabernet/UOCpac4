"""calculations module. Provides some useful calculations for new columns"""
import frame_filters
import pandas as pd

def calculate_bmi(df_in: pd.DataFrame,
                  gender: str,
                  year: int,
                  cols_to_return: list) -> pd.DataFrame:
    """Add a column call BMI and calculates it"""
    query = (['gender', 'year'], [gender, (year, year)])
    cols_query_return = [*cols_to_return, 'weight_kg', 'height_cm']
    result = frame_filters.find_rows_query(df_in, query, cols_query_return)
    result['BMI'] = result.apply(lambda row: row['weight_kg']/pow(row['height_cm']/100, 2), axis=1)
    cols_to_return.append('BMI')
    return result[cols_to_return]


def calculate_nationality(df_in: pd.DataFrame) -> pd.DataFrame:
    """Set a new column with the nationality code"""
    nat = 'nationality'
    df_in[nat] = df_in.apply(lambda row: str(row['club_flag_url']).split('/')[-1].split('.')[0],
                             axis=1)
    return df_in
