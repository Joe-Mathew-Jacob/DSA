#!/usr/bin/env python
# coding: utf-8

#  Read the dataset to python environment

# In[16]:


import pandas as pd
df=pd.read_excel("D:/DSA/iris.xls")
df


# Display the columns in the dataset.

# In[3]:


import pandas as pd
df=pd.read_excel("D:/DSA/iris.xls")
df.columns


# Calculate the mean of each column of the dataset

# In[8]:


import pandas as pd
df=pd.read_excel("D:/DSA/iris.xls")
df.mean()


# Check for the null values present in the dataset.

# In[9]:


import pandas as pd
df=pd.read_excel("D:/DSA/iris.xls")
df.info()


# In[5]:


df.isnull().sum()


# Perform meaningful visualizations using the dataset.

# In[56]:


import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("D:/DSA/iris.xls")
plt.xlabel("Classification")
plt.ylabel("SepaL Width")
plt.bar(df["Classification"],df["SW"])
plt.show()


# In[79]:


import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("D:/DSA/iris.xls")
plt.xlabel("SepaL Length")
plt.boxplot(df["SL"])
plt.show()


# In[58]:


import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("D:/DSA/iris.xls")
df1=df.groupby(["Classification"]).sum()
df1.plot.bar()


# In[ ]:





# In[ ]:




