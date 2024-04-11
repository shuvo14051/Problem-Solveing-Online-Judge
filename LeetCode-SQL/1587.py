#################### JOIN, GROUP BY, HAVING #################

# PostgreSQL
"""
SELECT users.name, sum(Transactions.amount) as balance
FROM users 
JOIN Transactions ON users.account = Transactions.account 
GROUP BY users.name
HAVING sum(Transactions.amount)>10000;
"""

# Pandas
import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(users, transactions, on='account')
    grouped = df.groupby('name').agg({'amount': 'sum'}).reset_index()
    grouped.rename(columns={'amount': 'balance'}, inplace=True)
    result = grouped[grouped['balance'] > 10000]
    return result