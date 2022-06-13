"""
Main script for the analysis
"""
import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import calculations
import data_loader
import dict_tools
import pprint
import evolucio

#==================
# Ex1
# Load data by year
YEARS = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
DATA = data_loader.join_datasets_year('data', YEARS)

#==================
# Ex2
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

#==================
# Ex3
# Male players BMI per country at 2022
COLUMNS = ['age', 'club_flag_url']
df_bmi = calculations.calculate_bmi(DATA, 'M', 2022, COLUMNS)
max_bmi = calculations.calculate_nationality(df_bmi).groupby('nationality', 
                                                             as_index=False )['BMI'].max()

# INSERT GRAPHIC EX3

#==================
# Ex4
# Load data by year
YEARS = [2016, 2017, 2018]
DATA_E4 = data_loader.join_datasets_year('data', YEARS)
id_list = [226328, 192476, 230566]
column_list = ["short_name", "overall", "potential", "player_positions", "year"]

dict_e4 = dict_tools.players_dict(DATA_E4, id_list, column_list)
print('\n\nDiccionary construït:\n')
pprint.pprint(dict_e4)

query = [("player_positions", "del_rep"),("short_name", "one")]
pprint.pprint(query)

dict_e4_clean = dict_tools.clean_up_players_dict(dict_e4, query)
print('\n\nDiccionary netejat:\n')
pprint.pprint(dict_e4_clean)

#==================
# Ex5
# Load data by year
YEARS = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
DATA_E5 = data_loader.join_datasets_year('data', YEARS)
column_list = ["short_name", "movement_sprint_speed", "year"]
id_list = DATA_E5['sofifa_id'].tolist()

dict_e5 = dict_tools.players_dict(DATA_E5, id_list, column_list)

query = [("short_name", "one")]

dict_e5_clean = dict_tools.clean_up_players_dict(dict_e5, query)

top_average_sprint_speedsters = evolucio.top_average_column(dict_e5, 
                                                            'short_name', 
                                                            'movement_sprint_speed', 2)

print("\n\nTop 4 futbolistes amb la millor mitjana de velocitat en sprint:\n")
pprint.pprint(top_average_sprint_speedsters[:4])

years_1 = top_average_sprint_speedsters[0][2]['year']
years_2 = top_average_sprint_speedsters[1][2]['year']
years_3 = top_average_sprint_speedsters[2][2]['year']
years_4 = top_average_sprint_speedsters[3][2]['year']

value_1 = top_average_sprint_speedsters[0][2]['value']
value_2 = top_average_sprint_speedsters[1][2]['value']
value_3 = top_average_sprint_speedsters[2][2]['value']
value_4 = top_average_sprint_speedsters[3][2]['value']

label_1 = top_average_sprint_speedsters[0][0]
label_2 = top_average_sprint_speedsters[1][0]
label_3 = top_average_sprint_speedsters[2][0]
label_4 = top_average_sprint_speedsters[3][0]

plt.rcParams["figure.figsize"] = (15,15)
fig, ax = plt.subplots()
ax.plot(years_1, value_1, label=label_1, ls=':')
ax.plot(years_2, value_2, label=label_2, ls='--')
ax.plot(years_3, value_3, label=label_3, ls=':')
ax.plot(years_4, value_4, label=label_4, ls=':')
ax.legend(fontsize=15)
plt.title("""Evolució any a any dels 4 futbolistes\n 
amb la millor mitjana de velocitat en sprint""", fontsize=20)
plt.ylabel('Puntuació', fontsize=15)
plt.xlabel('Anys', fontsize=15)
plt.show()