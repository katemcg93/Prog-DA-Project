import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#This programme is to simulate health indicators in the Irish population
#This survey is conducated yearly on participants aged 15 and older, intended as a representative sample of Irish population
#Demographic data gathered includes age, gender, employment status and education level

#First section - age data
#Got
ages_dist = np.random.normal(37.48, 22, size = 7500)
remove_kids = np.delete(ages_dist, np.where(ages_dist < 15))
fig, ax = plt.subplots()
sns.histplot(remove_kids, kde = True)
ax.set_xlim(15,120)
plt.show()
