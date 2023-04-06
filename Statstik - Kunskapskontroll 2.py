#Kunskapskontroll uppg. 2

import pandas as pd
import numpy as np
import statistics
import scipy.stats as st
import matplotlib.pyplot as plt

data = pd.read_csv('inlämning ihm.csv', sep= ";")

#Kod på rad 11 och 12 plockar data från kolumnen "Time on Website (Min)" och skapar en lista med data från kolumnen så att vi kan använda den i följande uppgifter.
time_on_website = data.loc[:,'Time on Website (Min)']
time_on_website = list(time_on_website)

#a)
medel = np.mean(time_on_website)
print('a): medelvärdet = ', round(medel,2))

#b)
s = np.std(time_on_website, ddof=1)
print('b): standardavvikelsen = ', round(s,2))

#c)

n = time_on_website

plt.hist(n, bins=20)
plt.title("Histogram")
#plt.show()
#Jag kommenterar bort rad 29 för att slippa att grafen ritas ut varje gång jag laddar programmet

#d)
medelfel = st.sem(time_on_website)
frihetsgrader = len(time_on_website)-1
t = st.t.ppf(q=0.95, df=frihetsgrader)
gräns= medel + (t*medelfel)

print('d): Gränsen för det ensidigt uppåt begränsade 95%-konfidensintervallet för tid spenderat på webbsidan = ', round(gräns,2))

#e)
median = np.median(time_on_website)
print('e): medianen = ', median)

#f)
#loopa igenom och summera alla värden mellan medianens värde och q3.
time_on_website.sort()

q3 = np.percentile(time_on_website, 75)

summa = 0
for x in time_on_website:
  if x > median and x < q3:
    summa += x
print('f): Summan av den totala tiden spenderad på hemsidan för tider mellan median och q3 = ', round(summa,2))

#g)
kön = data.loc[:,'Gender']

kön = list(kön)

antal_män = kön.count('Man')
antal_kvinnor = kön.count('Kvinna')

x1 = ['Män']
x2 = ['Kvinnor']
y1 = [antal_män]
y2 = [antal_kvinnor]

plt.bar(x1,y1, color = 'b', edgecolor='black')
plt.bar(x2,y2, color = '#8A2BE2', edgecolor='black')
#plt.show()
#Jag kommenterar bort rad 71 för att graden ritas ut varje gång jag laddar programmet.

#h)

k = 8
n = 20
p = antal_kvinnor/(antal_män + antal_kvinnor)

sannolikhet = st.binom.pmf(k,n,p)
print('h): Sannolikheten = ',sannolikhet)

#i)
land = data.loc[:,'Country']

land = list(land)

print('i): Det vanligaste landet är typvärdet = ', statistics.mode(land))