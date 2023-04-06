import pandas as pd
import statistics

data = pd.read_csv('inlämning ihm.csv', sep= ";")

land = data.loc[:,'Country']

land = list(land)

print('i): Det vanligaste landet är typvärdet = ', statistics.mode(land))