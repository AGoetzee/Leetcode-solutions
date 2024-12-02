import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_salespeople = pd.merge(pd.merge(sales_person, orders, on='sales_id',copy=False),company[company['name'] == 'RED'], on='com_id', how='inner', suffixes=('','_com'))['name'].unique()
    
    return sales_person[~sales_person['name'].isin(red_salespeople)][['name']]
 