SELECT 
    p.product_name AS product_name,
    s.year AS year,
    s.price AS price
FROM
    Product AS p
INNER JOIN Sales AS s 
    ON s.product_id=p.product_id;
