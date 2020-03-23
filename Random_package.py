
# coding: utf-8

# In[1]:


import numpy as np

np.random.seed()
position=[0]


for i in range(60):
    dice = np.random.randint(1, 7)
    step=position[-1]
    if dice<=2:
        step=max(step-1,0)
    elif dice>=3 and dice<=5:
        step=step+1
    else:
        step=step+np.random.randint(1,7)
    if np.random.rand()==0.001:
        step=0
    position.append(step)

    if np.random.rand()==0.001:  #To check the clumsiness of the user
        step=0
print(position)    #printing the position at each second
print("You are "+str(step)+" position away from the starting position")

