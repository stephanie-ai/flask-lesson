DROP TABLE IF EXISTS dogs;

CREATE TABLE dogs (
    id INT NOT NULL,
    name VARCHAR(255),
    breed VARCHAR(255),
    owner VARCHAR(255),
    -- age INTEGER,
    -- weight INTEGER
);

INSERT INTO dogs (id, name, breed, owner) VALUES (1, 'Oscar', 'Labrador', 'Bob');