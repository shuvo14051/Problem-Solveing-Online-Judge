-- 577 - Employee Bonus
SELECT Employee.name, Bonus.bonus 
FROM Employee 
LEFT OUTER JOIN Bonus ON Employee.empId = Bonus.empId
WHERE Bonus.bonus IS NULL OR Bonus.bonus < 1000;

-- 1075 Project Employees I
select project.project_id, round(avg(employee.experience_years), 2) 
as average_years from project 
join employee on project.employee_id = employee.employee_id
group by project_id
order by project.project_id

