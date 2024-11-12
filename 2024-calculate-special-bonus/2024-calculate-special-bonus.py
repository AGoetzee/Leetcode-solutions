import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    
    BONUS_AMOUNT = 1.0

    # find the requirements
    is_odd = employees['employee_id'] % 2 != 0
    is_notM = ~employees['name'].str.upper().str.startswith('M')
    is_odd_notM = (is_odd & is_notM) # combine using AND operator

    # assign bonuses
    bonus_emps = employees.copy()
    bonus_emps['bonus'] = 0 # create column
    bonus_emps.loc[is_odd_notM,'bonus'] = bonus_emps.loc[is_odd_notM,'salary'] * BONUS_AMOUNT # assign based on requirements
    
    # cleaned up dataframe
    bonus_emps  = bonus_emps.drop(columns=['salary','name']).sort_values(by='employee_id')

    return bonus_emps