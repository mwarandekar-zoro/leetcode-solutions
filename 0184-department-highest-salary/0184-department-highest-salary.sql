# Write your MySQL query statement below
select d.name as Department,
e.name as Employee,
e.salary as Salary
from Employee as e
join Department as d
on e.departmentid = d.id
where (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
)
