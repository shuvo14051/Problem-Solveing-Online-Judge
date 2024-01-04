-- URI 2602
SELECT name FROM customers where  state = 'RS';

-- URI 2603
SELECT name,street FROM customers where city = 'Porto Alegre';

-- URI 2604
SELECT id,name FROM products where price < 10 or price > 100;

-- URI 2605
SELECT products.name, providers.name from products
JOIN providers ON products.id_providers = providers.id
JOIN categories on products.id_categories = categories.id
WHERE categories.id = 6

-- URI 2606
select products.id, products.name from products join categories on products.id_categories =categories.id
where categories.name like '%super%';

-- URI 2607
select city from providers order by city;

-- URI 2608
select max(price), min(price) from products;

-- URI 2609
select categories.name, sum(products.amount)  from products 
join categories on products.id_categories = categories.id
GROUP BY categories.name

-- URI 2610
select round(avg(price), 2) as price from products

-- URI 2611
select movies.id, movies.name from movies
join genres on movies.id_genres = genres.id
where genres.description='Action'

-- URI 2613
select movies.id, movies.name from movies
join prices on movies.id_prices = prices.id
where prices.value<2.0

-- URI 2614
select customers.name, rentals.rentals_date from customers 
join rentals on customers.id = rentals.id_customers
where
EXTRACT(YEAR FROM rentals.rentals_date) = 2016
AND EXTRACT(MONTH FROM rentals.rentals_date) = 9;

-- URI 2615
select city from customers

-- URI 2616
SELECT customers.id, customers.name
FROM customers
LEFT JOIN locations ON customers.id = locations.id_customers
WHERE locations.id_customers IS NULL;

-- URI 2617
select products.name, providers.name from providers 
join products on providers.id = products.id_providers
where providers.name='Ajax SA'

-- URI 2618
select products.name, providers.name, categories.name from products 
join providers on products.id_providers = providers.id
join categories on products.id_categories = categories.id
where providers.name='Sansul SA' and categories.name='Imported'

-- URI 2619
select products.name, providers.name, products.price from products 
join providers on products.id_providers = providers.id
join categories on products.id_categories = categories.id
where products.price>1000  and categories.name='Super Luxury'

-- URI 2620
select customers.name, orders.id from customers
join orders on customers.id = orders.id_customers
where 
extract(month from orders.orders_date) <= 6;

-- URI 2621
SELECT products.name 
FROM providers 
JOIN products ON providers.id = products.id_providers
WHERE products.amount BETWEEN 10 AND 20 AND providers.name LIKE 'P%';

-- URI 2622
select customers.name from customers 
join legal_person on customers.id = legal_person.id_customers 
where customers.id=legal_person.id_customers

-- URI 2623
select products.name, categories.name from products
join categories on products.id_categories = categories.id
where products.amount > 100 and categories.id  in (1,2,3,6,9)
order by categories.id

-- URI 2624
select count(DISTINCT city) from customers

-- URI 2625
SELECT 
  CONCAT(
    LEFT(natural_person.cpf::text, 3), '.', 
    SUBSTRING(natural_person.cpf::text, 4, 3), '.', 
    SUBSTRING(natural_person.cpf::text, 7, 3), '-', 
    RIGHT(natural_person.cpf::text, 2)
  ) as CPF 
FROM natural_person
JOIN customers ON natural_person.id_customers = customers.id;

-- URI 2637
SELECT name, customers_number
FROM lawyers
WHERE customers_number = (SELECT MAX(customers_number) FROM lawyers)

UNION ALL

SELECT name, customers_number
FROM lawyers
WHERE customers_number = (SELECT MIN(customers_number) FROM lawyers)

UNION ALL

SELECT 'Average' AS name, ROUND(AVG(customers_number), 0) AS customers_number
FROM lawyers

-- URI 2638

select candidate.name, 
round(((score.math*2+score.specific*3+score.project_plan*5)/10),2) 
as avg from candidate join score
on candidate.id = score.candidate_id
order by (score.math*2+score.specific*3+score.project_plan*5)/10 desc

-- 2139
SELECT name, CAST(extract(day from payday) AS INT) as day FROM loan;

-- 2140

-- 2141
select concat('Approved: ',name), grade from students 
where grade >= 7
order by grade desc

-- 2142

--2743
select name, length(name) from people
order by length(name) desc;

--2744
select id, password, MD5(password) from account

--2745
select name, round(salary*.1,2) from people
where salary > 3000

--2746
select replace(name, 'H1', 'X') from virus;

--2993
SELECT amount AS most_frequent_value
FROM value_table
GROUP BY amount
ORDER BY COUNT(*) DESC
LIMIT 1;

-- 3482


-- 3483
(select city_name, population from cities
order by population desc limit 1 offset 1)

union all

(select city_name, population from cities
order by population asc limit 1 offset 1)

