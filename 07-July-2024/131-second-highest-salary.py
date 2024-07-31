# TITLE: SECOND HIGHEST SALARY
# TASK : Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).
# Source: https://leetcode.com/problems/second-highest-salary
# 31 July 2024


# LET'S GO!
# 1st
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # sort data to descending and drop duplicate value
    employee = employee.sort_values(by='salary', ascending=False).drop_duplicates(subset=['salary'])
    
    # make new dataframe as the result
    result_df = pd.DataFrame()
    if len(employee) > 1:
        result_df = employee.iloc[[1], [1]] # take row at index 1 and column at index 1
        result_df = result_df.rename(columns={ 'salary':'SecondHighestSalary'})  # rename column
    else:
        result_df = pd.DataFrame({ 'SecondHighestSalary': [None] }) # make new dataframe with null value

    return result_df