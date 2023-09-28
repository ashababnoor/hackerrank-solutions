-- Tables: 
--     - contests: contest_id, hacker_id, name
--     - colleges: college_id, contest_id
--     - challenges: college_id, challenge_id
--     - view_stats: challenge_id, total_views, total_unique_views
--     - submission_stats: challenge_id, total_submissions, total_accepted_submissions

-- Output format:
--      contest_id
--      , hacker_id
--      , name
--      , sum: total_submissions
--      , sum: total_accepted_submissions
--      , sum: total_views
--      , sum: total_unique_views

-- Order: contest_id
-- Condition: all four sums cannot be 0

with contests_challenges as (
    select
        l.contest_id
        , r.challenge_id
    from contests as l
    left join challenges as r
    on l.college_id = r.college_id
)

, challenges_all_stats as (
    select
        l.challenge_id
        , l.total_submissions
        , l.total_accepted_submissions
        , r.total_views
        , r.total_unique_views
    from submissions_stats l
    full outer join view_stats r
    on l.challenge_id = r.challenge_id
)

, contests_agg_stats as (
    select
        l.contest_id
        , sum(r.total_submissions)          as sum_total_submissions
        , sum(r.total_accepted_submission)  as sum_total_accepted_submissions
        , sum(r.total_views)                as sum_total_views
        , sum(r.total_unique_views)         as sum_total_unique_views
    from contests_challenges l 
    left join challenges_all_stats r
    using l.challenge_id = r.challenge_id
)

, contests_stats_and_meta as (
    select
        l.contest_id
        , r.hacker_id
        , r.name
        , l.sum_total_submissions
        , l.sum_total_accepted_submissions
        , l.sum_total_views
        , l.sum_total_unique_views
    from contests_agg_stats l 
    inner join contests r 
    on l.contest_id = r.contest_id
)

select
    concat(
        contest_id, " "
        , hacker_id, " "
        , name, " "
        , sum_total_submissions, " "
        , sum_total_accepted_submissions, " "
        , sum_total_views, " "
        , sum_total_unique_views, " "
    ) as output

from contests_stats_and_meta

where 1 = 1
	and sum_total_submissions
        + sum_total_accepted_submissions
        + sum_total_views
        + sum_total_unique_views > 0

order by contest_id