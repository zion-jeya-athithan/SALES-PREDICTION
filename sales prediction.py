import pandas as pd
df = pd.read_excel ('D:/ZION INTERNSHIP/advertising.xlsx')
print("DATA LOADED")
df.info()

print(df.head())
print(df.info())
print(df.isnull().sum())
print("DATA IS INSPECTED")
df.dropna(inplace=True)
print("MISSING VALUES HANDLED")

print("Basic statistics")
print(df.describe())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the datase
# Splitting the data into features (X) and target variable (y)
X = df.drop(columns=["Sales"])
y = df["Sales"]

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the Random Forest model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Making predictions
y_pred = rf_model.predict(X_test)

# Evaluating model performance
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

# Print results
print(f"MAE: {mae:.2f}, MSE: {mse:.2f}, RMSE: {rmse:.2f}, R² Score: {r2:.2f}")

# Separate Graph for Actual Sales
plt.figure(figsize=(6,6))
plt.scatter(range(len(y_test)), y_test, color='blue', label='Actual Sales')
plt.xlabel("Data Points")
plt.ylabel("Sales")
plt.title("Actual Sales Distribution")
plt.legend(loc='upper left')
plt.show()
plt.close()

# Separate Graph for Predicted Sales
plt.figure(figsize=(6,6))
plt.scatter(range(len(y_pred)), y_pred, color='green', label='Predicted Sales')
plt.xlabel("Data Points")
plt.ylabel("Sales")
plt.title("Predicted Sales Distribution")
plt.legend(loc='upper left')
plt.show()
plt.close()

# Correlation Heatmap
plt.figure(figsize=(6,6))
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Feature Correlation Heatmap")
plt.show()
plt.close()



