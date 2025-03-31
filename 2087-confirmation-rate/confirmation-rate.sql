WITH T AS 
(
    SELECT *,
        (
            SELECT COUNT(*)
            FROM Confirmations AS c1
            WHERE c1.user_id = c.user_id AND c1.action = 'confirmed'
        ) AS Confirmed,
        (
            SELECT COUNT(*)
            FROM Confirmations AS c2
            WHERE c2.user_id = c.user_id
        ) AS Total
    FROM Signups AS c
    GROUP BY c.user_id
)
SELECT 
    T.user_id, 
    COALESCE(ROUND(T.Confirmed / NULLIF(T.Total, 0), 2), 0) AS confirmation_rate
FROM T;
