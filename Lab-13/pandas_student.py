"""
Pandas Lab Activity - Employee Data Analysis
Name: Kspsvln Siddardha Kumar Kavuri
Roll Number: 2025201061

Instructions:
1. Complete all functions below marked with # TODO.
2. Do not change the function names or their parameters.
3. Run this script from your terminal (`python pandas_student.py`) to execute the main() function.
4. This script will generate 'analysis_report.txt' upon successful completion.
5. Submit this completed Python file for grading.
"""
import pandas as pd
import numpy as np
import io
from contextlib import redirect_stdout

# --- Constants ---
DATA_FILE = 'employees.csv'
REPORT_FILE = 'analysis_report.txt'

# ---------------------------------
# --- PART 1: Data Loading & Inspection ---
# ---------------------------------

def load_data(file_path):
    """
    (2 Marks)
    Loads the CSV file into a Pandas DataFrame.
    Handles potential FileNotFoundError.
    
    Parameters:
    file_path (str): The path to the employees.csv file.
    
    Returns:
    pd.DataFrame or None: A DataFrame with the data, or None if the file is not found.
    """
    # TODO: Try to load the CSV file.
    # If the file is not found, print an error message and return None.
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None




def get_data_summary(df):
    """
    (1 Mark)
    Returns a string containing the output of df.info()
    
    Parameters:
    df (pd.DataFrame): The employee DataFrame.
    
    Returns:
    str: A string summary of the DataFrame (from df.info()).
    """
    # TODO: This function is tricky. df.info() prints to stdout.
    # We need to capture this.
    # Hint: Use io.StringIO and contextlib.redirect_stdout
    buffer = io.StringIO()  # Create an in-memory text stream
    with redirect_stdout(buffer):
        df.info()  # This prints to the buffer instead of stdout
    result = buffer.getvalue()
    return result

def get_statistical_summary(df):
    """
    (1 Mark)
    Returns a DataFrame containing the output of df.describe()
    
    Parameters:
    df (pd.DataFrame): The employee DataFrame.
    
    Returns:
    pd.DataFrame: The statistical summary DataFrame (from df.describe()).
    """
    # TODO: Return the statistical summary.
    return df.describe(include="all")

# ---------------------------------
# --- PART 2: Data Cleaning ---
# ---------------------------------

def clean_data(df):
    """
    (10 Marks Total)
    Cleans the DataFrame by performing the following steps:
    1. (2 Marks) Drop duplicate rows.
    2. (3 Marks) Calculate the mean salary and fill missing 'Salary' values with it.
    3. (3 Marks) Drop any rows that are missing a 'Hire Date'.
    4. (2 Marks) Convert 'Hire Date' column to datetime objects.
    
    Parameters:
    df (pd.DataFrame): The dirty employee DataFrame.
    
    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    df_result=df.copy()
    # TODO: 1. Drop duplicates
    df_result=df_result.drop_duplicates().reset_index(drop=True)
    # df_result.to_csv("employees_output1.csv", index=False)

    # TODO: 2. Fill missing 'Salary' with the mean
    df_result['Salary'] = df_result['Salary'].fillna(df_result['Salary'].mean())
    # df_result.to_csv("employees_output2.csv", index=False)
    # TODO: 3. Drop rows missing 'Hire Date'
    df_result = df_result.dropna(subset=['Hire Date']).reset_index(drop=True)
    # df_result.to_csv("employees_output3.csv", index=False)
    # TODO: 4. Convert 'Hire Date' to datetime
    df_result['Hire Date'] = pd.to_datetime(df_result['Hire Date'])
    # df_result.to_csv("employees_output4.csv", index=False)

    return df_result
    
    
# ---------------------------------
# --- PART 3: Data Selection ---
# ---------------------------------

def select_engineering_employees(df):
    """
    (3 Marks)
    Selects all employees who are in the 'Engineering' department.
    
    Parameters:
    df (pd.DataFrame): The cleaned employee DataFrame.
    
    Returns:
    pd.DataFrame: A DataFrame containing only Engineering employees.
    """
    # TODO: Use boolean indexing to select rows
    df_result=df[df['Department']=='Engineering']

    return df_result

def select_high_earners(df):
    """
    (3 Marks)
    Selects all employees who earn more than 80,000.
    
    Parameters:
    df (pd.DataFrame): The cleaned employee DataFrame.
    
    Returns:
    pd.DataFrame: A DataFrame containing only employees with Salary > 80000.
    """
    # TODO: Use boolean indexing to select rows
    df_result=df[df['Salary']>80000]
    return df_result

def select_names_and_salaries(df):
    """
    (2 Marks)
    Selects only the 'Name' and 'Salary' columns from the DataFrame.
    
    Parameters:
    df (pd.DataFrame): The cleaned employee DataFrame.
    
    Returns:
    pd.DataFrame: A DataFrame containing only the 'Name' and 'Salary' columns.
    """
    # TODO: Select a subset of columns
    df_result=df[['Name','Salary']]

    return df_result

# ---------------------------------
# --- PART 4: Data Transformation ---
# ---------------------------------

def add_years_of_service(df):
    """
    (4 Marks)
    Creates a new column 'Years of Service' by calculating
    (2025 - hire_year).
    
    Parameters:
    df (pd.DataFrame): The cleaned employee DataFrame (with 'Hire Date' as datetime).
    
    Returns:
    pd.DataFrame: The DataFrame with the new 'Years of Service' column.
    """
    # TODO: Create the new column. Assumes 'Hire Date' is already datetime.
    df_result=df.copy()
    df_result['Years of Service']=2025-df['Hire Date'].dt.year

    return df_result


def get_bonus_tiers(salary):
    """
    Helper function for apply_bonus_tiers.
    Returns 'High' if salary > 75000, 'Medium' if 60000 <= salary <= 75000,
    and 'Low' otherwise.
    """
    if salary > 75000:
        return 'High'
    elif salary >= 60000:
        return 'Medium'
    else:
        return 'Low'

def apply_bonus_tiers(df):
    """
    (4 Marks)
    Creates a new column 'Bonus Tier' by applying the 
    `get_bonus_tiers` helper function to the 'Salary' column.
    
    Parameters:
    df (pd.DataFrame): The DataFrame from the previous step.
    
    Returns:
    pd.DataFrame: The DataFrame with the new 'Bonus Tier' column.
    """
    # TODO: Use the .apply() method to create the 'Bonus Tier' column
    df_result=df.copy()
    df_result['Bonus Tier']=df['Salary'].apply(get_bonus_tiers)

    return df_result

# ---------------------------------
# --- PART 5: Data Aggregation ---
# ---------------------------------

def get_average_salary_by_dept(df):
    """
    (5 Marks)
    Calculates the average salary for each department.
    
    Parameters:
    df (pd.DataFrame): The DataFrame from the previous step.
    
    Returns:
    pd.Series: A Series with 'Department' as the index and avg salary as values.
    """
    # TODO: Use groupby() and mean()

    return df.groupby('Department')['Salary'].mean()



def get_department_stats(df):
    """
    (5 Marks)
    Calculates the mean salary, max 'Years of Service', and total
    number of employees for each department.
    
    Parameters:
    df (pd.DataFrame): The DataFrame from the previous step.
    
    Returns:
    pd.DataFrame: A DataFrame with 'Department' as index and columns 
                  for 'Mean Salary', 'Max Years of Service', and 'Employee Count'.
    """
    # TODO: Use groupby() and agg()
    grouped = df.groupby('Department').agg(
        **{
            'Mean Salary': ('Salary', 'mean'),
            'Max Years of Service': ('Years of Service', 'max'),
            'Employee Count': ('EmployeeID', 'count')
        }
    )
    
    return grouped

# ---------------------------------
# --- Main Execution & Report Generation ---
# ---------------------------------

def main():
    """
    Main function to run the entire analysis and generate a report.
    You do not need to edit this function.
    """
    # Part 1
    print("Part 1: Loading Data...")
    df = load_data(DATA_FILE)
    if df is None:
        return
    
    info_summary = get_data_summary(df)
    stats_summary = get_statistical_summary(df)

    # Part 2
    print("Part 2: Cleaning Data...")
    df_clean = clean_data(df.copy()) # Use .copy() to avoid SettingWithCopyWarning

    # Part 3
    print("Part 3: Selecting Data...")
    eng_df = select_engineering_employees(df_clean)
    high_earners_df = select_high_earners(df_clean)
    names_salaries_df = select_names_and_salaries(df_clean)

    # Part 4
    print("Part 4: Transforming Data...")
    df_with_yos = add_years_of_service(df_clean)
    df_with_bonus = apply_bonus_tiers(df_with_yos)

    # Part 5
    print("Part 5: Aggregating Data...")
    avg_salary = get_average_salary_by_dept(df_with_bonus)
    dept_stats = get_department_stats(df_with_bonus)

    # Generate Report
    print(f"Generating report at {REPORT_FILE}...")
    try:
        with open(REPORT_FILE, 'w') as f:
            f.write("="*50 + "\n")
            f.write("Pandas Lab Activity - Analysis Report\n")
            f.write("="*50 + "\n\n")

            f.write("--- PART 1: Initial Data Inspection ---\n")
            f.write("Original Data Info:\n")
            f.write(info_summary)
            f.write("\nStatistical Summary (Original Data):\n")
            f.write(stats_summary.to_string())
            f.write("\n\n")

            f.write("--- PART 2: Cleaned Data Info ---\n")
            f.write(get_data_summary(df_clean)) # Info for cleaned data
            f.write("\n\n")

            f.write("--- PART 3: Data Selection Examples ---\n")
            f.write("Engineering Employees:\n")
            f.write(eng_df.to_string())
            f.write("\n\nHigh Earners (>$80k):\n")
            f.write(high_earners_df.to_string())
            f.write("\n\nNames and Salaries:\n")
            f.write(names_salaries_df.head().to_string())
            f.write("\n\n")

            f.write("--- PART 4: Data Transformation Example ---\n")
            f.write("Data with 'Years of Service' and 'Bonus Tier':\n")
            f.write(df_with_bonus.head().to_string())
            f.write("\n\n")

            f.write("--- PART 5: Data Aggregation ---\n")
            f.write("Average Salary by Department:\n")
            f.write(avg_salary.to_string())
            f.write("\n\nComprehensive Department Stats:\n")
            f.write(dept_stats.to_string())
            f.write("\n\n")

            f.write("="*50 + "\n")
            f.write("Report Generation Complete.\n")
            f.write("="*50 + "\n")
        
        print(f"Successfully generated {REPORT_FILE}")
    
    except Exception as e:
        print(f"Error writing report: {e}")

if __name__ == "__main__":
    main()

