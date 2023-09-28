/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/

with base as (
    select 
        event_id
        , participant_name
        , max(score) as score
    from scoretable
    group by 1, 2
)

, intermediate as (
    select
        event_id
        , participant_name
        , score
        , dense_rank() over(partition by event_id order by score desc) as rank_
    from base
)

, final as (
    select
        event_id
        , group_concat(participant_name order by participant_name asc separator ",") as participants
        , rank_
    from intermediate
    where rank_ <=3 
    group by 1, 3
)

, final_first as (
    select *
    from final
    where rank_ = 1
)

, final_second as (
    select *
    from final
    where rank_ = 2
)

, final_third as (
    select *
    from final
    where rank_ = 3
)

, post_final as (
    select
        p1.event_id as event_id
        , p1.participants as first
        , p2.participants as second
        , p3.participants as third
        
    from final_first as p1
    left join final_second as p2
    on p1.event_id = p2.event_id
    left join final_third as p3
    on p1.event_id = p3.event_id
)

select * 
from post_final
order by event_id
