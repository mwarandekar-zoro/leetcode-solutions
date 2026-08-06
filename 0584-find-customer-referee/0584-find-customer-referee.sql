# Write your MySQL query statement below
select a.name
from Customer as c
join Customer as a
on c.id = a.id
where c.referee_id != 2 or a.referee_id IS NULL