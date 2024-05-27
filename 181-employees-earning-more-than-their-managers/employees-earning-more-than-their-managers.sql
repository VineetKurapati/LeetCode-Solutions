# Write your MySQL query statement below
SELECT e.name as Employee
FROM Employee e
    JOIN Employee e2
        WHERE e2.id = e.managerId and e.salary > e2.salary