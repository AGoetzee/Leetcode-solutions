import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
    unique_salaries = np.sort(employee['salary'].unique())[::-1]

    if unique_salaries.shape[0] >= 2:
        return pd.DataFrame({'SecondHighestSalary': unique_salaries[1] }, index=[1] )
    return pd.DataFrame({'SecondHighestSalary': np.nan }, index=[1] )