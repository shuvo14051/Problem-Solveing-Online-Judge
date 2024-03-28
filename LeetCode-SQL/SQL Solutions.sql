-- ############## LEFT OUTER JOIN #############
-- 577 - Employee Bonus
SELECT Employee.name, Bonus.bonus 
FROM Employee 
LEFT OUTER JOIN Bonus ON Employee.empId = Bonus.empId
WHERE Bonus.bonus IS NULL OR Bonus.bonus < 1000;

-- ############### ROUND, INNER JOIN ###############
-- 1075 Project Employees I
select project.project_id, round(avg(employee.experience_years), 2) 
as average_years from project 
join employee on project.employee_id = employee.employee_id
group by project_id
order by project.project_id

-- ################ COALESCE ###############
-- 176 Second Height Salary
SELECT COALESCE(
    (SELECT DISTINCT salary AS SecondHighestSalary 
     FROM Employee 
     ORDER BY salary DESC 
     OFFSET 1 LIMIT 1), 
    NULL) AS SecondHighestSalary;

-- ################# LEFT JOIN ##############
-- 175 Combile Tables
SELECT person.firstname, person.lastname, address.city, address.state
FROM Person LEFT JOIN Address 
ON person.personid = address.personid;

-- #################### RANK, DENSE_RANK, OVERRIDE #################
-- 178	Rank Scores
                    -- SQL
SELECT score, 
       DENSE_RANK() OVER (ORDER BY score DESC) AS rank 
FROM Scores;
                    -- Pandas
def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values(by='score', ascending=False)
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    return scores[['score', 'rank']]