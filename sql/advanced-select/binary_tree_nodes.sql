-- Binary Tree Nodes
-- Link: https://www.hackerrank.com/challenges/binary-search-tree-1/problem

with node_list as (
    select 
        distinct n
    from bst
)

, parent_list as (
    select
        distinct p
    from bst
    where p is not null
)

, base_nodes as (
    select
        n as node
        , case
            when p is not null then "leaf or inner"
            when p is null then "root"
        end as leaf_inner_check
        , case
            when n not in (select * from parent_list) then "leaf"
            when n in (select * from parent_list) then "inner or root"
        end as inner_root_check
    from bst
)

, nodes_feature as (
    select
        node
        , case
            when leaf_inner_check = "root" then "Root"
            when inner_root_check = "leaf" then "Leaf"
            when leaf_inner_check = "leaf or inner" and inner_root_check = "inner or root" then "Inner"
        end as node_type
    from base_nodes
)

select
    concat(node, " ", node_type) as output
from nodes_feature
order by node