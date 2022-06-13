"""dictionaries"""
from itertools import chain
import pandas as pd


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
