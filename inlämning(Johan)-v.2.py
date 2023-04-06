#!/usr/bin/env python
# coding: utf-8

# **Inlämningsuppgift - Del 1 (Johan)**
# 
# Data: E-commerce Transaction Data (fil: Sales Transaction v.4a)

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


ecom_df = pd.read_csv('Sales_Transaction.csv')
#ecom_df.head(-5)


# In[3]:


ecom_df = ecom_df.sample(frac = 0.10, random_state=0)


# In[4]:


ecom_df.info()


# In[5]:


ecom_df.describe()


# In[6]:


ecom_df.corr()


# In[7]:


ecom_df['Date'].sort_values()


# In[8]:


#Vi tar fram en boxplot för att få en överblick över outliers
data = ecom_df['Quantity']

fig1, ax1 = plt.subplots()
ax1.set_title('Boxplot innan data cleaning')
ax1.boxplot(data)


# In[9]:


mask1 = ecom_df['Quantity'] >= 1


# In[10]:


ecom_df = ecom_df[mask1]

ecom_df


# In[11]:


#filtrera ut värden i den översta kvantilen och skapar en ny DataFrame utan dessa "outliers"
q_limit  = ecom_df["Quantity"].quantile(0.99)

ecom_df = ecom_df.loc[(ecom_df["Quantity"] < q_limit),]
print("q_limit = ", q_limit)


# In[12]:


data = ecom_df['Quantity']

fig1, ax1 = plt.subplots()
ax1.set_title('Boxplot efter data cleaning')
ax1.boxplot(data)


# In[13]:


#ecom_df.loc['Real_date'] = pd.to_datetime(ecom_df["Date"]) #LOOK INTO THIS !!!
ecom_df['Real_date'] = pd.to_datetime(ecom_df["Date"])


# In[14]:


#skapa day
#skapa week
ecom_df['Day'] = pd.DatetimeIndex(ecom_df['Date']).day
ecom_df['Week'] = pd.DatetimeIndex(ecom_df['Date']).week
ecom_df['Month'] = pd.DatetimeIndex(ecom_df['Date']).month

#ecom_df['Day'] = ecom_df['Real_date'].dt.day
#ecom_df['Week'] = ecom_df['Real_date'].dt.week
#ecom_df['Month'] = ecom_df['Real_date'].dt.month


# In[15]:


ecom_df['Week_cat'] = pd.Categorical(ecom_df['Week'], ordered=True)
ecom_df['Month_cat'] = pd.Categorical(ecom_df['Month'], ordered=True)


# In[16]:


#Tar bort onödiga kolumner

ecom_df.drop(["TransactionNo", "Date", "ProductNo", "CustomerNo"], axis=1, inplace=True)


# In[17]:


ecom_df


# **Måste "one-hot-encoda" kategorivariabler för att kunna använda kategorivariabler**

# In[18]:


ecom_df = pd.get_dummies(ecom_df, columns=["ProductName", "Country"])


# In[19]:


ecom_df.info()


# In[20]:


clean_df = ecom_df


# In[21]:


#Nu har vi en korrekt DataFrame som heter clean_df som innehåller endast transaktioner med positiv Quantity, korrekta datumkolumner och one-hot-encodade kolumner.
clean_df


# In[22]:


data = clean_df['Quantity']

fig1, ax1 = plt.subplots()
ax1.set_title('Boxplot efter data cleaning')
ax1.boxplot(data)


# Nu är vi klara med vår dataformatering och datatvätt. Nu är det dags för linjär regression!

# In[23]:


#X = clean_df.loc[:, ~clean_df.columns.isin(['Quantity', 'Real_date'])]
X = clean_df.loc[:,['Price','Day','Week_cat','Month_cat']]
y = clean_df.Quantity


# In[24]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# **OBS, kör de nedanstående cellerna en gång innan RFECV cellerna körs**

# In[33]:


#RFECV för LINJÄR REGRESSION (LinearRegression)
from sklearn.feature_selection import RFECV

selector = RFECV(LinearRegression(), step=1, cv=5, scoring='r2', verbose=3)

selector.fit(X_train, y_train)

selector.get_feature_names_out()
selector.cv_results_


# In[34]:


#RFECV för DECISION TREE (DecisionTreeRegressor)
from sklearn.feature_selection import RFECV

selector = RFECV(DecisionTreeRegressor(), step=1, cv=5, scoring='r2', verbose=3)

selector.fit(X_train, y_train)

print(selector.get_feature_names_out())
print(selector.cv_results_)


# In[27]:


from sklearn.linear_model import LinearRegression
linreg_model = LinearRegression()

linreg_model = linreg_model.fit(X = X_train, y = y_train)
print('Coefficients: \n', linreg_model.coef_)


# In[28]:


#kolla intercept
linreg_model.intercept_


# In[29]:


#genomsnitt för kvantitet
clean_df['Quantity'].mean()


# In[30]:


y_test_pred = linreg_model.predict(X_test)


# In[31]:


#Hur väl fungerar vår modell?

from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt

#mean squared error
mse = mean_squared_error(y_test, y_test_pred)
print('Mean squared error:', round(mse, 2))

#root mean squared error
rmse = sqrt(mse)
print('Root mean squared error:', round(rmse, 2))

#coefficient of determination: 1 is perfect regression
r2 = r2_score(y_test, y_test_pred)
print('Coefficient of determination:', round(r2, 2))


# **Testar att använda ett beslutsträd istället**

# In[36]:


from sklearn.tree import DecisionTreeRegressor
tree_reg_model = DecisionTreeRegressor()

#För att bara testa 'Price' sätt in detta efter X_train och X_test: ['Price'].values.reshape(-1, 1)

tree_reg_model = tree_reg_model.fit(X=X_train['Price'].values.reshape(-1, 1), y=y_train)
print('Modellens djup:', tree_reg_model.get_depth())

y_test_pred_tree = tree_reg_model.predict(X_test['Price'].values.reshape(-1, 1))

# Dags att utvärdera vår modell!!!

from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt

#mean squared error
mse = mean_squared_error(y_test, y_test_pred_tree)
print('Mean squared error:', round(mse, 2))

#root mean squared error
rmse = sqrt(mse)
print('Root mean squared error:', round(rmse, 2))

#coefficient of determination: 1 is perfect regression
r2_tree = r2_score(y_test, y_test_pred_tree)
print('Coefficient of determination:', round(r2_tree, 2))


# In[ ]:




