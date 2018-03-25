
# coding: utf-8

# In[1]:


import pandas
import matplotlib
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from keras.models import Sequential
from keras.layers import Dense
import numpy
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from keras.constraints import nonneg


# In[2]:


names = ["Area","Date and Time","Day","Weather","Jam Factor"]
dataset = pandas.read_csv("trafficdata.csv",names=names,converters={"Area":int,"Date and Time":int,"Day":int,"Weather":int,"Jam Factor":float})
values = dataset.values


# In[152]:


numpy.random.seed(7)


# In[4]:


print(dataset.shape)


# In[5]:


print(dataset.head(20))


# In[6]:


dataset.plot(kind='box', subplots=True, sharex=False, sharey=False)
plt.show()


# In[7]:


print(dataset.describe())


# In[8]:


dataset.hist()
plt.show()


# In[9]:


# specify columns to plot
groups = [1, 3, 4]
i = 1
# plot each column
plt.figure()
for group in groups:
	plt.subplot(len(groups), 1, i)
	plt.plot(values[:, group])
	plt.title(dataset.columns[group], y=0.5, loc='right')
	i += 1
plt.show()


# In[10]:


array = dataset.values
X = array[:,0:4]
Y = array[:,4]


# In[153]:


# create model
model = Sequential()
model.add(Dense(12, input_dim=4, kernel_initializer='normal', activation='relu'))
model.add(Dense(8, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal'))


# In[154]:


#compile model
model.compile(loss='mse', optimizer='adam',metrics=['mae','mse'])


# In[155]:


model.fit(X, Y, epochs=40, batch_size=10)


# In[156]:


scores = model.evaluate(X,Y)


# In[157]:


print("Mean Absolute Error: %.2f%%\nMean Squared Error: %.2f%%" % (scores[1],scores[2]))


# In[164]:


#Making predictions
my_input = numpy.array([[1,1521466838,1,31],[3,1521466844,4,31]])
predictions = model.predict(X)
for i in predictions:
    if(numpy.floor(i)<4):
        print("Light Traffic")
    elif(numpy.floor(i)>=4):
        print("Medium Traffic")

