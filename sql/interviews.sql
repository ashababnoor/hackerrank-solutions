-- Link: https://www.hackerrank.com/challenges/interviews/problem

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

-------------------------
-- Version 01: Using CTEs
-------------------------

with contests_challenges as (
    select
        l.contest_id
		, l.hacker_id
		, l.name
        , r.challenge_id

    from contests as l
    left join challenges as r
    on l.college_id = r.college_id
)

, contests_all_stats as (
    select
		l.contest_id
		, l.hacker_id
		, l.name
        , l.challenge_id

        , r1.total_submissions
        , r1.total_accepted_submissions
        , r2.total_views
        , r2.total_unique_views
    from contests_challenges as l
	left join submissions_stats as r1
	on l.challenge_id = r1.challenge_id
    left join view_stats as r2
    on l.challenge_id = r2.challenge_id
)

, contests_agg_stats as (
    select
		l.contest_id
		, l.hacker_id
		, l.name

        , sum(r.total_submissions)          as sum_total_submissions
        , sum(r.total_accepted_submission)  as sum_total_accepted_submissions
        , sum(r.total_views)                as sum_total_views
        , sum(r.total_unique_views)         as sum_total_unique_views
    from contests_all_stats as l 
	group by contest_id, hacker_id, name
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

from contests_agg_stats

where 1 = 1
	and sum_total_submissions
        + sum_total_accepted_submissions
        + sum_total_views
        + sum_total_unique_views > 0

order by contest_id;


---------------------------
-- Version 02: Using no CTE
---------------------------

select    
    contest_id
    , hacker_id
    , name
    , sum_total_submissions
    , sum_total_accepted_submissions
    , sum_total_views
    , sum_total_unique_views

from (
    select
        contest_id
        , hacker_id
        , name
        , sum(total_submissions)          as sum_total_submissions
        , sum(total_accepted_submissions) as sum_total_accepted_submissions
        , sum(total_views)                as sum_total_views
        , sum(total_unique_views)         as sum_total_unique_views
    
    from (
        select
            t1.contest_id
            , t1.hacker_id
            , t1.name
            , t1.challenge_id
            , r1.total_submissions
            , r1.total_accepted_submissions
            , r2.total_views
            , r2.total_unique_views

        from (
            select
                con.contest_id
                , con.hacker_id
                , con.name
                , chl.challenge_id

            from colleges col

            left join challenges chl
            on col.college_id = chl.college_id
            
            left join contests con
            on col.contest_id = con.contest_id
        ) as t1

        left join submission_stats as r1
        on t1.challenge_id = r1.challenge_id

        left join view_stats as r2
        on t1.challenge_id = r2.challenge_id
    ) as t2

    group by contest_id, hacker_id, name
) as t3

where 1 = 1
    and not(sum_total_submissions
        + sum_total_accepted_submissions
        + sum_total_views
        + sum_total_unique_views = 0)

order by contest_id;


-------------------------------
-- Version 03: Correct Solution
-------------------------------

SELECT
    con.contest_id
    , con.hacker_id
    , con.name
    , ts.sum_of_total_submissions
    , ts.sum_of_total_accepted_submissions
    , tv.sum_of_total_views
    , tv.sum_of_total_unique_views

FROM contests con

INNER JOIN (
    SELECT
        coll.contest_id
        , SUM(ss.total_submissions) AS sum_of_total_submissions
        , SUM(ss.total_accepted_submissions) AS sum_of_total_accepted_submissions
    
    FROM colleges coll
    
    INNER JOIN
        challenges chall ON chall.college_id = coll.college_id
    INNER JOIN
        submission_stats ss ON ss.challenge_id = chall.challenge_id
    
    GROUP BY coll.contest_id
) ts ON ts.contest_id = con.contest_id

INNER JOIN (
    SELECT
        coll.contest_id
        , SUM(vs.total_views) AS sum_of_total_views
        , SUM(vs.total_unique_views) AS sum_of_total_unique_views
    
    FROM colleges coll
    
    INNER JOIN
        challenges chall ON chall.college_id = coll.college_id
    INNER JOIN
        view_stats vs ON vs.challenge_id = chall.challenge_id
    
    GROUP BY coll.contest_id
) tv ON tv.contest_id = con.contest_id

WHERE
    ts.sum_of_total_submissions > 0
    OR ts.sum_of_total_accepted_submissions > 0
    OR tv.sum_of_total_views > 0
    OR tv.sum_of_total_unique_views > 0

ORDER BY con.contest_id;
