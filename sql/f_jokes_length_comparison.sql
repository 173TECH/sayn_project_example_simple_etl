-- this SQL query will be compiled using Jinja
-- the user_prefix parameter is compiled based on the value in the profile used at execution time

SELECT j.joke_type
     , j.translation_type
     , SUM(j.flag_text_translated_length_longer) * 1.0 / COUNT(DISTINCT j.joke_id) AS pct_translated_jokes_text_longer -- * 1.0 to cast to float

FROM {{user_prefix}}f_jokes_stats j

GROUP BY 1, 2
