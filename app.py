# app.py
import streamlit as st
import sqlite3
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect('hotel_employees.db')

# Load employee data from the database
employee_data = pd.read_sql_query('SELECT * FROM employees', conn)
conn.close()

# Load the trained linear regression model
with open('employee_performance_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Page title
st.title("Hotel Employee Performance Dashboard")

# Select an employee from the sidebar
st.sidebar.header("Select an Employee")
employee_names = employee_data['name'].tolist()
selected_employee = st.sidebar.selectbox("Choose an employee", employee_names)

# Get selected employee's data
employee = employee_data[employee_data['name'] == selected_employee].iloc[0]

# Display employee details
st.subheader(f"Employee Details: {selected_employee}")
st.write(f"Role: {employee['role']}")
st.write(f"Sex: {employee['sex']}")
st.write(f"Age: {employee['age']} years")
st.write(f"Start Date: {employee['start_date']}")
st.write(f"Attendance: {employee['attendance']}%")
st.write(f"Task Completion: {employee['task_completion']}%")
st.write(f"Customer Service: {employee['customer_service']}%")

# Sliders for adjusting performance metrics
new_attendance = st.slider(
    f"Adjust Attendance for {selected_employee}", 
    min_value=60, max_value=100, 
    value=int(employee['attendance'])
)

new_task_completion = st.slider(
    f"Adjust Task Completion for {selected_employee}", 
    min_value=50, max_value=100, 
    value=int(employee['task_completion'])
)

new_customer_service = st.slider(
    f"Adjust Customer Service for {selected_employee}", 
    min_value=40, max_value=100, 
    value=int(employee['customer_service'])
)

# Predict performance score based on adjusted metrics
predicted_performance = model.predict([[new_attendance, new_task_completion, new_customer_service]])[0]
st.write(f"Predicted Performance Score: {predicted_performance:.2f}%")

# Simulated performance progression over time
months = np.arange(1, 13)
performance_progress = np.clip(
    employee['attendance'] + np.random.normal(0, 5, 12), 
    60, 100
)

# Plot the progress chart with color-coded performance ranges
st.subheader(f"Performance Progress for {selected_employee}")
fig, ax = plt.subplots()

# Color segments based on performance score ranges
for i in range(len(months)-1):
    if performance_progress[i] > 85:
        color = 'green'
    elif performance_progress[i] < 70:
        color = 'red'
    else:
        color = 'yellow'
    
    ax.plot(months[i:i+2], performance_progress[i:i+2], marker='o', linestyle='-', color=color)

# Add horizontal lines for reference
ax.axhline(85, color='green', linestyle='--', label='Excellent Performance (85% and above)')
ax.axhline(70, color='yellow', linestyle='--', label='Satisfactory Performance (70%-85%)')
ax.axhline(70, color='red', linestyle='--', label='Needs Improvement (Below 70%)')

# Labels and Title
ax.set_xlabel("Month")
ax.set_ylabel("Performance Score (%)")
ax.set_title(f"{selected_employee}'s Performance Progress")
ax.legend()

# Display the chart
st.pyplot(fig)

# Display performance metrics underneath the chart
st.write(f"Adjusted Attendance: {new_attendance}%")
st.write(f"Adjusted Task Completion: {new_task_completion}%")
st.write(f"Adjusted Customer Service: {new_customer_service}%")

# Performance color legend
st.write(
    "Performance Legend: \n"
    "- **Green**: Excellent (Above 85%)\n"
    "- **Red**: Needs Improvement (Below 70%)\n"
    "- **Yellow**: Satisfactory (Between 70% and 85%)"
)
