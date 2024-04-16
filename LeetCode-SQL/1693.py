##################### ORDER BY, GROUP BY ###################

# PostgreSQL
"""
SELECT date_id, make_name, COUNT( distinct lead_id) AS unique_leads,  
COUNT( distinct partner_id) AS unique_partners 
FROM DailySales
GROUP BY date_id, make_name
ORDER BY make_name DESC ;
"""

# Pandas
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    result = daily_sales.groupby(['date_id', 'make_name']).agg(unique_leads=('lead_id', 'nunique'),
                                                          unique_partners=('partner_id', 'nunique')).reset_index()
    result = result.sort_values(by='make_name', ascending=False)
    return result
    
    