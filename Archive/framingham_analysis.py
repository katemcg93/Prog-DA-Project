import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pandas.core import frame
import seaborn as sns
import numpy as np
from numpy import random
from scipy import stats
from scipy.stats import powerlaw
from scipy.stats import skewnorm
from scipy.stats import rayleigh 
from fitter import Fitter, get_common_distributions, get_distributions
from matplotlib.pyplot import hist
np.random.seed (1245)
rng = random.default_rng()

col_names = ()
framingham_df = pd.read_csv( "C:\\Users\\Owner\\Desktop\\repos\\Prog-DA-Project\Archive\\Framingham Heart Study.csv", na_values=['(NA)']).fillna(0)
print(framingham_df.columns)

framingham_df[["age", "cigsPerDay", "totChol", "sysBP", "diaBP", "BMI", "heartRate", "glucose"]].apply(pd.to_numeric, errors='coerce')
print(framingham_df.describe())

age = framingham_df["age"].astype(int).to_numpy()

sns.histplot(age, bins=100)
plt.show()
plt.close()

framingham_df.loc[framingham_df['age']<40, 'age_group'] = 'Group 1'
framingham_df.loc[framingham_df['age'].between(40,49), 'age_group'] = 'Group 2'
framingham_df.loc[framingham_df['age'].between(50,75), 'age_group'] = 'Group 3'



u40 = framingham_df.loc[framingham_df["age_group"] == "Group 1"]
print(u40.count())

b40_49 = framingham_df.loc[framingham_df["age_group"] == "Group 2"]
print(b40_49.count())

b50_75 = framingham_df.loc[framingham_df["age_group"] == "Group 3"]
print(b50_75.count())


def summarize (x, y):
    f = Fitter(x,distributions = get_common_distributions(), bins = 10)
    f.fit()
    print(f.summary())
    print(x.std())
    print(x.mean())
    plt.savefig("{}.png".format(y))
    plt.close()
    return f

current_smoker = framingham_df.loc[framingham_df["currentSmoker"] == 1]

summarize(x = framingham_df["cigsPerDay"], y ="cigs.png")