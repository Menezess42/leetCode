import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    r = pd.merge(employee, employee, left_on='managerId', right_on='id', suffixes=('_employee', '_manager'))
    r = r[r['salary_employee'] > r['salary_manager']]
    r.rename(columns={'name_employee': 'Employee'}, inplace=True)
    return r[['Employee']]
