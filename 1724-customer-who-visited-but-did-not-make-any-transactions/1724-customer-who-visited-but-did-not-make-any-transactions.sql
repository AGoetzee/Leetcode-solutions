SELECT 
    v.customer_id,
    COUNT(*) AS count_no_trans
FROM 
    Visits v
LEFT JOIN 
    Transactions t 
    ON v.visit_id = t.visit_id
GROUP BY 
    customer_id, t.visit_id
HAVING
    ISNULL(SUM(t.amount));


