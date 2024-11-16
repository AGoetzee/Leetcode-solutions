import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    #  Do we have enough values in the dataframe?
    if employee.shape[0] < N or employee['salary'].unique().shape[0] < N or N < 1:
        return pd.DataFrame({f'getNthHighestSalary({N})': np.nan},index=[1])
   
    # We have enough values. Sort the array of unique salaries and wrap it inside a dataframe constructor
    else: 
        return pd.DataFrame([np.sort(employee['salary'].unique())[::-1][N-1]],columns=[f'getNthHighestSalary({N})'])