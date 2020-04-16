#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import os
import numpy as np
import random
import seaborn as sb


# ## Loading The Directory##

# In[2]:


os.chdir(r"C:\Users\satya\Downloads\Compressed")


# Reading the csv File

# In[3]:


data = pd.read_csv("attrition.csv")


# In[4]:


data.head()


# In[5]:


population = data['Attrition'] # loading the column values in a new list named population so that its category can be changed into numerical values


# In[6]:


import matplotlib.pyplot as plt # loading library for graphs / visulaisations


# Converting the categorical values into numerical values

# In[7]:


population = data['Attrition'].astype('category')
population.dtypes 


# In[8]:


population = population.cat.codes
population.head()


# In[9]:


population.dtype


# In[10]:


plt.hist(population) # here we can see that our population data is binomially distributed


# In[11]:


P_mean = population.mean()
P_std = population.std()
print('population mean = ',P_mean.round(4) , 'population standard deviation =',P_std.round(4))


# # Generating 1000 samples of different size

# In[16]:


samples_10 = [np.mean(random.choices(population,k=10)) for _ in range(1000)]

sb.distplot(samples_10, hist=True)
plt.show()


# In[17]:


samples_20 = [np.mean(random.choices(population,k=20)) for _ in range(1000)]


sb.distplot(samples_20, hist=True)
plt.show()


# In[18]:


samples_30 = [np.mean(random.choices(population,k=30)) for _ in range(1000)]
sb.distplot(samples_30, hist=True)
plt.show()


# In[19]:


samples_40 = [np.mean(random.choices(population,k=40)) for _ in range(1000)]
sb.distplot(samples_40, hist = True)
plt.show()


# In[20]:


samples_100 = [np.mean(random.choices(population,k=100)) for _ in range(1000)]
sb.distplot(samples_100,hist = True)


# In[21]:


samples_300 = [np.mean(random.choices(population,k=300)) for _ in range(1000)]
sb.distplot(samples_300,hist = True)


# In[22]:


samples_400 = [np.mean(random.choices(population,k=400)) for _ in range(1000)]
sb.distplot(samples_400, hist = True)


# In[23]:


samples_500 = [np.mean(random.choices(population,k=500)) for _ in range(1000)]
sb.distplot(samples_500, hist = True)


# In[24]:


samples_1000 = [np.mean(random.choices(population,k=1000)) for _ in range(1000)]
sb.distplot(samples_1000, hist = True)


# In[41]:


samples_10 = np.array(samples_10)
samples_20 = np.array(samples_20)
samples_30 = np.array(samples_30)
samples_40 = np.array(samples_40)
samples_400 = np.array(samples_400)
samples_500 = np.array(samples_500)
samples_1000 = np.array(samples_1000)


# In[42]:


S_10_mean = samples_10.mean()
S_10_std = samples_10.std()
S_20_mean = samples_20.mean()
S_20_std = samples_20.std()
S_30_mean = samples_30.mean()
S_30_std = samples_30.std()
S_40_mean = samples_40.mean()
S_40_std = samples_40.std()
S_400_mean = samples_400.mean()
S_400_std = samples_400.std()
S_500_mean = samples_500.mean()
S_500_std = samples_500.std()
S_1000_mean = samples_1000.mean()
S_1000_std = samples_1000.std()


# In[46]:


P_mean = population.mean()
P_std = population.std()
print('population mean = ',P_mean.round(4) , 'population standard deviation =',P_std.round(4) ,"\n" ,
      'sample mean with no. of sample @10 = ',S_10_mean.round(4) , 'sample standard deviation =',S_10_std.round(4) ,"\n" ,
     'sample mean with no. of sample @20 =  ',S_20_mean.round(4) , 'sample standard deviation =',S_20_std.round(4) ,"\n" ,
     'sample mean with no. of sample @30 =  ',S_30_mean.round(4) , 'sample standard deviation =',S_30_std.round(4) ,"\n" ,
     'sample mean with no. of sample @40 =  ',S_40_mean.round(4) , 'sample standard deviation =',S_40_std.round(4) ,"\n" ,
     'sample mean with no. of sample @400 =  ',S_400_mean.round(4) , 'sample standard deviation =',S_400_std.round(4) ,"\n" ,
      'sample mean with no. of sample @500 =  ',S_500_mean.round(4) , 'sample standard deviation =',S_500_std.round(4) ,"\n" ,
      'sample mean with no. of sample @1000 =  ',S_1000_mean.round(4) , 'sample standard deviation =',S_1000_std.round(4))
      
      


# In[ ]:




