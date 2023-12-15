




003 - Revising the Select Query II
SELECT NAME FROM CITY WHERE POPULATION > 120000 and COUNTRYCODE = 'USA';

004 - Select By ID
SELECT * FROM CITY WHERE ID = 1661;

005 - Japanese Cities Attributes
SELECT * FROM CITY WHERE COUNTRYCODE = 'JPN';

006 - Japanese Cities Names
SELECT NAME FROM CITY WHERE  COUNTRYCODE = 'JPN';

007 - Weather Observation Station 1
SELECT CITY, STATE  FROM STATION;

008 - Weather Observation Station 3
SELECT COUNT(CITY) - DISTINCT(CITY) FROM STATION WHERE  mod(ID, 2) = 0;

009 - Weather Observation Station 4
SELECT COUNT(CITY) - COUNT(DISTINCT(CITY)) FROM STATION;

010 - Weather Observation Station 5
SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY), CITY LIMIT 1;
SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY) DESC, CITY LIMIT 1;

011 - Weather Observation Station 6
SELECT DISTINCT (CITY) FROM STATION WHERE SUBSTRING(CITY,1,1) IN ('A','E','I','O','U','a', 'e', 'i', 'o', 'u');

012 - Weather Observation Station 7
SELECT DISTINCT (CITY) FROM STATION WHERE RIGHT(CITY,1) IN ('A','E','I','O','U','a', 'e', 'i', 'o', 'u');


013 - Weather Observation Station 8
SELECT DISTINCT (CITY) FROM STATION WHERE RIGHT(CITY,1) IN ('A','E','I','O','U','a', 'e', 'i', 'o', 'u')
AND SUBSTRING(CITY,1,1) IN ('A','E','I','O','U','a', 'e', 'i', 'o', 'u');


014 - Weather Observation Station 9
SELECT DISTINCT (CITY) FROM STATION WHERE SUBSTRING(CITY,1,1) NOT IN ('A','E','I','O','U','a', 'e', 'i', 'o', 'u');

015 - Weather Observation Station 10
SELECT DISTINCT (CITY) FROM STATION WHERE RIGHT(CITY,1) NOT IN ('A','E','I','O','U','a', 'e', 'i', 'o', 'u');

016 - Weather Observation Station 11
SELECT DISTINCT (CITY) FROM STATION WHERE RIGHT(CITY,1) NOT IN ('A','E','I','O','U','a', 'e', 'i', 'o', 'u')
OR SUBSTRING(CITY,1,1) NOT IN ('A','E','I','O','U','a', 'e', 'i', 'o', 'u');

017 - Weather Observation Station 12
SELECT DISTINCT (CITY) FROM STATION WHERE RIGHT(CITY,1) NOT IN ('A','E','I','O','U','a', 'e', 'i', 'o', 'u')
AND SUBSTRING(CITY,1,1) NOT IN ('A','E','I','O','U','a', 'e', 'i', 'o', 'u');

018 - Higher Than 75 Marks
SELECT NAME FROM STUDENTS WHERE MARKS > 75 ORDER BY RIGHT(NAME, 3), ID ASC;

019 - Employee Names
SELECT NAME FROM EMPLOYEE ORDER BY NAME;

020 - Employee Salaries
SELECT NAME FROM EMPLOYEE WHERE SALARY > 2000 AND MONTHS < 10 ORDER BY employee_id;

021 - Revising Aggregations - The Count Function
SELECT COUNT(NAME) FROM CITY WHERE POPULATION > 100000;

022 - Revising Aggregations - The Sum Function
SELECT SUM(POPULATION) FROM CITY WHERE DISTRICT = 'California';

023 - Revising Aggregations - Averages
SELECT AVG(POPULATION) FROM CITY WHERE DISTRICT = 'California';

024 - Average Population
SELECT ROUND(AVG(POPULATION)) FROM CITY;

025 - Japan Population
SELECT SUM(POPULATION) FROM CITY WHERE COUNTRYCODE = 'JPN';

026 - Population Density Difference
SELECT MAX(POPULATION) - MIN(POPULATION) FROM CITY;


