#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np
import random


# # A. Plotting a Circle

# In[6]:


plt.figure(figsize=(5,5))

theta = np.linspace(0,2*np.pi,100)
x = 0.5 + 0.5*np.cos(theta)
y = 0.5 + 0.5*np.sin(theta)

plt.plot(x, y, color = "blue")
plt.xlim(0,1)
plt.ylim(0,1)
plt.show()


# # B. Creating a series of random points between 0,1 

# In[35]:


def pairs(n):
        c = 0 
        X = []
        Y = []
        while c<n:
            X.append(random.uniform(0,1))
            Y.append(random.uniform(0,1))
            c += 1
        return list(zip(X, Y))
          


#  # C. Testing if the random points are in the circle or not
#  

# In[31]:


r = 0.5
xi= 0.5
yi = 0.5 #Shift of our circle

def in_circle(x,y):
    return ((x-xi)**2)+ (y-yi)**2 < r**2 #If the distance from the random point and the circle's perimeter is greater than the radius then the point is not in the circle


# # D. Putting it all Together
# 
# The ratio of the area of the circle over the area of the square is:
# $$ \frac{\pi\times (0.5)^2}{1} = \frac{\pi}{4} \approx \frac{Number of Pointsin Circle}{Number of pairs generated}$$
# 
# $$\pi  \approx 4 \times \frac{NumberOfPairsInCircle}{TotalNumberOfPairsGenerated}$$
# 
# 

# In[32]:


def counting(n):
    z = pairs(n) #Creates n points 
    count = 0
    for i in z:
        x = i[0]
        y = i[1]
        count += in_circle(x,y)
        
    return "We found {} number of points out of {} random tries, resulting in a pi approximation of {}.".format(count, n,4*count/n)
        


# In[36]:


n = 50 
i_500 = counting(n)
print(i_500)


# In[37]:


n = 500
i_500 = counting(n)
print(i_500)


# In[38]:


n = 10000000
i_big = counting(n)
print(i_big)


# # Graph it, to Visualize it:

# In[41]:


plt.figure(figsize = (9,9))

x = 0.5 + 0.5 * np.cos(theta)
y = 0.5 + 0.5 * np.sin(theta)

n = [500, 10000, 50000, 100000]

for i in n:
    z = pairs(i)
    x1, y1 = [],[]
    for j in range(0, len(z)):
        x1.append(z[j][0])
        y1.append(z[j][1])
    plt.subplot(2, 2, (n.index(i)+1))
    plt.plot(x, y, color = 'red')
    plt.scatter(x1, y1)
    plt.plot()


# In[ ]:




