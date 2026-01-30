import pandas as pd


# My 1st Hypothesis: < Correct Hypothesis>
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    response = customers[~customers['id'].isin(orders['customerId'])]
    response = response.drop(columns='id').rename(columns={"name": "Customers"})
    return response

# More Performatic Code
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    cond = ~customers['id'].isin(orders['customerId'])
    return customers.loc[cond, ["name"]].rename(columns={"name": "Customers"})



