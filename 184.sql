WITH salary_rank AS ( # Creates a temporary virtual table to do queries on it
     SELECT name, departmentId, salary,
     rank() over (partition by departmentId order by salary desc) as sal_rank # creates a rank for departmentId base on the salary from greater to less
     from Employee
)
select d.name as Department, sr.name as Employee, sr.salary
from salary_rank sr join department d
on d.id = sr.departmentId where sal_rank = 1
