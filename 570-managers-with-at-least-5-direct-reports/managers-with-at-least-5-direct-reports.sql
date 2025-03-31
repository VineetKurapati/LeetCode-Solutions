WITH T as (SELECT e.*, 
       (SELECT COUNT(*)
        FROM Employee e1
        WHERE e1.managerId = e.id
       ) AS report_count
FROM Employee e
) 
SELECT T.name 
    FROM T 
        WHERE T.report_count >= 5;