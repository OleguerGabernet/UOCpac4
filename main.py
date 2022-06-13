"""
Main script for the analysis
"""
import pprint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils import calculations, data_loader, dict_tools, frame_filters

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
QUERY_RESULT = frame_filters.find_rows_query(DATA, QUERY, COLUMNS)
print(frame_filters.find_max_col(QUERY_RESULT, 'potential', COLUMNS))

# Query 2:
print("""\n\nPorteres majors de 28 anys amb “overall” superior
a 85 al futbol femení:\n""")
QUERY = (['gender', 'player_positions', 'age', 'overall'], ['F', 'GK', (28, 100), (85, 100)])
print(frame_filters.find_rows_query(DATA, QUERY, COLUMNS))

#==================
# Ex3
# Male players BMI per country at 2022
COLUMNS = ['age', 'club_flag_url']
DF_BMI = calculations.calculate_bmi(DATA, 'M', 2022, COLUMNS)
MAX_BMI = calculations.calculate_nationality(DF_BMI).groupby('nationality',
                                                             as_index=False)['BMI'].max()

X_VALUES = MAX_BMI['nationality'].tolist()
Y_VALUES = MAX_BMI['BMI'].tolist()

X_POS = np.arange(len(X_VALUES))

plt.bar(X_POS, Y_VALUES)

plt.xticks(X_POS, X_VALUES, rotation=90, fontsize=10)

plt.yticks(fontsize=10)

plt.axhline(y=18.5, color='g', linestyle='-', linewidth=2)

plt.axhline(y=25, color='b', linestyle='-', linewidth=2)

plt.axhline(y=30, color='r', linestyle='-', linewidth=2)

plt.rcParams["figure.figsize"] = (20, 20)
plt.title("""BMI per país de jugadors masculins al 2022.\n
Les línies divideixen baix pes, pes normal, sobrepes i obès""", fontsize=10)
plt.ylabel('BMI', fontsize=10)
plt.xlabel('Nacionalitat', fontsize=10)
plt.show()

print("""Els resultats són curiosos, hem agafat el màxim de BMI i pràcticament totes\n
les nacionalitats tenen jugadors amb sobrepès. Dit això és normal que si agafem els \n
valors màxim surtin jugadors pesats, que potser no són els més atlètics, i el futbol\n
també és un joc de contacte, tenir un BMI per sobre la resta pot ser favorable en certes\n
situacions.""")

#==================
# Ex4
# Load data by year
YEARS = [2016, 2017, 2018]
DATA_E4 = data_loader.join_datasets_year('data', YEARS)
ID_LIST = [226328, 192476, 230566]
COLUMN_LIST = ["short_name", "overall", "potential", "player_positions", "year"]

DICT_E4 = dict_tools.players_dict(DATA_E4, ID_LIST, COLUMN_LIST)
print('\n\nDiccionary construït:\n')
pprint.pprint(DICT_E4)

QUERY = [("player_positions", "del_rep"), ("short_name", "one")]
pprint.pprint(QUERY)

DICT_E4_CLEAN = dict_tools.clean_up_players_dict(DICT_E4, QUERY)
print('\n\nDiccionary netejat:\n')
pprint.pprint(DICT_E4_CLEAN)

#==================
# Ex5
# Load data by year
YEARS = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
DATA_E5 = data_loader.join_datasets_year('data', YEARS)
COLUMN_LIST = ["short_name", "movement_sprint_speed", "year"]
ID_LIST = DATA_E5['sofifa_id'].tolist()

DICT_E5 = dict_tools.players_dict(DATA_E5, ID_LIST, COLUMN_LIST)

QUERY = [("short_name", "one")]

DICT_E5_CLEAN = dict_tools.clean_up_players_dict(DICT_E5, QUERY)

TOP_AVERAGE_SPRINT_SPEEDSTERS = dict_tools.top_average_column(DICT_E5_CLEAN,
                                                            'short_name',
                                                            'movement_sprint_speed', 2)

print("\n\nTop 4 futbolistes amb la millor mitjana de velocitat en sprint:\n")
pprint.pprint(TOP_AVERAGE_SPRINT_SPEEDSTERS[:4])

YEARS_1 = TOP_AVERAGE_SPRINT_SPEEDSTERS[0][2]['year']
YEARS_2 = TOP_AVERAGE_SPRINT_SPEEDSTERS[1][2]['year']
YEARS_3 = TOP_AVERAGE_SPRINT_SPEEDSTERS[2][2]['year']
YEARS_4 = TOP_AVERAGE_SPRINT_SPEEDSTERS[3][2]['year']

VALUE_1 = TOP_AVERAGE_SPRINT_SPEEDSTERS[0][2]['value']
VALUE_2 = TOP_AVERAGE_SPRINT_SPEEDSTERS[1][2]['value']
VALUE_3 = TOP_AVERAGE_SPRINT_SPEEDSTERS[2][2]['value']
VALUE_4 = TOP_AVERAGE_SPRINT_SPEEDSTERS[3][2]['value']

LABEL_1 = TOP_AVERAGE_SPRINT_SPEEDSTERS[0][0]
LABEL_2 = TOP_AVERAGE_SPRINT_SPEEDSTERS[1][0]
LABEL_3 = TOP_AVERAGE_SPRINT_SPEEDSTERS[2][0]
LABEL_4 = TOP_AVERAGE_SPRINT_SPEEDSTERS[3][0]

plt.rcParams["figure.figsize"] = (15, 15)
FIG, AX = plt.subplots()
AX.plot(YEARS_1, VALUE_1, label=LABEL_1, ls=':')
AX.plot(YEARS_2, VALUE_2, label=LABEL_2, ls='--')
AX.plot(YEARS_3, VALUE_3, label=LABEL_3, ls=':')
AX.plot(YEARS_4, VALUE_4, label=LABEL_4, ls=':')
AX.legend(fontsize=15)
plt.title("""Evolució any a any dels 4 futbolistes\n
amb la millor mitjana de velocitat en sprint""", fontsize=20)
plt.ylabel('Puntuació', fontsize=15)
plt.xlabel('Anys', fontsize=15)
plt.show()

print('\n\nFi de les solucions')
