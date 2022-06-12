"""
Basic statistics
"""
from numbers import Number
import pandas as pd
from pandas.api.types import is_string_dtype, is_numeric_dtype


def find_max_col(df: pd.DataFrame, filter_col: str, cols_to_return: list) -> pd.DataFrame:
    """max col"""
    return df.loc[df[filter_col] == df[filter_col].max(), cols_to_return]


def string_filter(df: pd.DataFrame, column_filtered: str, filter_condition: str) -> pd.Series:
    """string filter. Contains is used in case we need to mach only a part of stirng 
    (i.e.: a player can have varous positions)
    """
    return df[column_filtered].str.contains(filter_condition, regex=False)


def numeric_filter(df: pd.DataFrame, column_filtered: str, filter_condition: Number) -> pd.Series:
    """numeric range filter"""
    return df[column_filtered].between(filter_condition[0], filter_condition[1], inclusive='both')


def find_rows_query(df: pd.DataFrame, query: tuple, cols_to_return: list) -> pd.DataFrame:
    """dataframe query"""
    mask  = pd.Series(True, index=df.index)

    for column_filtered, filter_condition in zip(query[0], query[1]):
        if is_string_dtype(df[column_filtered]):
            filter_mask = string_filter(df, column_filtered, filter_condition)
        
        elif is_numeric_dtype(df[column_filtered]):
            filter_mask = numeric_filter(df, column_filtered, filter_condition)
        
        else:
            print("QUERY: Type of the column to filter not supported")

        mask = mask & filter_mask

    return df.loc[mask, cols_to_return]
        
        

