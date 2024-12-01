import pandas as pd
import time

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # Set indexes for easy joinging
    # Use inplace for memory optimization
    employees.set_index('id', inplace=True)
    employee_uni.set_index('id', inplace=True)

    # Now join the dfs on the index
    # Use a left merge to keep all employee names and fill missing ids with null
    return pd.merge(employees, employee_uni, left_index=True, right_index=True, how='left', copy=False, sort=False)