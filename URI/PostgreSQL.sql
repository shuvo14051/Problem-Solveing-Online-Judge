URI 2602
SELECT name FROM customers where  state = 'RS';

URI 2603
SELECT name,street FROM customers where city = 'Porto Alegre';

URI 2604
SELECT id,name FROM products where price < 10 or price > 100;

URI 2605

URI 2606
select products.id, products.name from products join categories on products.id_categories =categories.id
where categories.name like '%super%';

URI 2607
select city from providers order by city;

URI 2608
select max(price), min(price) from products;

URI 2607

URI 2607

URI 2607

URI 2607


