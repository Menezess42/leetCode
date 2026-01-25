import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['fst_next_num'] = logs['num'].shift(1)
    logs['scnd_next_num'] = logs['num'].shift(2)
    final  = logs[(logs['num'] == logs['fst_next_num']) & (logs['num'] == logs['scnd_next_num'])]
    final = final[['num']].drop_duplicates().rename(columns={"num": "ConsecutiveNums"})
    return final
