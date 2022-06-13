"""
Main script for the analysis
"""
import statistics
import numpy as np
import pandas as pd
import calculations
import data_loader

if __name__ == '__main__':
    # Load data by year
    YEARS = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
    DATA = data_loader.join_datasets_year('data', YEARS)

    # Columns that we want to retrieve
    COLUMNS = ['short_name', 'year', 'age', 'overall', 'potential']

    # Query 1:
    print("""\n\nJugadors de nacionalitat belga menors de 25 anys
amb màxim “potential” al futbol masculí:\n""")
    QUERY = (['gender', 'nationality_name', 'age'], ['M', 'Belgium', (0, 24)])
    query_result = statistics.find_rows_query(DATA, QUERY, COLUMNS)
    print(statistics.find_max_col(query_result, 'potential', COLUMNS))

    # Query 2:
    print("""\n\nPorteres majors de 28 anys amb “overall” superior
a 85 al futbol femení:\n""")
    QUERY = (['gender', 'player_positions', 'age', 'overall'], ['F', 'GK', (28, 100), (85, 100)])
    print(statistics.find_rows_query(DATA, QUERY, COLUMNS))

    # Male players BMI per country at 2022
    COLUMNS = ['age', 'club_flag_url']
    df_bmi = calculations.calculate_bmi(DATA, 'M', 2022, COLUMNS)
    max_bmi = calculations.calculate_nationality(df_bmi).groupby('nationality')['BMI'].max()
    print(max_bmi)
