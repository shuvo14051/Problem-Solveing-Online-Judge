####################### ORDER BY, GROUP BY ######################

                    # PostgreSQL
"""
SELECT event_day AS day,  emp_id, SUM(out_time - in_time) AS total_time 
FROM Employees 
GROUP BY emp_id, event_day
ORDER BY emp_id, event_day;
"""

                    # Pandas
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    result = employees.groupby(['event_day', 'emp_id']).sum().reset_index()
    result.rename(columns={'event_day': 'day'}, inplace=True)
    result.sort_values(by=['emp_id', 'day'], inplace=True)
    return result[['total_time', 'day', 'emp_id']]