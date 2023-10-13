-- Occupations
-- Link: https://www.hackerrank.com/challenges/occupations/problem

/*
Enter your query here.
*/
with doctors as (
    select
        name
        , row_number() over(partition by occupation order by name) as row_num
    from occupations
    where occupation = "Doctor"
)

, professors as (
    select
        name
        , row_number() over(partition by occupation order by name) as row_num
    from occupations
    where occupation = "Professor"
)

, singers as (
    select
        name
        , row_number() over(partition by occupation order by name) as row_num
    from occupations
    where occupation = "Singer"
)

, actors as (
    select
        name
        , row_number() over(partition by occupation order by name) as row_num
    from occupations
    where occupation = "Actor"
)

, left_joined as (
    select
        row_num
        , d.name as doctors
        , p.name as professors
        , s.name as singers
        , a.name as actors
    from doctors d
    left join professors p 
    using (row_num)
    left join singers s
    using (row_num)
    left join actors a
    using (row_num)
)

, right_joined as (
    select
        row_num
        , d.name as doctors
        , p.name as professors
        , s.name as singers
        , a.name as actors
    from doctors d
    right join professors p 
    using (row_num)
    right join singers s
    using (row_num)
    right join actors a
    using (row_num)
)

, final_table as (
    select
        *
        , row_number() over(partition by doctors, professors, singers, actors) final_row_num
    from (
        select * from left_joined
        union all
        select * from right_joined
    ) as outer_joined
)

select
    doctors
    , professors
    , singers
    , actors
from final_table
where final_row_num = 1
order by doctors

