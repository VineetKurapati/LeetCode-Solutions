WITH T AS (
    SELECT 
        DATE_FORMAT(T1.trans_date, '%Y-%m') AS month, 
        T1.country, 
        (
            SELECT COUNT(*)
            FROM Transactions AS T2
            WHERE 
                (T1.country = T2.country OR (T1.country IS NULL AND T2.country IS NULL))
                AND DATE_FORMAT(T1.trans_date, '%Y-%m') = DATE_FORMAT(T2.trans_date, '%Y-%m')
        ) AS trans_count,
        (
            SELECT COUNT(*)
            FROM Transactions AS T3
            WHERE 
                (T1.country = T3.country OR (T1.country IS NULL AND T3.country IS NULL))
                AND DATE_FORMAT(T1.trans_date, '%Y-%m') = DATE_FORMAT(T3.trans_date, '%Y-%m')
                AND T3.state = 'approved'
        ) AS approved_count, 
        (
            SELECT SUM(T4.amount)
            FROM Transactions AS T4 
            WHERE 
                (T1.country = T4.country OR (T1.country IS NULL AND T4.country IS NULL))
                AND DATE_FORMAT(T1.trans_date, '%Y-%m') = DATE_FORMAT(T4.trans_date, '%Y-%m')
        ) AS trans_total_amount,
        IFNULL((
            SELECT SUM(T5.amount)
            FROM Transactions AS T5 
            WHERE 
                (T1.country = T5.country OR (T1.country IS NULL AND T5.country IS NULL))
                AND DATE_FORMAT(T1.trans_date, '%Y-%m') = DATE_FORMAT(T5.trans_date, '%Y-%m')
                AND T5.state = 'approved'
        ), 0) AS approved_total_amount
    FROM Transactions AS T1
    GROUP BY T1.country, DATE_FORMAT(T1.trans_date, '%Y-%m')
)

SELECT 
    T.month,
    T.country,
    T.trans_count,
    T.approved_count,
    T.trans_total_amount,
    T.approved_total_amount
FROM T;
