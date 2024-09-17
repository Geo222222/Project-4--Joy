# model_training.py

import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Connect to SQLite database
conn = sqlite3.connect('hotel_employees.db')

# Load data from the employee_data table
employee_data = pd.read_sql_query('SELECT * FROM employee_data', conn)
conn.close()

# Define features (attendance, task completion, customer service) and target (performance_score)
X = employee_data[['attendance', 'task_completion', 'customer_service']]  # Multiple features
y = employee_data['performance_score']

# Split data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model to a file using pickle
with open('employee_performance_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model training complete!")


