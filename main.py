import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import DenGAI_Func
import numpy as np
import seaborn as sns

# Time converters register
register_matplotlib_converters()

# Dataframes generation: 1 Dataframe per dataset given
train_data = pd.read_csv('./Data/dengue_features_train.csv')
test_data = pd.read_csv('./Data/dengue_features_test.csv')
labels = pd.read_csv('./Data/dengue_labels_train.csv')

# Exploring Data
train_data.info()
train_data.describe()

# Convert dates from object to datetime
train_data['week_start_date'] = pd.to_datetime(train_data['week_start_date'])
test_data['week_start_date'] = pd.to_datetime(test_data['week_start_date'])
print(train_data['week_start_date'].head())

# Some temperatures are given in celsius, other in Kelvin
# Convert all temperatures to degrees Celsius
K = 273.15
kelvin_features = ['reanalysis_max_air_temp_k',
                   'reanalysis_min_air_temp_k',
                   'reanalysis_avg_temp_k',
                   'reanalysis_air_temp_k',
                   'reanalysis_dew_point_temp_k']
for kf in kelvin_features:
    kc = kf.replace(kf[-1], 'c')
    train_data[kc] = train_data[kf] - K
    test_data[kc] = test_data[kf] - K

train_data = train_data.drop(kelvin_features, axis=1)
test_data = test_data.drop(kelvin_features, axis=1)

# Make seperate dataset for each city

# train_sj, train_iq = sep_df_bycity(train_data)
train_sj = train_data.loc[train_data['city']=='sj']
train_iq = train_data.loc[train_data['city']=='iq']

test_sj = test_data.loc[test_data['city']=='sj']
test_iq = test_data.loc[test_data['city']=='iq']

labels_sj = labels.loc[labels['city']=='sj']
labels_iq = labels.loc[labels['city']=='iq']

# EDA Step 1: How is data like
# Global Plot: Sj
plt.figure(figsize = (20, 5))
(train_sj
     .ndvi_ne
     .plot
     .line(lw = 1))

plt.show()

# Global Plot: Sj
plt.figure(figsize = (20, 5))
(train_iq
     .ndvi_ne
     .plot
     .line(lw = 1))

plt.show()

# Per City
plt.figure()
ax = plt.gca()
plt.title('Weekly dengue fever cases in San Juan and Iquitos')
plt.plot(train_sj['week_start_date'], labels_sj['total_cases'], 'b', label='San Juan')
plt.plot(train_iq['week_start_date'], labels_iq['total_cases'], 'r', label='Iquitos')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%y'))
plt.gcf().autofmt_xdate()
plt.xlabel('year')
plt.ylabel('cases')
plt.legend()
plt.grid()
plt.show()

# Correlation between variables
# San Juan (sj) - Correlation Matrix
train_sj['total_cases'] = labels_sj['total_cases']

sj_corr = train_sj.corr()

sns.set(font_scale = 2)
plt.figure(figsize=(20, 10))

sns.heatmap(sj_corr)
plt.title('Correlation Plot of all features in the San Juan Dataset')
plt.show()

# Correlation coefficients
sns.set(font_scale = 1.5)
(abs(sj_corr)
 .total_cases
 .drop('total_cases')
 .sort_values()
 .plot
 .barh())

# Filling Nan Values using the most recent observation

train_sj.sort_index(inplace = True)
train_sj.fillna(method = 'ffill', inplace = True)
test_sj.fillna(method = 'ffill', inplace = True)

train_iq.sort_index(inplace = True)
train_iq.fillna(method = 'ffill', inplace = True)
test_iq.fillna(method = 'ffill', inplace = True)