import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#This programme is to simulate health indicators in the Irish population
#This survey is conducated yearly on participants aged 15 and older, intended as a representative sample of Irish population
#Demographic data gathered includes age, gender, employment status and education level

#Gender

total_pop = pd.read_csv('Population by Gender 2016.csv')
print(total_pop.columns)
total_pop = total_pop.rename(columns = {"VALUE": "Population"})
whole_country = total_pop.loc[total_pop['Regional Authority'] == 'State']
male_pop = whole_country.loc[whole_country["Sex"] == "Male"]
female_pop = whole_country.loc[whole_country["Sex"] == "Female"]
percentage_females = female_pop["Population"].values/(female_pop["Population"].values + male_pop["Population"].values) * 100
percentage_males = 100 - percentage_females
print("Total percentage of female Irish population : {}".format(percentage_females))
print("Total percentage of Irish male population : {}".format(percentage_males))

# Age Data
# Mean age of Irish population is 37.48
# Plugged this into random normal distribution with estimated SD
# Excluded values under 15 as study did not include children
ages_dist = np.random.normal(37.48, 20, size = 7500)
remove_kids = np.delete(ages_dist, np.where(ages_dist < 15))
fig, ax = plt.subplots()
sns.histplot(remove_kids, kde = True)
ax.set_xlim(15,120)
plt.show()


