# TITLE: EMPLOYESS EARNING MORE THAN MANAGERS
# TASK : Write a solution to find the employees who earn more than their managers.
# Source: https://leetcode.com/problems/employees-earning-more-than-their-managers
# 30 July 2024

# LET'S GO!
import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(employee, employee, left_on='managerId', right_on='id', suffixes=('', '_manager')) # merge into a large dataframe with wide cplumn
    result_df = merged_df[merged_df['salary'] > merged_df['salary_manager']] # get the result that have bigger salary than his manager
    result_df = result_df[['name']] # get the 'name' column only
    result_df = result_df.rename(columns={ 'name': 'Employee'}) # rename column from 'name' to 'Employee'
    return result_df
