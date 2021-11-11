
SELECT 
    ids.id,
    Jan_Revenue,
    Feb_Revenue,
    Mar_Revenue,
    Apr_Revenue,
    May_Revenue,
    Jun_Revenue,
    Jul_Revenue,
    Aug_Revenue,
    Sep_Revenue,
    Oct_Revenue,
    Nov_Revenue,
    Dec_Revenue
FROM (
    SELECT id FROM Department GROUP BY id
) as ids
LEFT JOIN (
SELECT id, revenue as Jan_Revenue FROM Department WHERE month = "Jan"
    ) as jan
ON ids.id = jan.id
LEFT JOIN (
    SELECT id, revenue as Feb_Revenue FROM Department WHERE month = "Feb"
    ) as feb
ON ids.id = feb.id
LEFT JOIN (
    SELECT id, revenue as Mar_Revenue FROM Department WHERE month = "Mar"
    ) as mar
ON ids.id = mar.id
LEFT JOIN (
    SELECT id, revenue as Apr_Revenue FROM Department WHERE month = "Apr"
    ) as apr
ON ids.id = apr.id
LEFT JOIN (
    SELECT id, revenue as May_Revenue FROM Department WHERE month = "May"
    ) as may
ON ids.id = may.id
LEFT JOIN (
    SELECT id, revenue as Jun_Revenue FROM Department WHERE month = "Jun"
    ) as jun
ON ids.id = jun.id
LEFT JOIN (
    SELECT id, revenue as Jul_Revenue FROM Department WHERE month = "Jul"
    ) as jul
ON ids.id = jul.id
LEFT JOIN (
    SELECT id, revenue as Aug_Revenue FROM Department WHERE month = "Aug"
    ) as aug
ON ids.id = aug.id
LEFT JOIN (
    SELECT id, revenue as Sep_Revenue FROM Department WHERE month = "Sep"
    ) as sep
ON ids.id = sep.id
LEFT JOIN (
    SELECT id, revenue as Oct_Revenue FROM Department WHERE month = "Oct"
    ) as oct
ON ids.id = oct.id
LEFT JOIN (
    SELECT id, revenue as Nov_Revenue FROM Department WHERE month = "Nov"
    ) as nov
ON ids.id = nov.id
LEFT JOIN (
    SELECT id, revenue as Dec_Revenue FROM Department WHERE month = "Dec"
    ) as dece
ON ids.id = dece.id
