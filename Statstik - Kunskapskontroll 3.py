#Kunskapskontroll uppg 3

import pandas as pd
import numpy as np

data = pd.read_csv('inlämning ihm.csv', sep= ";")

#a)
#lista med antalet köpta items
nr_items = data.loc[:,'Items Bought on Website']
nr_items = list(nr_items)

summa = 0
for x in nr_items:
  if x > 0:
    summa +=1

probability = summa/2000

print('a) Sannolikheten = ', probability)

#b)
r = 3 #antalet typer av reklam
p = 5 #Antalet typer av produkt

svar = r*p
print('b)Svar = ', svar)

#c) Produkter: familj, lyx, budget och sport
typ = data['Direction of Commercial']
köp = data['Items Bought on Website']

sport = data[typ == 'Husbil-Sport']['Items Bought on Website']
lyx = data[typ == 'Husbil-Lyx']['Items Bought on Website']
budget = data[typ == 'Husbil-Budget']['Items Bought on Website']
familj = data[typ == 'Husbil-Familj']['Items Bought on Website']

#Listor med antalet köpta produkter för varje produktkategori.
sport = list(sport)
lyx = list(lyx)
budget = list(budget)
familj = list(familj)

print('Nedan följer flera rader kod med lösning till uppg. 3c)')

#print(sport)
print('Mängden reklam med husbil-sport = ', len(sport))
print('Mängden reklam med husbil-lyx = ', len(lyx))
print('Mängden reklam med husbil-budget = ', len(budget))
print('Mängden reklam med husbil-familj = ', len(familj))

summa_sport = 0

for element1 in sport:
  if element1 > 0:
    summa_sport += 1
print('Mängden gynnsamma utfall för sport', summa_sport)

summa_lyx = 0

for element2 in lyx:
  if element2 > 0:
    summa_lyx += 1
print('Mängden gynnsamma utfall för lyx', summa_lyx)

summa_budget = 0

for element3 in budget:
  if element3 > 0:
    summa_budget += 1
print('Mängden gynnsamma utfall för budget', summa_budget)

summa_familj = 0

for element4 in familj:
  if element4 > 0:
    summa_familj += 1
print('Mängden gynnsamma utfall för familj', summa_familj)

print('P(sport)', round(summa_sport/len(sport),3))

print('P(lyx)', round(summa_lyx/len(lyx),3))

print('P(budget)', round(summa_budget/len(budget),3))

print('P(familj)', round(summa_familj/len(familj),3))