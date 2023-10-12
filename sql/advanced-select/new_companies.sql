-- New Companies
-- Link: https://www.hackerrank.com/challenges/the-company/problem

/*
Enter your query here.
*/

select
    company_code
    , founder
    , count(distinct lead_manager_code)
    , count(distinct senior_manager_code)
    , count(distinct manager_code)
    , count(distinct employee_code)
from (
    select distinct
        c.company_code
        , c.founder
        , lm.lead_manager_code
        , sm.senior_manager_code
        , m.manager_code
        , e.employee_code
    from 
        company c

        inner join lead_manager lm
        on c.company_code = lm.company_code

        inner join senior_manager sm
        on c.company_code = sm.company_code
        and lm.lead_manager_code = sm.lead_manager_code

        inner join manager m
        on c.company_code = m.company_code
        and lm.lead_manager_code = m.lead_manager_code
        and sm.senior_manager_code = m.senior_manager_code

        inner join employee e
        on c.company_code = e.company_code
        and lm.lead_manager_code = e.lead_manager_code
        and sm.senior_manager_code = e.senior_manager_code
        and m.manager_code = e.manager_code
) as joined_table
group by
    company_code
    , founder