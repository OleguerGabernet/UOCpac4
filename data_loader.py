"""Module providingFunction printing python version."""
import os
import pandas as pd


def read_add_year_gender(filepath: str, gender: str, year: int) -> pd.DataFrame:
    """
    Loads the file
    """
    df_gender_year = pd.read_csv(filepath, low_memory=False)
    return df_gender_year.assign(**{'gender':gender, 'year':year})


def join_male_female(path: str, year: int) -> pd.DataFrame:
    """
    Loads the file
    """
    year_suffix = str(year%100)
    # read csv files
    female_data = read_add_year_gender(os.path.join(path, f'female_players_{year_suffix}.csv'), 'F', year)
    male_data = read_add_year_gender(os.path.join(path, f'players_{year_suffix}.csv'), 'M', year)
    # union both dataFrames
    return pd.concat([female_data, male_data], ignore_index=True)


def join_datasets_year(path: str, years: list) -> pd.DataFrame:
    """
    Loads the file
    """
    # read the first year data
    df_1 = join_male_female(path, years.pop(0))
    # read the other year data concatenating it to the first
    for year in years:
        df_2 = join_male_female(path, year)
        df_1 = pd.concat([df_1, df_2], ignore_index=True)
    return df_1
