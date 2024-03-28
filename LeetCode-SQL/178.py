#################### RANK, DENSE_RANK, OVERRIDE #################

                     # PostgreSQL
"""
SELECT score, 
       DENSE_RANK() OVER (ORDER BY score DESC) AS rank 
FROM Scores;
"""
                    # Pandas
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values(by='score', ascending=False)
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    return scores[['score', 'rank']]