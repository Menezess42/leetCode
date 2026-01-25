import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.drop('id', axis=1).sort_values(by='score',  ascending=False)
    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)
    return scores
