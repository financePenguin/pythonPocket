#Uppg. 4

import pandas as pd
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'sklearn'])
from sklearn.linear_model import LinearRegression
import numpy as np
data = pd.read_csv('inlämning ihm.csv', sep= ";")

#listor med tid på sidan och antalet köpta items
lista_time = data.loc[:,'Time on Website (Min)']
lista_time = list(lista_time)
nr_items = data.loc[:,'Items Bought on Website']
nr_items = list(nr_items)

#konverterar till vektorer
x = np.array(lista_time)
y = np.array(nr_items)
#beräkna och printa r-värdet som finns högst till höger
r_value=np.corrcoef(x,y)
print(r_value)

#konvertera x till en kolumn
x = np.array(lista_time).reshape((-1, 1))
#vi utför linjär regression
model = LinearRegression().fit(x, y)


#printar lutningen (k-värdet)
print('Lutningen =',model.coef_)
#printar skärning m y-axel
print('Skärning m av y-axeln =',model.intercept_)
#printar r^2-värdet (förklaringsgrad)
print('Förklaringsgraden =',model.score(x, y))

#c)Prediktion

m = 9 #Antal_minuter

#Formel för att beräkna prediktion
pred = m*0.07997728+0.6341914358430332

print('Besökaren kommer köpa ',round(pred,2), ' stycken produkter.')