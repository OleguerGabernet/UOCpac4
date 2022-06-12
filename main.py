"""
Main script for the analysis
"""
import numpy as np
import pandas as pd
import data_loader
import statistics

if __name__ == '__main__':
    # Load data by year
    years = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
    DATA = data_loader.join_datasets_year('data', years)

    # Columns that we want to retrieve
    columns = ['short_name', 'year', 'age', 'overall', 'potential']

    # Query 1:
    print('\n\nJugadors de nacionalitat belga menors de 25 anys màxim “potential” al futbol masculí:\n')
    query = (['gender', 'nationality_name', 'age'], ['M', 'Belgium', (0, 24)])
    query_result = statistics.find_rows_query(DATA, query, columns)
    print(statistics.find_max_col(query_result, 'potential', columns))

    # Query 2:
    print('\n\nPorteres majors de 28 anys amb “overall” superior a 85 al futbol femení:\n')
    query = (['gender', 'player_positions', 'age', 'overall'], ['F', 'GK', (28, 100), (85, 100)])
    print(statistics.find_rows_query(DATA, query, columns))





