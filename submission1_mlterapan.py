# -*- coding: utf-8 -*-
"""Submission1_MLTerapan.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XTpZaWCapMmHYrUw6tyJEncfRkS4POc4

### Import Libraries Needed
"""

import pandas as pd
import numpy as np
from google.colab import files
import seaborn as sns
import matplotlib.pyplot as plt

"""### Import Data"""

df = pd.read_csv('https://raw.githubusercontent.com/jerichols/MLTerapan/main/BBRI.JK.csv')
df

# Set Date as index
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

df.info() #Check data type and count

df.isnull().sum() #Checking if there is null value in the data

df.describe() # Checking more detailed about the data to see if there is any "unclean" data

"""### Plotting Relationship"""

sns.pairplot(df)

corr_matrix = df.select_dtypes(include='number').corr()
print("\nMatriks Korelasi:")
print(corr_matrix)

# Check the correlation between column

"""### Checking Outlier"""

sns.boxplot(y="Open", data=df, color="skyblue")
plt.title('Boxplot of Open')
plt.show()

sns.boxplot(y="High", data=df, color="salmon")
plt.title('Boxplot of High')
plt.show()

sns.boxplot(y="Low", data=df, color="lightgreen")
plt.title('Boxplot of Low')
plt.show()

sns.boxplot(y="Close", data=df, color="lightcoral")
plt.title('Boxplot of Close')
plt.show()

sns.boxplot(y="Adj Close", data=df, color="lightblue")
plt.title('Boxplot of Adj Close')
plt.show()

sns.boxplot(y="Volume", data=df, color="orange")
plt.title('Boxplot of Volume')
plt.show()

# Function to calculate outliers
def identify_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers, lower_bound, upper_bound

# Identify outliers for 'Adj Close'
adj_close_outliers, adj_close_lower, adj_close_upper = identify_outliers(df, 'Adj Close')
print(f"Adj Close - Lower Bound: {adj_close_lower}, Upper Bound: {adj_close_upper}")
print(f"Number of outliers in 'Adj Close': {len(adj_close_outliers)}")

# Identify outliers for 'Volume'
volume_outliers, volume_lower, volume_upper = identify_outliers(df, 'Volume')
print(f"Volume - Lower Bound: {volume_lower}, Upper Bound: {volume_upper}")
print(f"Number of outliers in 'Volume': {len(volume_outliers)}")

"""As you can see there is some outlier in Adj Close and Volume, i chose to remove the outlier because its a small sample that it doesnt effect much of the data."""

# Remove outliers for 'Adj Close'
df_cleaned_adj_close = df[(df['Adj Close'] >= adj_close_lower) & (df['Adj Close'] <= adj_close_upper)]

# Remove outliers for 'Volume'
df_cleaned = df_cleaned_adj_close[(df_cleaned_adj_close['Volume'] >= volume_lower) & (df_cleaned_adj_close['Volume'] <= volume_upper)]

print(f"Original DataFrame Size: {df.shape}")
print(f"Cleaned DataFrame Size: {df_cleaned.shape}")

df_cleaned.describe()

"""### Data Preprocessing

#### Drop Adj Close
"""

# Droping Adj CLose because it is not usefull for realtime prediction
df_cleaned = df_cleaned.drop(columns=['Adj Close'])

"""#### Spliting the data into training and testing"""

from sklearn.model_selection import train_test_split

# Define features and target
features = ['Open', 'High', 'Low', 'Volume']
target = 'Close'

# Split the data into features (X) and target (y)
X = df_cleaned[features]
y = df_cleaned[target]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training Data Size: {X_train.shape}, Testing Data Size: {X_test.shape}")

print(f'Total # of sample in whole dataset: {len(X)}')
    print(f'Total # of sample in train dataset: {len(X_train)}')
    print(f'Total # of sample in test dataset: {len(X_test)}')

"""#### Standartization training Data"""

from sklearn.preprocessing import MinMaxScaler

# Initialize the scaler
scaler = MinMaxScaler()

# Fit the scaler on the entire DataFrame
scaler.fit(X_train)

# Transform the entire DataFrame
X_train_scaled = scaler.transform(X_train)

# Convert the scaled NumPy array back to DataFrame, maintaining column names
X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns, index = X_train.index)

# Display the scaled DataFrame
print(X_train_scaled.head())

"""### Models"""

models = pd.DataFrame(index=['train_mse', 'test_mse'],  columns=[ 'RandomForest', 'Boosting'])

"""#### Random Forest"""

# Impor library yang dibutuhkan
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_squared_error

    # buat model prediksi
    RF = RandomForestRegressor(n_estimators=200, max_depth=8, random_state=55, n_jobs=-1)
    RF.fit(X_train_scaled, y_train)


    models.loc['train_mse','RandomForest'] = mean_squared_error(y_pred=RF.predict(X_train_scaled), y_true=y_train)

# Get feature importances from Random Forest
importances_rf = RF.feature_importances_
features = X_train.columns

# Create a DataFrame for visualization
importance_df_rf = pd.DataFrame({'Feature': features, 'Importance': importances_rf})
importance_df_rf = importance_df_rf.sort_values(by='Importance', ascending=False)
importance_df_rf

# Plot feature importances
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=importance_df_rf, palette='viridis')
plt.title('Feature Importance - Random Forest')
plt.show()

"""#### Boost Algorithm


"""

import xgboost as xgb
from sklearn.metrics import mean_squared_error

# Define the XGBoost regressor
boosting = xgb.XGBRegressor(
    learning_rate=0.08,
    n_estimators=200,
    max_depth=4,
    random_state=55
)
# Fit the model
boosting.fit(X_train_scaled, y_train)

# Predict and evaluate
y_train_pred = boosting.predict(X_train_scaled)
train_mse = mean_squared_error(y_true=y_train, y_pred=y_train_pred)

# Update the models DataFrame
models.loc['train_mse', 'XGBoost'] = train_mse

# Get feature importances from XGBoost
importances_boosting = boosting.feature_importances_
importance_df_boosting = pd.DataFrame({'Feature': features, 'Importance': importances_boosting})
importance_df_boosting = importance_df_boosting.sort_values(by='Importance', ascending=False)

importance_df_boosting

# Plot feature importances
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=importance_df_boosting, palette='viridis')
plt.title('Feature Importance - XGBoost')
plt.show()

"""### Evaluasi Model"""

# Scale the Test Data
X_test_scaled = scaler.transform(X_test)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns,  index=X_test.index)

mse = pd.DataFrame(columns=['train', 'test'], index=['RF','Boosting'])

# Buat dictionary untuk setiap algoritma yang digunakan
model_dict = { 'RF': RF, 'Boosting': boosting}

# Hitung Mean Squared Error masing-masing algoritma pada data train dan test
for name, model in model_dict.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train_scaled))/1e3
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test_scaled))/1e3

# Panggil mse
mse

#Plotting the evaluation
    fig, ax = plt.subplots()
    mse.sort_values(by='test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
    ax.grid(zorder=0)

#Make a prediction based on the data
  prediksi = X_test_scaled.iloc[:1].copy()
  pred_dict = {'y_true':y_test[:1]}
  for name, model in model_dict.items():
      pred_dict['prediksi_'+name] = model.predict(prediksi).round(1)

  pd.DataFrame(pred_dict)

"""As we can see random forest algorithm perform better the XGBoost

#### Plot the prediction
"""

# Make predictions on the test set
y_test_pred_rf = RF.predict(X_test_scaled)

# Create a DataFrame for plotting with the dates from the test set
plot_df = pd.DataFrame({
    'Date': df_cleaned.loc[X_test.index].index,  # Access dates from index
    'Actual': y_test.values,
    'Predicted_RF': y_test_pred_rf
})

# Sort the DataFrame by date
plot_df.sort_values(by='Date', inplace=True)

# Plotting the predictions vs actual values
plt.figure(figsize=(14, 7))
plt.plot(plot_df['Date'], plot_df['Actual'], label='Actual', color='blue', linestyle='--', marker='o', markersize=4)
plt.plot(plot_df['Date'], plot_df['Predicted_RF'], label='Predicted by RF', color='red', linestyle='-', marker='x', markersize=4)
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Actual vs Predicted Close Price Using Random Forest')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()