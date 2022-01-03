from os import remove
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from scipy.stats.morestats import yeojohnson
import seaborn as sns
import pandas as pd
from scipy import stats
from scipy.stats import skewnorm
from scipy.stats import gamma
from scipy.stats import expon
from scipy.stats import truncnorm

np.random.seed(seed = 1234)

#This programme is to simulate health indicators in the Irish population
#This survey is conducated yearly on participants aged 15 and older, intended as a representative sample of Irish population
#Demographic data gathered includes age, gender, employment status and education level

#Gender

age_dist = truncnorm.rvs(a = 15, b = 100, loc = 37.4, scale = 20, size = 7500)

total_pop = pd.read_csv('Population by Gender 2016.csv')
print(total_pop.columns)
total_pop = total_pop.rename(columns = {"VALUE": "Population"})
whole_country = total_pop.loc[total_pop['Regional Authority'] == 'State']
male_pop = whole_country.loc[whole_country["Sex"] == "Male"]
female_pop = whole_country.loc[whole_country["Sex"] == "Female"]
percentage_females = female_pop["Population"].values/(female_pop["Population"].values + male_pop["Population"].values) * 100
percentage_males = 100 - percentage_females
print("Total percentage of female Irish population : {}".format(percentage_females))
print("Total percentage of Irish male population  : {}".format(percentage_males))

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
plt.close()

#Affluence data
#For this survey - participants were divided into quintiles based on affluence/poverty level
#Equal chance that particpant would be in any of these categories

quintiles = ["Very Disadvantaged", "Disadvantaged", "Average", "Affluent", "Very Affluent"]
affluence_levels = np.random.choice(quintiles, 7500, p = [0.2, 0.2, 0.2, 0.2, 0.2])
unique, counts = np.unique(affluence_levels, return_counts = True)
sns.barplot(x = unique, y = counts)
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()
plt.close()


demographic_dataset = pd.DataFrame({"Gender": gender, "Age": remove_kids, "Socioeconomic Status": affluence_levels})
demographic_dataset.to_csv("dataset.csv")

#Unemployment Data
#Taking figures from mid-2019 to reflect time that Healthy Ireland Survey was done

monthly_unemployment = pd.read_csv('Monthly Unemployment Figures 06 21.csv')
monthly_unemployment = monthly_unemployment[["Age Group", "Sex", "VALUE"]]

age_order = ["15-24", "25-34", "35-44", "45-54", "55-64", "65-74", "75+"]
bmi_order = ["Underweight", "Healthy Weight", "Overweight", "Obese"]

age_group = []

def age_categories (row) :
    if row["Age"] <= 24:
        age_classification = "15-24"
    elif row["Age"] > 24 and row["Age"] <=34:
        age_classification = "25-34"
    elif row["Age"] > 34 and row["Age"] <=44:
        age_classification = "35-44"
    elif row["Age"] > 44 and row["Age"] <=54:
        age_classification = "45-54"
    elif row["Age"] > 54 and row["Age"] <=64:
        age_classification = "55-64"
    elif row["Age"] > 64 and row["Age"] <=74:
        age_classification = "65-74"
    else:
        age_classification = "75+"

    age_group.append(age_classification)

    return(age_classification)

demographic_dataset["Age Category"] = demographic_dataset.apply(age_categories, axis = 1)
demographic_dataset.to_csv("dataset.csv")


employment_choices = ["Employed", "Unemployed", "Not in Labour Force"]

def in_employment (row):
    if row["Gender"] == "Male":
        if row["Age"] <20:
            return np.random.choice(a = employment_choices, p =[0.33, 0.12, 0.55])
        elif row["Age"] >= 20 and row["Age"] < 25:
            return np.random.choice(a = employment_choices, p =[0.68, 0.12, 0.20])
        elif row["Age"] >= 25  and row["Age"] < 35:
            return np.random.choice(a = employment_choices, p =[0.84, 0.07, 0.08])
        elif row["Age"] >= 35  and row["Age"] < 45:
            return np.random.choice(a = employment_choices, p =[0.9, 0.03, 0.07])
        elif row["Age"] >= 45  and row["Age"] < 55:
            return np.random.choice(a = employment_choices, p =[0.85, 0.04, 0.11])
        elif row["Age"] >= 55  and row["Age"] < 59:
            return np.random.choice(a = employment_choices, p =[0.79, 0.04, 0.17])
        elif row["Age"] >= 59  and row["Age"] < 64:
            return np.random.choice(a = employment_choices, p =[0.58, 0.04, 0.38])
        elif row["Age"] >= 59  and row["Age"] < 64:
            return np.random.choice(a = employment_choices, p =[0.2, 0.01, 0.89])
        else:
            return np.random.choice(a = employment_choices, p =[0, 0.06, 0.94])
    else:
        if row["Age"] <20:
            return np.random.choice(a = employment_choices, p =[0.33, 0.16, 0.61])
        elif row["Age"] >= 20 and row["Age"] < 25:
            return np.random.choice(a = employment_choices, p =[0.68, 0.09, 0.25])
        elif row["Age"] >= 25  and row["Age"] < 35:
            return np.random.choice(a = employment_choices, p =[0.77, 0.05, 0.18])
        elif row["Age"] >= 35  and row["Age"] < 45:
            return np.random.choice(a = employment_choices, p =[0.77, 0.05, 0.18])
        elif row["Age"] >= 45  and row["Age"] < 55:
            return np.random.choice(a = employment_choices, p =[0.74, 0.04, 0.12])
        elif row["Age"] >= 55  and row["Age"] < 59:
            return np.random.choice(a = employment_choices, p =[0.67, 0.04, 0.29])
        elif row["Age"] >= 59  and row["Age"] < 64:
            return np.random.choice(a = employment_choices, p =[0.58, 0.04, 0.38])
        elif row["Age"] >= 59  and row["Age"] < 64:
            return np.random.choice(a = employment_choices, p =[0.2, 0.01, 0.89])
        else:
            return np.random.choice(a = employment_choices, p =[0, 0.06, 0.94])



        
demographic_dataset["Employment Status"] = demographic_dataset.apply(in_employment, axis = 1)
sns.countplot(x = "Employment Status", hue = "Age Category", data = demographic_dataset, hue_order= age_order)
plt.show()
plt.close()
demographic_dataset.to_csv("dataset.csv")



def bmi_assign (row):
    if row ["Gender"] == "Male":
        if row["Age"] <= 24:
            if row["Socioeconomic Status"].isin ("Disadvantaged, Very Disadvantaged"):
                return skewnorm.rvs(a = 2, loc = 25, scale = 5, size = 1)
            else:
                return skewnorm.rvs(a = 2, loc = 20, scale = 5, size = 1)
        elif row["Age"] > 24 and row["Age"] <= 34:
            return skewnorm.rvs(a = 2, loc = 23, scale = 3, size = 1)
        elif row["Age"] > 34 and row["Age"] <= 44:
            return skewnorm.rvs(a = 2, loc = 23, scale = 5, size = 1)
        elif row["Age"] > 44 and row["Age"] <= 54:
            return skewnorm.rvs(a = 2, loc = 25, scale = 5, size = 1)
        elif row["Age"] > 54 and row["Age"] <= 64:
            return skewnorm.rvs(a = 3, loc = 26, scale = 5, size = 1)
        elif row["Age"] > 64 and row["Age"] <= 74:
            return skewnorm.rvs(a = 3, loc = 27, scale = 5, size = 1)
        else:
            return skewnorm.rvs(a = 4, loc = 27, scale = 5, size = 1)

demographic_dataset["BMI"] = demographic_dataset.apply(bmi_assign, axis = 1)

bmi_values = []
bmi_classification = []
for value in demographic_dataset["BMI"].values:
    bmi_values.append(value.item())
    if value.item() < 18.5:
        classification = "Underweight"
    elif value.item() >= 18.5 and value.item () < 25:
        classification = "Healthy Weight"
    elif value.item() >= 25 and value.item () < 30:
        classification = "Overweight"
    else:
        classification = "Obese"
    bmi_classification.append(classification)

demographic_dataset["BMI"] = bmi_values
demographic_dataset["BMI Classification"] = bmi_classification

demographic_dataset.to_csv("dataset.csv")

sns.histplot(bmi_values)
plt.show()
plt.close()

sns.countplot(x = "Age Category", hue = "BMI Classification", order = age_order, hue_order=bmi_order, data = demographic_dataset)
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()
plt.close()

meeting_ex_guidelines = ["Yes", "No", "No Exercise"]


test_exercise = skewnorm.rvs(a = 5, loc = 170, scale = 10, size = 7500)
sns.histplot(test_exercise)
plt.show()
plt.close()

def mins_exercise(row):
        if row["Gender"] == 'Male':
            if row["Age"] <= 24:
                if row["BMI Classification"] == "Obese":
                     return skewnorm.rvs(a = 0, loc = 120, scale = 40, size = 1)
                else:
                    return skewnorm.rvs(a = 1, loc = 150, scale = 40, size = 1)
            elif row["Age"] > 24 and row["Age"] <= 44:
                if row["BMI Classification"] == "Obese":
                    return skewnorm.rvs(a = 0, loc = 110, scale = 40, size = 1)
                else:
                    return skewnorm.rvs(a = 1, loc = 140, scale = 40, size = 1)
            elif row["Age"] > 44 and row["Age"] <= 54:
                return skewnorm.rvs(a = 0, loc = 130, scale = 40, size = 1)
            elif row["Age"] > 54 and row["Age"] <= 64:
                return skewnorm.rvs(a = 0, loc = 120, scale = 40, size = 1)
            elif row["Age"] > 64 and row["Age"] <= 74:
                return skewnorm.rvs(a = -1, loc = 100, scale = 40, size = 1)
            elif row["Age"] > 74:
                return skewnorm.rvs(a = -1, loc = 80, scale = 40, size = 1)

        else:
            if row["Age"] <= 24:
                    if row["BMI Classification"] == "Obese":
                     return skewnorm.rvs(a = 0, loc = 120, scale = 40, size = 1)
                    else:
                     return skewnorm.rvs(a = 1, loc = 140, scale = 40, size = 1)
            elif row["Age"] > 24 and row["Age"] <= 44:
                    if row["BMI Classification"] == "Obese":
                     return skewnorm.rvs(a = 0, loc = 100, scale = 40, size = 1)
                    else:
                     return skewnorm.rvs(a = 1, loc = 130, scale = 40, size = 1)
            elif row["Age"] > 44 and row["Age"] <= 54:
                return skewnorm.rvs(a = 0, loc = 120, scale = 40, size = 1)
            elif row["Age"] > 54 and row["Age"] <= 64:
                return skewnorm.rvs(a = -1, loc = 100, scale = 40, size = 1)
            elif row["Age"] > 64 and row["Age"] <= 74:
                  return skewnorm.rvs(a = -1, loc = 90, scale = 40, size = 1)
            elif row["Age"] > 74:
                return skewnorm.rvs(a = -1, loc = 80, scale = 40, size = 1)

demographic_dataset["Minutes Exercise per Week"] = demographic_dataset.apply(mins_exercise, axis = 1)
demographic_dataset.to_csv("dataset.csv")

minutes_exercise = []
meeting_guidelines = []
for value in demographic_dataset["Minutes Exercise per Week"].values:
    minutes_exercise.append(value.item())
    if value.item ()  > 150:
        is_meeting = "Yes"
    else:
        is_meeting = "No"
    meeting_guidelines.append(is_meeting)

demographic_dataset["Minutes Exercise per Week"] = minutes_exercise
demographic_dataset["Meeting Exercise Guidelines"] = meeting_guidelines

demographic_dataset.to_csv("dataset.csv")

alcohol_choices = ["Drinks Alcohol", "Does Not Drink Alcohol"]

sns.histplot()

sns.countplot(x = "Meeting Exercise Guidelines", data = demographic_dataset, hue = "Age Category", hue_order = age_order)
plt.show()
plt.close()

def drinks_alcohol(row):
    if row["Socioeconomic Status"] == "Very Disadvantaged":
        return np.random.choice(alcohol_choices, p = [0.71, 0.29])
    elif row["Socioeconomic Status"] == "Disadvantaged":
        return np.random.choice(alcohol_choices, p = [0.72, 0.28])
    elif row["Socioeconomic Status"] == "Average":
        return np.random.choice(alcohol_choices, p = [0.76, 0.24])
    elif row["Socioeconomic Status"] == "Affluent":
        return np.random.choice(alcohol_choices, p = [0.79, 0.21])
    else:
        return np.random.choice(alcohol_choices, p = [0.83, 0.17])

demographic_dataset["Drinks Alcohol"] = demographic_dataset.apply(drinks_alcohol, axis = 1)
demographic_dataset.to_csv("dataset.csv")

def alcohol_consumption(row):
    if row["Drinks Alcohol"] == "Drinks Alcohol":
        if row ["Gender"] == "Male":
            return np.random.gamma(shape = 0.98, scale = 38.57, size = 1)
        else:
            return np.random.gamma(shape = 0.91, scale = 15.55, size = 1)

    else:
        return np.zeros(1)

demographic_dataset["Alcohol Consumption"] = demographic_dataset.apply(alcohol_consumption, axis = 1)

alc_consumption = []

for value in demographic_dataset["Alcohol Consumption"].values:
    alc_consumption.append(value.item())


demographic_dataset["Alcohol Consumption"] = alc_consumption
alc_consumers = demographic_dataset.loc[demographic_dataset["Drinks Alcohol"] == "Drinks Alcohol" ]
sns.histplot(x = alc_consumers["Alcohol Consumption"], hue = alc_consumers["Gender"], palette= "coolwarm")
plt.show()
plt.close()



def hours_sleep(row):
    if row["Age"] < 24:
        if row["BMI"] > 25:
            if row ["Employment Status"] == "Employed":
                return skewnorm.rvs(a = 2, loc = 6.5, scale = 3, size = 1)
            else:
               return skewnorm.rvs(a = 2, loc = 7.2, scale = 3, size = 1)
        else:
            if row ["Employment Status"] == "Employed":
                return skewnorm.rvs(a = 2, loc = 7.1, scale = 3, size = 1)
            else:
                return skewnorm.rvs(a = 2, loc = 7.9, scale = 3, size = 1)
    else:
        if row["BMI"] > 25:
            if row["Employment Status"] == "Employed":
                return np.random.normal(6, 1, size = 1)
            else:   
                return np.random.normal(6.8, 1, size = 1)
        else:
            if row["Employment Status"] == "Employed":
                return np.random.normal(7.1, 1, size = 1)
            else:   
                return np.random.normal(7.5, 1, size = 1)

demographic_dataset["Hours Sleep"] = demographic_dataset.apply(hours_sleep, axis = 1)

hours_sleep = []

for value in demographic_dataset["Hours Sleep"].values:
    hours_sleep.append(value.item())

demographic_dataset["Hours Sleep"] = hours_sleep

sns.kdeplot(demographic_dataset["Hours Sleep"], hue = demographic_dataset["Employment Status"])
demographic_dataset.to_csv("dataset.csv")

plt.show()
plt.close()

sns.kdeplot(x = demographic_dataset["Hours Sleep"], hue = demographic_dataset["Age Category"], fill = False, palette = "coolwarm", linewidth = 3, hue_order=age_order)
plt.show()
plt.close()

smoking_choices = ["Current Smoker", "Ex Smoker", "Never Smoked"]

def smoking_status(row):
        if row["Age"] >= 24:
            if row["Socioeconomic Status"] == "Very Disadvantaged":
                return np.random.choice(smoking_choices, p = [0.4,0.1,0.5])
            if row["Socioeconomic Status"] == "Disadvantaged":
                return np.random.choice(smoking_choices, p = [0.3,0.1,0.6])
            if row["Socioeconomic Status"] == "Average":
                return np.random.choice(smoking_choices, p = [0.3,0.1,0.6])
            if row["Socioeconomic Status"] == "Affluent":
                return np.random.choice(smoking_choices, p = [0.2,0.1,0.7])
            if row["Socioeconomic Status"] == "Very Affluent":
                return np.random.choice(smoking_choices, p = [0.15,0.05,0.8])

        elif row["Age"] > 24 and row["Age"] <= 35:
            if row["Socioeconomic Status"] == "Very Disadvantaged":
                return np.random.choice(smoking_choices, p = [0.6,0.2,0.2])
            if row["Socioeconomic Status"] == "Disadvantaged":
                return np.random.choice(smoking_choices, p = [0.5,0.2,0.4])
            if row["Socioeconomic Status"] == "Average":
                return np.random.choice(smoking_choices, p = [0.45,0.05,0.5])
            if row["Socioeconomic Status"] == "Affluent":
                return np.random.choice(smoking_choices, p = [0.4,0.1,0.5])
            if row["Socioeconomic Status"] == "Very Affluent":
                return np.random.choice(smoking_choices, p = [0.4,0.1,0.5])

        elif row["Age"] > 34 and row["Age"] <= 45:
                if row["Socioeconomic Status"] == "Very Disadvantaged":
                    return np.random.choice(smoking_choices, p = [0.3,0.4,0.3])
                if row["Socioeconomic Status"] == "Disadvantaged":
                    return np.random.choice(smoking_choices, p = [0.3,0.4,0.3])
                if row["Socioeconomic Status"] == "Average":
                    return np.random.choice(smoking_choices, p = [0.2,0.05,0.3])
                if row["Socioeconomic Status"] == "Affluent":
                    return np.random.choice(smoking_choices, p = [0.1,0.6,0.3])
                if row["Socioeconomic Status"] == "Very Affluent":
                    return np.random.choice(smoking_choices, p = [0.1,0.5,0.4])
        
        elif row["Age"] > 44 and row["Age"] <= 55:
                if row["Socioeconomic Status"] == "Very Disadvantaged":
                    return np.random.choice(smoking_choices, p = [0.2,0.6,0.1])
                if row["Socioeconomic Status"] == "Disadvantaged":
                    return np.random.choice(smoking_choices, p = [0.3,0.5,0.1])
                if row["Socioeconomic Status"] == "Average":
                    return np.random.choice(smoking_choices, p = [0.2,0.05,0.3])
                if row["Socioeconomic Status"] == "Affluent":
                    return np.random.choice(smoking_choices, p = [0.1,0.6,0.3])
                if row["Socioeconomic Status"] == "Very Affluent":
                    return np.random.choice(smoking_choices, p = [0.1,0.6,0.3])
        
        elif row["Age"] > 54 and row["Age"] <= 65:
                    if row["Socioeconomic Status"] == "Very Disadvantaged":
                        return np.random.choice(smoking_choices, p = [0.2,0.3,0.3])
                    if row["Socioeconomic Status"] == "Disadvantaged":
                        return np.random.choice(smoking_choices, p = [0.2,0.3,0.3])
                    if row["Socioeconomic Status"] == "Average":
                        return np.random.choice(smoking_choices, p = [0.1,0.5,0.4])
                    if row["Socioeconomic Status"] == "Affluent":
                        return np.random.choice(smoking_choices, p = [0.05,0.55,0.4])
                    if row["Socioeconomic Status"] == "Very Affluent":
                        return np.random.choice(smoking_choices, p = [0.05,0.35,0.6])
            
        elif row["Age"] > 54 and row["Age"] <= 65:
                    if row["Socioeconomic Status"] == "Very Disadvantaged":
                        return np.random.choice(smoking_choices, p = [0.1,0.6,0.3])
                    if row["Socioeconomic Status"] == "Disadvantaged":
                        return np.random.choice(smoking_choices, p = [0.1,0.7,0.2])
                    if row["Socioeconomic Status"] == "Average":
                        return np.random.choice(smoking_choices, p = [0.1,0.6,0.3])
                    if row["Socioeconomic Status"] == "Affluent":
                        return np.random.choice(smoking_choices, p = [0.05,0.55,0.3])
                    if row["Socioeconomic Status"] == "Very Affluent":
                        return np.random.choice(smoking_choices, p = [0.05,0.4,0.55])
            
        else:
                    if row["Socioeconomic Status"] == "Very Disadvantaged":
                        return np.random.choice(smoking_choices, p = [0.05,0.85,0.1])
                    if row["Socioeconomic Status"] == "Disadvantaged":
                        return np.random.choice(smoking_choices, p = [0.05,0.85,0.1])
                    if row["Socioeconomic Status"] == "Average":
                        return np.random.choice(smoking_choices, p = [0.05,0.65,0.3])
                    if row["Socioeconomic Status"] == "Affluent":
                        return np.random.choice(smoking_choices, p = [0.05,0.55,0.4])
                    if row["Socioeconomic Status"] == "Very Affluent":
                        return np.random.choice(smoking_choices, p = [0.05,0.4,0.55])

daily_smoke = expon.rvs(size = 7500, loc = 10, scale = 5)
sns.histplot(daily_smoke)
plt.show()
plt.close()

demographic_dataset["Smoking Status"] = demographic_dataset.apply(smoking_status, axis = 1)
sns.countplot(x = "Smoking Status", data = demographic_dataset, hue = "Socioeconomic Status", hue_order=quintiles)
plt.show()
plt.close()

def cigs_per_day(row):
    if row["Smoking Status"] == "Current Smoker":
        return expon.rvs(size = 1, loc  = 5, scale = 20)
    else:
        return np.zeros(1)

demographic_dataset["Cigarettes Per Day"] = demographic_dataset.apply(cigs_per_day, axis = 1)

daily_cigs = []

for value in demographic_dataset["Cigarettes Per Day"].values:
    daily_cigs.append(value.item())
demographic_dataset["Cigarettes Per Day"] = daily_cigs

smokers_only =  demographic_dataset.loc[demographic_dataset["Smoking Status"] == "Current Smoker" ]

sns.histplot(smokers_only["Cigarettes Per Day"])
plt.show()
plt.close()
demographic_dataset.to_csv("dataset.csv")

            
        




