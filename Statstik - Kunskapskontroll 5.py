#Uppg. 5

import pandas as pd
import numpy as np
import scipy.stats as st

data = pd.read_csv('inlämning ihm.csv', sep= ";")

#Kod på rad 11 och 12 plockar data från kolumnen "Type of Commercial" och skapar en lista med data från kolumnen så att vi kan använda den i följande uppgifter.

type = data['Type of Commercial']
lista_time = data['Time on Website (Min)']

sidebar = data[type == 'Sidebarreklam']['Time on Website (Min)']
popup = data[type =='Popuppreklam med musik']['Time on Website (Min)']

sidebar = list(sidebar)
popup = list(popup)

print(st.ttest_ind(sidebar,popup,equal_var='False',alternative='greater'))

print('Medelvärdet för tid på sidan (sidebar) = ',np.mean(sidebar))
print('Medelvärdet för tid på sidan (popup) = ',np.mean(popup))