# Project-4

# Hotel Employee Performance Dashboard

This project is a predictive analytics dashboard designed to assess employee performance at a hotel based on various metrics such as attendance, task completion, and customer service. The application uses a linear regression model to predict performance scores and provides visual insights into employee performance trends over time.

## Overview
The **Hotel Employee Performance Dashboard** is an interactive web application built using Streamlit. It allows hotel management to view, predict, and analyze employee performance. Performance metrics like attendance, task completion, and customer service are adjustable via sliders, and the dashboard provides real-time updates on predicted performance.

The main features include:
- Employee performance predictions based on custom metrics.
- Visual performance progression displayed on a line chart.
- Customizable sliders to adjust employee metrics.
- A visually styled dashboard with color-coded performance indicators.

## Features
- **Employee Details:** View details like employee role, sex, age, start date, and current performance metrics.
- **Performance Prediction:** Predict employee performance based on attendance, task completion, and customer service.
- **Performance Progression:** View a month-by-month performance progression with color-coded score ranges (green, yellow, red).
- **Custom Styling:** Personalized dashboard with custom fonts, background color, and theme.

## Technologies Used
- **Python**: Core programming language for building the app.
- **Streamlit**: Framework for creating the interactive web dashboard.
- **SQLite**: Database to store employee information.
- **Pandas**: Data manipulation and analysis.
- **Matplotlib**: Plotting and visualization of employee performance.
- **Scikit-learn**: Linear regression model for performance prediction.

## Installation
### Prerequisites
- Python 3.x
- Streamlit
- Pandas
- SQLite
- Matplotlib
- Scikit-learn

### Usage
1. Lunch the Streamlit app by running "streamlit run app.py" in the terminal.
2. Select an employee from the sideba to view their details.
3. Adjust the performance metrics (attendance, task completion, customer service) using the sliders.
4. View the updated predicted performance score and the employee's performance progress over time. 

### Model Details

The dashboard uses a Linear Regression Model to predict and employee's overall performance score based on threee key metrics:

1. Attendance
2. Task Completion
3. Customer Service

The model was trained on historical data, which included employee performance metrics. The predicted performance score helps management assess and improve employee productivity. 

### License

This project is licensed under the MIT License
