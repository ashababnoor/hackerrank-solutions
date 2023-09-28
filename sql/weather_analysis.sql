/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/

with base as (
    select 
        month(record_date) as month_
        , record_date
        , data_type
        , data_value
    from temperature_records
)

, intermediate as (
    select
        month_
        , max(if(data_type = "max", data_value, NULL)) max_
        , min(if(data_type = "min", data_value, NULL)) min_
        , round(avg(if(data_type = "avg", data_value, NULL))) avg_
    from base
    group by 1
)

, final as (
    select
        month_ as month
        , max_ as max
        , min_ as min
        , avg_ as avg
    from intermediate
)

select * from final