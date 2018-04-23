
# coding: utf-8

# In[ ]:


#Libraries
import time
import datetime
import pandas
from dateutil.parser import parse
import numpy as np
from numpy import array
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ipywidgets as widgets


# In[ ]:


#Converting unix timestamp to date
reqtime = datetime.datetime.fromtimestamp(int("1521479617")).strftime('%Y-%m-%d %H:%M:%S')
print(reqtime)


# In[ ]:


np.random.seed(7)


# In[ ]:


#Getting the dataset
names = ["Area","Date and Time","Day","Weather","Jam Factor"]
dataset = pandas.read_csv("newtrafficdata.csv",names=names)


# In[ ]:


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


# In[ ]:


dataset["Month"] = dataset["Date and Time"].apply(parse_month)
dataset["Date"] = dataset["Date and Time"].apply(parse_date)
dataset["Hour"] = dataset["Date and Time"].apply(parse_hour)
dataset["Minute"] = dataset["Date and Time"].apply(parse_minute)


# In[ ]:


print(dataset.head(10))


# In[ ]:


cols = list(dataset.columns.values)
print(cols)


# In[ ]:


cols = ["Area","Month","Date","Hour","Minute","Date and Time","Day","Weather","Jam Factor"]
dataset = dataset[cols]


# In[ ]:


print(dataset.head(10))


# In[ ]:


#Deleting column
del dataset["Date and Time"]


# In[ ]:


#Print dataset
print(dataset.head(10))


# In[ ]:


#Using the model on this data
array = dataset.values
X = array[:,0:7]
Y = array[:,7]
print(X)


# In[ ]:


# create model
model = Sequential()
model.add(Dense(12, input_dim=7, kernel_initializer='normal', activation='relu'))
model.add(Dense(8, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal'))


# In[ ]:


#compile model
model.compile(loss='mse', optimizer='adam',metrics=['mae'])


# In[ ]:


#Train the model
model.fit(X, Y, epochs=50, batch_size=10)


# In[ ]:


#Evaluate the model
scores = model.evaluate(X,Y)


# In[ ]:


#Printing Error values
print("Mean Absolute Error: %f" % (scores[1]))


# In[ ]:


#Making predictions
predictions = model.predict(X)
for i,j in zip(predictions,Y):
    print(i,j)


# In[ ]:


#Plotting the data for month, date and jam factor
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X1 = X[:,1]
X2 = X[:,2]
scatter1 = ax.scatter3D(X1, X2, Y)
scatter2 = ax.scatter3D(X1,X2,predictions)
ax.set_xlabel('Month')
ax.set_ylabel('Date')
ax.set_zlabel('Jam Factor')
ax.legend([scatter1,scatter2],['observed value','predicted value'])
plt.show()


# In[ ]:


#Plotting the data for hour, minute and jam factor
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X3 = X[:,3]
X4 = X[:,4]
scatter1 = ax.scatter3D(X3, X4, Y)
scatter2 = ax.scatter3D(X3,X4,predictions)
ax.set_xlabel('Hour')
ax.set_ylabel('Minute')
ax.set_zlabel('Jam Factor')
ax.legend([scatter1,scatter2],['observed value','predicted value'])
plt.show()


# In[ ]:


#Creating area widget
area = {"NH45":1,"Anna Salai":2,"Arcot Road":3}
areaWidget = widgets.Dropdown(
    options=area,
    value=None,
    description='Area:',
)


# In[ ]:


#Creating month widget
month = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
monthWidget = widgets.Dropdown(
    options=month,
    value=None,
    description='Month:',
)


# In[ ]:


#Creating date widget
date = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
dateWidget = widgets.Dropdown(
    options=date,
    value=None,
    description='Date:',
)


# In[ ]:


#Creating hour widget
hour = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
hourWidget = widgets.Dropdown(
    options=hour,
    value=None,
    description='Hour:',
)


# In[ ]:


#Creating minute widget
minute = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]
minuteWidget = widgets.Dropdown(
    options=minute,
    value=None,
    description='Minute:',
)


# In[ ]:


#Creating day widget
day = {"Sunday":0,"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6}
dayWidget = widgets.Dropdown(
    options=day,
    value=None,
    description='Day:',
)


# In[ ]:


#Getting user input
display(areaWidget)
display(monthWidget)
display(dateWidget)
display(hourWidget)
display(minuteWidget)
display(dayWidget)


# In[ ]:


#Getting values
areaValue = areaWidget.value
monthValue = monthWidget.value
dateValue = dateWidget.value
hourValue = hourWidget.value
minuteValue = minuteWidget.value
dayValue = dayWidget.value
weatherValue = 31


# In[ ]:


#Making prediction on user input
user_input = np.array([[areaValue,monthValue,dateValue,hourValue,minuteValue,dayValue,weatherValue]])
user_prediction = model.predict(user_input)


# In[ ]:


#Deciding level of traffic
jamFactor = float(user_prediction)
if(np.round(jamFactor)<4):
    traffic = "Light"
elif(np.round(jamFactor)>=4 and np.round(jamFactor)<7):
    traffic = "Medium"
elif(np.round(jamFactor)>=7):
    traffic = "Heavy"


# In[ ]:


#Getting results
for areaName, area in area.items():    
    if area == areaValue:
        areaResult = areaName

for monthName, month in month.items():  
    if month == monthValue:
        monthResult = monthName
        
for dayName, day in day.items():    
    if day == dayValue:
        dayResult = dayName


# In[ ]:


#Printing the result
print("The jam factor is "+str(jamFactor)+". "+traffic+" traffic is predicted at "+areaResult+" on "+monthResult+" "+str(dateValue)+" at "+str(hourValue)+":"+str(minuteValue)+", "+dayResult+".")

