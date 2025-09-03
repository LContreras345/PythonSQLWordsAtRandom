
CREATE TABLE IF NOT EXISTS WordList (
	WordID INTEGER PRIMARY KEY,
	WordName TEXT NOT NULL,
	WordType TEXT NOT NULL,
	WordDefinition TEXT
);


INSERT INTO WordList (WordID, WordName, WordType, WordDefinition) VALUES (1, 'Daisy', 'Noun', 'A small European grassland plant which has flowers with a yellow disc and white rays.');
INSERT INTO WordList (WordID, WordName, WordType, WordDefinition) VALUES (2, 'Run', 'Verb', 'To move at a speed faster than a walk.');
INSERT INTO WordList (WordID, WordName, WordType, WordDefinition) VALUES (3, 'Blue', 'Adjective', 'Of a color intermediate between green and violet, as of the sky or sea on a sunny day.');
