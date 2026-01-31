import pandas as pd

# < MY SOLUTION>
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['sal_rank'] = employee.groupby('departmentId')['salary'].rank(ascending=False, method='min')
    employee_dept = pd.merge(employee, department, left_on="departmentId", right_on="id", how='left')
    employee_dept_filtered = employee_dept[employee_dept['sal_rank'] == 1]
    employee_dept_filtered.rename(columns={'name_y': 'Department', 'name_x': 'Employee'}, inplace=True)
    return employee_dept_filtered[['Department', 'Employee', 'salary']]



# BEST PERFORMATIC SOLUTION
def department_highest_salary_2(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    data = employee.merge(department, left_on='departmentId', right_on='id')
    data['max_salary'] = data.groupby('name_y')['salary'].transform('max')

    data = data[data['salary'] == data['max_salary']]
    
    data = data[['name_x', 'name_y', 'salary']]
    data.columns = ['Deparment', 'Employee', 'Salary']

    return data
