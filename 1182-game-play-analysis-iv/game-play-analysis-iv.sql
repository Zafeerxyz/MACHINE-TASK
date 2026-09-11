-- Write your PostgreSQL query statement below


WITH player_login AS (
SELECT player_id,
event_date,
MIN(event_date) OVER(PARTITION BY player_id) AS first_login FROM activity
)
SELECT ROUND(COUNT(DISTINCT player_id)::NUMERIC/(SELECT COUNT(DISTINCT player_id) FROM Activity),2) AS fraction 
FROM player_login
WHERE event_date = first_login +1