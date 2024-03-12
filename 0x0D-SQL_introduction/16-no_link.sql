-- lists all records of `second_table`
-- don't list rows without a `name` value
-- result to display score and name (in this order) and listed in descending order of score
SELECT `score`, `name` FROM `second_table` WHERE `name` IS NOT NULL ORDER BY `score` DESC;
