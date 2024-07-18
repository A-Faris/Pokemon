-- All of the SQL commands to create the database, tables and relationships for the Pokemon Database

DROP TABLE pokemon, pokemon_type, type_assignment;

CREATE TABLE pokemon (
    pokemon_id INT GENERATED ALWAYS AS IDENTITY,
    pokemon_name VARCHAR(30) UNIQUE NOT NULL,
    pokemon_height SMALLINT NOT NULL,
    pokemon_weight INT NOT NULL,
    pokemon_description TEXT NOT NULL,
    PRIMARY KEY (pokemon_id)
);

CREATE TABLE pokemon_type (
    type_id INT GENERATED ALWAYS AS IDENTITY,
    type_name VARCHAR(30) UNIQUE NOT NULL,
    PRIMARY KEY (type_id)
);

CREATE TABLE type_assignment (
    type_assignment_id INT GENERATED ALWAYS AS IDENTITY,
    pokemon_id INT NOT NULL,
    type_id INT NOT NULL,
    FOREIGN KEY (pokemon_id) REFERENCES pokemon ON DELETE SET NULL (pokemon_id),
    FOREIGN KEY (type_id) REFERENCES pokemon_type ON DELETE SET NULL (type_id)
);
