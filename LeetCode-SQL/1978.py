################## Topics covered ################### 
"""
Subquery --> SQL
"""

                                   # PostgreSQL
"""
SELECT employee_id FROM Employees
WHERE salary < 30000 AND manager_id 
NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id;
"""

# Pandas

# Wrong answer
import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    filtered_employees = employees[employees['salary'] < 30000]
    existing_managers = employees['employee_id'].tolist()
    result = filtered_employees[~filtered_employees['manager_id'].isin(existing_managers)]
    output = result[['employee_id']]
    return output