-- Any custom INSERT statements for the pokemon table

INSERT INTO pokemon
    (pokemon_name, pokemon_height, pokemon_weight, pokemon_description)
VALUES
    ('Kabuto', 500, 11500,
    'It is thought to have inhabited beaches 300 million years ago.');

INSERT INTO pokemon_type
    (type_name)
VALUES
    ('Rock');

INSERT INTO pokemon_type
    (type_name)
VALUES
    ('Bug');

INSERT INTO pokemon_type
  (type_name)
VALUES
  ('Fighting'),
  ('Psychic'),
  ('Water'),
  ('Poison');

-- INSERT INTO type_assignment
--     (pokemon_id, type_id)
-- VALUES
--     (1, 1);

-- INSERT INTO type_assignment
--     (pokemon_id, type_id)
-- VALUES
--     (1, 2);

