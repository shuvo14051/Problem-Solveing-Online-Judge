SELECT 
    current_day.id AS id
FROM 
    Weather AS current_day
JOIN 
    Weather AS previous_day 
ON 
    current_day.recordDate = previous_day.recordDate + INTERVAL '1 day'
WHERE 
    current_day.temperature > previous_day.temperature;