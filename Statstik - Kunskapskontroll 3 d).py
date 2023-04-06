# Uppg. 3d)

import pandas as pd
import numpy as np

data = pd.read_csv('inlämning ihm.csv', sep= ";")

kön = data['Gender']
köp = data['Items Bought on Website']

kvinna = data[kön == 'Kvinna']['Items Bought on Website']
man = data[kön == 'Man']['Items Bought on Website']

#Listor med antalet köpta produkter för respektive.
kvinna = list(kvinna)
man = list(man)

#Loopar igenom listorna så att vi får summan av mängden köp respektive köp.
summa_kvinna = 0

for element1 in kvinna:
  if element1 > 0:
    summa_kvinna += 1
print('Mängden köp av kvinnor', summa_kvinna)

print('Sannolikhet för köp om kvinna = ', summa_kvinna/len(kvinna))

summa_man = 0

for element2 in man:
  if element2 > 0:
    summa_man += 1
print('Mängden köp av kvinnor', summa_man)

print('Sannolikhet för köp om man = ', summa_man/len(man))