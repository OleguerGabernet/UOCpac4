"""dictionaries"""
import pandas as pd
import numpy as np
from itertools import chain


def players_dict(df_in: pd.DataFrame, id_list: list, cols_list:list) -> dict:
    """dict"""
    df_in = df_in.set_index('sofifa_id')
    df_in = df_in.loc[df_in.index.isin(id_list), cols_list]
    df_in = df_in.groupby('sofifa_id', as_index='False').agg(list)
    return df_in.to_dict(orient='index')


def clean_up_players_dict(player_dict: dict, col_query: list) -> dict:
    for key, columns_dict in player_dict.items():
        for column_change in col_query:
            if column_change[1] == 'one':
                columns_dict[column_change[0]] = columns_dict[column_change[0]][0]
            elif column_change[1] == 'del_rep':
                columns_dict[column_change[0]] = [x.split(', ') for x in columns_dict[column_change[0]]]
                columns_dict[column_change[0]] = list(set(chain.from_iterable(columns_dict[column_change[0]])))
            else:
                print('incorrect column change')
        player_dict[key] = columns_dict
    return player_dict
