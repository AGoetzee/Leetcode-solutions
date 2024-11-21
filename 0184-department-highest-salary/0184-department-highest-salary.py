import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    max_salary_grouped = employee.groupby('departmentId')['salary'].max().reset_index()
    highest_salaries = employee.merge(max_salary_grouped, on=['departmentId', 'salary'], how='inner')
    highest_salaries['Department'] = highest_salaries['departmentId'].map(department.set_index('id')['name'])
    highest_salaries.rename(columns={'name': 'Employee', 'salary': 'Salary'}, inplace=True)

    return highest_salaries[['Department', 'Employee', 'Salary']]
