-- Write your PostgreSQL query statement below
SELECT e.name , b.bonus
FROM Employee e
LEFT JOIN Bonus b
ON e.empID = b.empId
WHERE b.bonus is NULL or b.bonus < 1000