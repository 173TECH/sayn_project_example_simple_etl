-- this SQL query will be compiled using Jinja
-- the user_prefix parameter is compiled based on the value in the profile used at execution time

SELECT j.id AS joke_id
     , j.type AS joke_type
     , j.text
     , j.text_translated
     , j.translation_type
     , LENGTH(j.text) AS text_length
     , LENGTH(j.text_translated) AS text_translated_length
     , CASE WHEN LENGTH(j.text_translated) > LENGTH(j.text) THEN 1 ELSE 0 END flag_text_translated_length_longer

FROM {{user_prefix}}jokes_translated j
