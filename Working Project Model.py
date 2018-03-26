
# coding: utf-8

# In[16]:


#Libraries
import time
import datetime
import pandas
from dateutil.parser import parse
import numpy as np
from numpy import array
from keras.models import Sequential
from keras.layers import Dense


# In[17]:


#Converting unix timestamp to date
reqtime = datetime.datetime.fromtimestamp(int("1521479617")).strftime('%Y-%m-%d %H:%M:%S')
print(reqtime)


# In[40]:


np.random.seed(7)


# In[35]:


#Converting hour to sin and cos
sin_hour = np.sin(dt.hour*(2.*np.pi/24))
cos_hour = np.cos(dt.hour*(2.*np.pi/24))
print(sin_hour)
print(cos_hour)


# In[18]:


#Getting the dataset
names = ["Area","Date and Time","Day","Weather","Jam Factor"]
dataset = pandas.read_csv("trafficdata.csv",names=names)


# In[19]:


#Defining functions for parsing month,date,hour and minute
def parse_month(given_date):
    reqtime = datetime.datetime.fromtimestamp(int(given_date)).strftime('%Y-%m-%d %H:%M:%S')
    dt = parse(reqtime)
    return dt.month
def parse_date(given_date):
    reqtime = datetime.datetime.fromtimestamp(int(given_date)).strftime('%Y-%m-%d %H:%M:%S')
    dt = parse(reqtime)
    return dt.day
def parse_hour(given_date):
    reqtime = datetime.datetime.fromtimestamp(int(given_date)).strftime('%Y-%m-%d %H:%M:%S')
    dt = parse(reqtime)
    return dt.hour
def parse_minute(given_date):
    reqtime = datetime.datetime.fromtimestamp(int(given_date)).strftime('%Y-%m-%d %H:%M:%S')
    dt = parse(reqtime)
    return dt.minute


# In[20]:


dataset["Month"] = dataset["Date and Time"].apply(parse_month)
dataset["Date"] = dataset["Date and Time"].apply(parse_date)
dataset["Hour"] = dataset["Date and Time"].apply(parse_hour)
dataset["Minute"] = dataset["Date and Time"].apply(parse_minute)


# In[21]:


print(dataset.head(10))


# In[22]:


cols = list(dataset.columns.values)
print(cols)


# In[23]:


cols = ["Area","Month","Date","Hour","Minute","Date and Time","Day","Weather","Jam Factor"]
dataset = dataset[cols]


# In[24]:


print(dataset.head(10))


# In[25]:


#Deleting column
del dataset["Date and Time"]


# In[30]:


#Print dataset
print(dataset.head(10))


# In[49]:


#Using the model on this data
array = dataset.values
X = array[:,0:7]
Y = array[:,7]
print(X)


# In[41]:


# create model
model = Sequential()
model.add(Dense(12, input_dim=7, kernel_initializer='normal', activation='relu'))
model.add(Dense(4, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal'))


# In[42]:


#compile model
model.compile(loss='mse', optimizer='adam',metrics=['mae','mse'])


# In[43]:


#Train the model
model.fit(X, Y, epochs=50, batch_size=10)


# In[44]:


#Evaluate the model
scores = model.evaluate(X,Y)


# In[45]:


#Printing Error values
print("Mean Absolute Error: %.2f%%\nMean Squared Error: %.2f%%" % (scores[1],scores[2]))


# In[53]:


#Making predictions
my_input = np.array([[2,3,26,14,45,1,34]])
predictions = model.predict(my_input)
for i in predictions:
    print(i)

