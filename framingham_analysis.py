import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from numpy import random
from scipy import stats
from fitter import Fitter, get_common_distributions, get_distributions
from matplotlib.pyplot import hist


col_names = ()
framingham_df = pd.read_csv( "Framingham Heart Study.csv", na_values=['(NA)']).fillna(0)
print(framingham_df.columns)

framingham_df[["age", "cigsPerDay", "totChol", "sysBP", "diaBP", "BMI", "heartRate", "glucose"]].apply(pd.to_numeric, errors='coerce')
print(framingham_df.describe())

age = framingham_df["age"].to_numpy()
age_mode = stats.mode(age)
print(age_mode)

f = Fitter(age, distributions= get_common_distributions(), bins = 10)
f.fit()

print(f.summary())
plt.show()
plt.close()



