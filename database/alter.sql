-- Any custom update statements for the pokemon table

UPDATE pokemon
SET pokemon_weight = 50
WHERE pokemon_name = 'Kabuto';

DELETE FROM pokemon_type
WHERE type_name = 'Fighting';

-- UPDATE type_assignment
-- SET (pokemon_id, type_id) = (1, 2)
-- WHERE (pokemon_id, type_id) = (1, 5);

UPDATE type_assignment
SET (pokemon_id, type_id) = (1, 5)
WHERE (pokemon_id, type_id) = (1, 2);
