# -*- coding: utf-8 -*-
"""Another copy of PP_10_06_projects.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oYYSOH2mHxi5MtOdh-WOk94rYqFwJ0eF

Project Title: "Personal Expense Tracker"

Objective

Develop a Python application that allows users to track and analyze their daily expenses using
concepts learned in the course, including file handling, data structures, loops, NumPy, and
Pandas.

1. User Input and Data Storage
● Allow users to input expense details through the console:
○ Fields: Date, Category (e.g., Food, Rent, Entertainment), Amount,
Description.

● Use File Handling to save the data in a CSV file.

2. Expense Summary and Analysis

● Use Pandas to:

○ Read the stored expenses from the CSV file.

○ Group expenses by category and calculate total expenses for each.

○ Analyze monthly total expenses and average daily expenses.
"""

import pandas as pd
df = pd.read_csv('/MOCK_DATA.csv')
print(df)

df.shape

df.tail()

import pandas as pd


data = {
    "id": [
        "23.53.40.139/6", "233.168.249.50/26", "180.70.67.14/20", "139.208.154.147/8",
        "246.98.17.246/11", "167.248.222.4/17", "168.202.249.199/17", "123.145.50.70/21",
        "159.134.203.89/10", "139.202.233.243/18"
    ],
    "date": [
        "10/8/2024", "8/12/2024", "2/13/2024", "12/5/2024", "3/18/2024",
        "2/18/2024", "8/3/2024", "8/22/2024", "5/17/2024", "5/11/2024"
    ],
    "category": [
        "Organix Complete", "Healing Waters White Tea Pear Hand Sanitizer",
        "VP CH Plus", None, None, "CVS Fast Acting Baby Teething", "Fenoglide",
        "AMOXICILLIN", "Nux vomica", "Adenosine"
    ],
    "amount": [
        5.00, 2.25, 3.41, 9.28, 9.44, 6.62, 6.53, 3.23, 3.92, 4.13
    ],
    "description": [
        "Ardeen", "Trudey", "Mycah", "Chester", "Ebonee", "Alidia", "Ilene", "Barbi", "Vicky", "Delmar"
    ]
}

df = pd.DataFrame(data)


df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')


df['year_month'] = df['date'].dt.to_period('M')


monthly_expenses = df.groupby('year_month')['amount'].sum().reset_index()


monthly_expenses['days_in_month'] = monthly_expenses['year_month'].apply(lambda x: pd.Period(year=x.year, month=x.month, freq='M').days_in_month)


monthly_expenses['average_daily_expense'] = monthly_expenses['amount'] / monthly_expenses['days_in_month']
t
print(monthly_expenses)

def update_title_of_df(title,new_title):
  df.loc[df['title'] ==title,'title']=new_title
  return df

previous_title_of_df(title,)

"""filter or search"""

def filter_df(df,coloum_name,search_key):
  return df[df[column_name]==search_key]

def filter_df(df, column_name, search_key):
  searched_df = df[df[column_name] == search_key]
  if searched_df.empty:
    return f"No data found with search key: {search_key}"
  else:
    return searched_df

"""3. Visualization
● Use Matplotlib or Pandas Visualization to:
○ Create a pie chart showing the percentage of expenses per category.
○ Plot a bar chart of monthly expenses.
○ Generate a line graph of daily expenses for a selected month.






"""

import pandas as pd
import matplotlib.pyplot as plt


data = {
    "id": [
        "23.53.40.139/6", "233.168.249.50/26", "180.70.67.14/20", "139.208.154.147/8", "246.98.17.246/11",
        "167.248.222.4/17", "168.202.249.199/17", "123.145.50.70/21", "159.134.203.89/10", "139.202.233.243/18"
    ],
    "date": [
        "10/8/2024", "8/12/2024", "2/13/2024", "12/5/2024", "3/18/2024",
        "2/18/2024", "8/3/2024", "8/22/2024", "5/17/2024", "5/11/2024"
    ],
    "category": [
        "Organix Complete", "Healing Waters White Tea Pear Hand Sanitizer", "VP CH Plus", None, None,
        "CVS Fast Acting Baby Teething", "Fenoglide", "AMOXICILLIN", "Nux vomica", "Adenosine"
    ],
    "amount": [
        5.00, 2.25, 3.41, 9.28, 9.44, 6.62, 6.53, 3.23, 3.92, 4.13
    ],
    "description": [
        "Ardeen", "Trudey", "Mycah", "Chester", "Ebonee", "Alidia", "Ilene", "Barbi", "Vicky", "Delmar"
    ]
}


df = pd.DataFrame(data)


df['category'].fillna('Unknown', inplace=True)

category_expenses = df.groupby('category')['amount'].sum()

plt.figure(figsize=(8, 8))
category_expenses.plot(kind='pie', autopct='%1.1f%%', startangle=90, cmap='viridis')
plt.title("Expense Breakdown by Category")
plt.ylabel('')
plt.show()


df['date'] = pd.to_datetime(df['date'])


df['year_month'] = df['date'].dt.to_period('M')


monthly_expenses = df.groupby('year_month')['amount'].sum()


monthly_expenses.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title("Monthly Expenses")
plt.xlabel("Month")
plt.ylabel("Total Expense ($)")
plt.xticks(rotation=45)
plt.show()

february_data = df[(df['date'].dt.month == 2) & (df['date'].dt.year == 2024)]


february_data['day'] = february_data['date'].dt.day
daily_expenses = february_data.groupby('day')['amount'].sum()


daily_expenses.plot(kind='line', marker='o', figsize=(10, 6), color='orange')
plt.title("Daily Expenses in February 2024")
plt.xlabel("Day")
plt.ylabel("Total Expense ($)")
plt.xticks(range(1, 29))
plt.grid(True)
plt.show()

"""4. Applying Functions and Logic
● Implement Functions for:
○ Adding a new expense entry.
○ Deleting an expense based on the entry ID or description.
○ Generating a summary report of total and category-wise expenses.

5. Advanced Features (Optional for Bonus Marks)
● Regular Expressions (RegEx):
○ Validate date inputs (e.g., YYYY-MM-DD format).
● Exception Handling:
○ Handle errors like invalid input (e.g., non-numeric amounts) or missing files.

● Keyword-Based Search:
○ Allow users to search for expenses based on keywords in the description.

6. User Interaction
● Provide a menu-driven interface for the user to:
○ Add a new expense.
○ View expense summaries (daily, monthly, or category-wise).
○ Update or delete an expense entry.
○ Export filtered data to a new CSV file.
7. Using NumPy for Statistical Analysis
● Use NumPy to:
○ Calculate statistical measures like the highest, lowest, and average expense.
○ Identify spending trends (e.g., days with the highest and lowest expenses).
"""