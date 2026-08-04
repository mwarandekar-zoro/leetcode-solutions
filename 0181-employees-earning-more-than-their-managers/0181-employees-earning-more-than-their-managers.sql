# Write your MySQL query statement below
select e.name as employee
from Employee as e
left join Employee as m
on e.managerId = m.Id
where e.salary > m.salary;