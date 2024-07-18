-- Queries related to your pokemon database

SELECT *
FROM pokemon
LIMIT 10;

SELECT pokemon_name, pokemon_height
FROM pokemon
LIMIT 10;

SELECT *
FROM pokemon_type, type_assignment
LIMIT 5;

SELECT pokemon_name
FROM pokemon
ORDER BY pokemon_height DESC
LIMIT 5;

-- Shortest: Joltik, Tallest: Wailord,

SELECT pokemon_name
FROM pokemon
ORDER BY pokemon_weight DESC
LIMIT 5;

-- Heaviest: Groudon, Giratina, Dialga, Metagross, Snorlax

SELECT pokemon_name
FROM pokemon
WHERE pokemon_height > 100 AND pokemon_weight < 10000;

-- Ekans, Gastly, Haunter, Weezing, Dratini, Spinda

SELECT COUNT(*)
FROM pokemon
WHERE pokemon_height = 100 OR pokemon_height = 200;

-- 68 Pokemons are exactly 1m or 2m tall

SELECT pokemon_name
FROM pokemon
WHERE pokemon_weight BETWEEN 10 AND 500;

-- Gastly, Haunter, Hoppip, Rotom, Uxie, Mesprit, Azelf, Tynamo

SELECT pokemon_name, pokemon_height
FROM pokemon
WHERE pokemon_name IN ('Machop', 'Machoke', 'Machamp');

-- Machop = 80, Machoke = 150, Machamp = 160

SELECT pokemon_name
FROM pokemon
WHERE pokemon_name LIKE 'Cha%';

-- Chandelure, Chansey, Charizard, Charmander, Charmeleon, Chatot

SELECT pokemon_name
FROM pokemon
WHERE pokemon_name LIKE '%saur';

-- Bulbasaur, Ivysaur, Venusaur

--Create an SQL query that displays types of the first three pokemon in the type_assignment table.

SELECT type_name
FROM type_assignment AS TA
JOIN pokemon_type AS PT
ON PT.type_id = TA.type_id
LIMIT 3;

-- Grass, Poison, Grass

SELECT P.pokemon_name, type_name
FROM pokemon AS P
JOIN type_assignment AS TA
ON P.pokemon_id = TA.pokemon_id
JOIN pokemon_type AS PT
ON PT.type_id = TA.type_id
LIMIT 10;

SELECT P.pokemon_name, type_name
FROM pokemon AS P
JOIN type_assignment AS TA
ON P.pokemon_id = TA.pokemon_id
JOIN pokemon_type AS PT
ON PT.type_id = TA.type_id
WHERE type_name = 'Fire'
LIMIT 10;

SELECT P.pokemon_name, type_name
FROM pokemon AS P
JOIN type_assignment AS TA
ON P.pokemon_id = TA.pokemon_id
JOIN pokemon_type AS PT
ON PT.type_id = TA.type_id
WHERE type_name = 'Grass'
ORDER BY pokemon_name
LIMIT 10;

SELECT P.pokemon_name, type_name
FROM pokemon AS P
JOIN type_assignment AS TA
ON P.pokemon_id = TA.pokemon_id
JOIN pokemon_type AS PT
ON PT.type_id = TA.type_id
WHERE type_name = 'Ghost'
ORDER BY pokemon_weight
LIMIT 10;

SELECT P.pokemon_name, type_name, pokemon_description
FROM pokemon AS P
JOIN type_assignment AS TA
ON P.pokemon_id = TA.pokemon_id
JOIN pokemon_type AS PT
ON PT.type_id = TA.type_id
WHERE type_name = 'Fighting' AND pokemon_description LIKE '%punch%';

-- Machamp, Hitmonchan, Blaziken, Breloom

SELECT P.*, ARRAY_AGG(type_name) AS type
FROM pokemon AS P
JOIN type_assignment AS TA
ON P.pokemon_id = TA.pokemon_id
JOIN pokemon_type AS T
ON T.type_id = TA.type_id
GROUP BY P.pokemon_id
LIMIT 10;