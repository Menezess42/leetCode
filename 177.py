import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    e = employee.drop("id", axis=1).drop_duplicates()

    if N > len(e) or N < 1:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    return e.sort_values(['salary'], ascending=False).iloc[[N-1], [0]].rename(columns={"salary":f"getNthHighestSalary({N})"})
