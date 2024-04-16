################## Topics covered ################### 
"""
COUNT, DISTINCT, GROUP BY -----> SQL
groupby() nunique() reset_index() ----> Pandas
"""

                        # PostgreSQL
"""
SELECT teacher_id, COUNT(DISTINCT subject_id) as cnt
FROM Teacher 
GROUP BY teacher_id;
"""

                          # Pandas
import pandas as pd
def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    result = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index(name='cnt')
    return result
    