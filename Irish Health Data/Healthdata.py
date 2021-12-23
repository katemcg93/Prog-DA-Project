import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

np.random.seed(seed = 1234)

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

genders = ["Male", "Female"]
gender = np.random.choice(a = genders, size = 7500, p = [0.5044340085, 0.4955659915])
unique, counts = np.unique(gender, return_counts = True)
print (np.asarray((unique, counts)).T)

# Age Data
# Mean age of Irish population is 37.48
# Plugged this into random normal distribution with estimated SD
# Excluded values under 15 as study did not include children
# Increasing size to account for fact that children will be removed from the array - will be left with 7500
ages_dist = np.random.normal(37.48, 17, size = 8269)
remove_kids = np.delete(ages_dist, np.where(ages_dist < 15))
print(remove_kids.size)
fig, ax = plt.subplots()
sns.histplot(remove_kids, kde = True)
ax.set_xlim(15,120)
plt.show()

#Affluence data
#For this survey - participants were divided into quintiles based on affluence/poverty level
#Equal chance that particpant would be in any of these categories

quintiles = ["Very Disadvantaged", "Disadvantaged", "Average", "Affluent", "Very Affluent"]
affluence_levels = np.random.choice(quintiles, 7500, p = [0.2, 0.2, 0.2, 0.2, 0.2])
unique, counts = np.unique(affluence_levels, return_counts = True)
print (np.asarray((unique, counts)).T)