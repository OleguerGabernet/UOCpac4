"""
Basic statistics
"""
from numbers import Number
import pandas as pd
from pandas.api.types import is_string_dtype, is_numeric_dtype


def find_max_col(df_in: pd.DataFrame, filter_col: str, cols_to_return: list) -> pd.DataFrame:
    """max col"""
    return df_in.loc[df_in[filter_col] == df_in[filter_col].max(), cols_to_return]


def string_filter(df_in: pd.DataFrame, column_filtered: str, filter_condition: str) -> pd.Series:
    """string filter. Contains is used in case we need to mach only a part of stirng
    (i.e.: a player can have varous positions)
    """
    return df_in[column_filtered].str.contains(filter_condition, regex=False)


def numeric_filter(df_in: pd.DataFrame,
                   column_filtered: str,
                   filter_condition: Number) -> pd.Series:
    """numeric range filter"""
    return df_in[column_filtered].between(filter_condition[0],
                                          filter_condition[1],
                                          inclusive='both')


def find_rows_query(df_in: pd.DataFrame, query: tuple, cols_to_return: list) -> pd.DataFrame:
    """dataframe query"""
    mask = pd.Series(True, index=df_in.index)

    for column_filtered, filter_condition in zip(query[0], query[1]):
        if is_string_dtype(df_in[column_filtered]):
            filter_mask = string_filter(df_in, column_filtered, filter_condition)

        elif is_numeric_dtype(df_in[column_filtered]):
            filter_mask = numeric_filter(df_in, column_filtered, filter_condition)

        else:
            print("QUERY: Type of the column to filter not supported")

        mask = mask & filter_mask

    return df_in.loc[mask, cols_to_return]
        