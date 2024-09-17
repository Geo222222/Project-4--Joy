import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Connect to SQLite database 
conn = sqlite3.connect('hotel_employees.db')
cursor = conn.cursor()

# Drop the table if it exists to ensure fresh data insertion
cursor.execute('DROP TABLE IF EXISTS employee_data')

# Create a new table with all necessary fields
cursor.execute('''
    CREATE TABLE employee_data (
        employee_id INTEGER PRIMARY KEY,
        name TEXT,
        role TEXT,
        sex TEXT,
        age INTEGER,
        start_date DATE,
        attendance REAL,
        task_completion REAL,
        customer_service REAL,
        guest_satisfaction REAL,
        performance_score REAL
    )
''')

# Define employee roles
roles = ['Housekeeping', 'Front Desk', 'Maintenance', 'Breakfast', 'Restaurant', 'Valet', 'Bartender', 'Janitor']

# Seed for reproducibility
np.random.seed(42)

# Generate sample data for 100 employees
num_employees = 100
names = [f"Employee_{i}" for i in range(1, num_employees + 1)]
sex = np.random.choice(['Male', 'Female'], num_employees)
ages = np.random.randint(20, 60, num_employees)

# Generate random start dates within the last 5 years
start_dates = [datetime.now() - timedelta(days=np.random.randint(365, 365 * 5)) for _ in range(num_employees)]

# Create the employee data
employee_data = []
for i in range(num_employees):
    employee_id = i + 1
    name = f"Employee_{employee_id}"  # Using actual employee ID as part of the name or replace with real names later
    role = np.random.choice(roles)
    start_date = start_dates[i].strftime('%Y-%m-%d')
    attendance = np.random.randint(60, 100)
    task_completion = np.random.randint(50, 100)
    customer_service = np.random.randint(40, 100)
    guest_satisfaction = np.random.randint(1, 10)
    performance_score = (attendance + task_completion + customer_service) / 3  # Example performance score formula

    # Add employee data tuple to the list
    employee_data.append((name, role, sex[i], ages[i], start_date, attendance, task_completion, customer_service, guest_satisfaction, performance_score))

# Insert employee data into the SQLite database
cursor.executemany('''
    INSERT INTO employee_data (name, role, sex, age, start_date, attendance, task_completion, customer_service, guest_satisfaction, performance_score)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', employee_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database setup complete!")
