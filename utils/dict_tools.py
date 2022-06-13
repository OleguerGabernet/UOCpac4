"""dictionaries"""
from itertools import chain
import pandas as pd
import numpy as np


def players_dict(df_in: pd.DataFrame, id_list: list, cols_list: list) -> dict:
    """dict"""
    df_in = df_in.set_index('sofifa_id')
    df_in = df_in.loc[df_in.index.isin(id_list), cols_list]
    df_in = df_in.groupby('sofifa_id', as_index='False').agg(list)
    return df_in.to_dict(orient='index')


def clean_up_players_dict(player_dict: dict, col_query: list) -> dict:
    """clean dict"""
    for key, col_dict in player_dict.items():
        for col_change in col_query:
            if col_change[1] == 'one':
                col_dict[col_change[0]] = col_dict[col_change[0]][0]
            elif col_change[1] == 'del_rep':
                col_dict[col_change[0]] = [x.split(', ') for x in col_dict[col_change[0]]]
                col_dict[col_change[0]] = list(set(chain.from_iterable(col_dict[col_change[0]])))
            else:
                print('incorrect column change')
        player_dict[key] = col_dict
    return player_dict

def top_average_column(data: dict, identifier: str, col: str, threshold: int) -> list:
    """top average"""
    tuple_list = []
    for columns_dict in data.values():
        if len(columns_dict['year']) >= threshold and not np.isnan(columns_dict[col]).any():
            mean_value = sum(columns_dict[col]) / len(columns_dict[col])
            tuple_element = (columns_dict[identifier],
                             mean_value,
                             {'value': columns_dict[col], 'year': columns_dict['year']})
            tuple_list.append(tuple_element)
    tuple_list.sort(key=lambda tup: tup[1], reverse=True)
    return tuple_list