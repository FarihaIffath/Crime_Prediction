import pandas as pd
import numpy as np
np.random.seed(42)

 
# Matplotlib and seaborn for plotting
import matplotlib.pyplot as plt
%matplotlib inline

import matplotlib
matplotlib.rcParams['font.size'] = 16
matplotlib.rcParams['figure.figsize'] = (9, 9)

import seaborn as sns

from IPython.core.pylabtools import figsize

# Scipy helper functions
from scipy.stats import percentileofscore
from scipy import stats

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import ElasticNet
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR

# Splitting data into training/testing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error, median_absolute_error

# Distributions
import scipy
import pymc3 as pm

df = pd.read_csv('Final.csv')

# Grade distribution by address
sns.kdeplot(df.ix[df['Location'] == 'DMP', 'Murder'], label = 'DMP', shade = True)
sns.kdeplot(df.ix[df['Location'] == 'CMP', 'Murder'], label = 'CMP', shade = True)
sns.kdeplot(df.ix[df['Location'] == 'KMP', 'Murder'], label = 'KMP', shade = True)
sns.kdeplot(df.ix[df['Location'] == 'RMP', 'Murder'], label = 'RMP', shade = True)
sns.kdeplot(df.ix[df['Location'] == 'BMP', 'Murder'], label = 'BMP', shade = True)
sns.kdeplot(df.ix[df['Location'] == 'SMP', 'Murder'], label = 'SMP', shade = True)
sns.kdeplot(df.ix[df['Location'] == 'Dhaka Range', 'Murder'], label = 'Dhaka Range', shade = True)

plt.xlabel('Grade'); plt.ylabel('Density'); plt.title('Density Plot of Final Grades by Location');

