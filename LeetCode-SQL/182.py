#################### HAVING, GROUP BY, COUNT #########################

# PostgreSQL
"""
SELECT email from Person
GROUP BY email
HAVING COUNT(*) > 1
"""

# Pandas
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    email_counts = person.groupby('email').size()
    # Selecting emails with count > 1 and converting to DataFrame
    duplicate_emails_df = email_counts[email_counts > 1].reset_index()
    duplicate_emails_df.columns = ['Email', 'Count']  # Renaming columns
    duplicate_emails_df = duplicate_emails_df[['Email']]  # Selecting only 'Email' column

    return duplicate_emails_df