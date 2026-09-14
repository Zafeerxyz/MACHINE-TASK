-- Write your PostgreSQL query statement below
select sell_date,
         COUNT(DISTINCT product)num_sold ,
         STRING_AGG(DISTINCT product,',')products
FROM Activities 
GROUP BY sell_date 
ORDER BY sell_date