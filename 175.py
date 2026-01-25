import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    new_address = address[['state', 'city', 'personId']]
    new_person = person[['firstName', 'lastName', 'personId']]
    return pd.merge(new_person, new_address, on='personId', how='left').drop(columns=['personId'])
