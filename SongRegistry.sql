USE hoa30;
CREATE TABLE IF NOT EXISTS genres (
    genre_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    genre_name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS album (
    album_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    album_title VARCHAR(255) NOT NULL,
    release_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS artist (
    artist_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS publisher (
publisher_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
first_name VARCHAR(20) NOT NULL,
last_name VARCHAR(20) NOT NULL
);
    
CREATE TABLE IF NOT EXISTS song_writers (
song_writer_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
username VARCHAR(30) NOT NULL,
f_name VARCHAR(30) NOT NULL,
l_name VARCHAR(30) NOT NULL,
email VARCHAR(50) NOT NULL,
pass VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS payments (
payment_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
song_writer_id_fk INT NOT NULL,
song_id_fk INT NOT NULL,
amount DOUBLE NOT NULL,
payment_date DATE NOT NULL,
payment_method VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS registrations (
register_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
song_writer_id_fk INT NOT NULL,
payment_id_fk INT NOT NULL,
song_id_fk INT NOT NULL,
copyright_fk INT NOT NULL
);

CREATE TABLE IF NOT EXISTS songs (
    song_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    song_title VARCHAR(255),
    album_id_fk INT,
    artist_id_fk INT NOT NULL,
    genre_id_fk INT,
    publisher_id_fk INT,
    song_writer_id_fk INT NOT NULL);

CREATE TABLE IF NOT EXISTS copyright_info (
copyright_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
copyright_info TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS label (
label_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
label_name VARCHAR(20) NOT NULL,
fk_song_id INT NOT NULL,
FOREIGN KEY (fk_song_id)
REFERENCES songs (song_id)
ON DELETE CASCADE
ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS song_metadata (
metadata_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
release_date DATETIME NOT NULL,
duration TIME NOT NULL,
song_id_fk INT NOT NULL,
language VARCHAR(20) NOT NULL,
FOREIGN KEY (song_id_fk)
REFERENCES songs(song_id)
ON DELETE CASCADE
ON UPDATE CASCADE
);

ALTER TABLE registrations
ADD CONSTRAINT
FOREIGN KEY (song_writer_id_fk)
REFERENCES song_writers(song_writer_id)
ON DELETE CASCADE	
ON UPDATE CASCADE;
ALTER TABLE registrations
ADD CONSTRAINT
FOREIGN KEY (payment_id_fk)
REFERENCES payments(payment_id)
ON DELETE CASCADE	
ON UPDATE CASCADE;
ALTER TABLE payments
ADD CONSTRAINT
FOREIGN KEY (song_writer_id_fk)
REFERENCES song_writers(song_writer_id)
ON DELETE CASCADE	
ON UPDATE CASCADE;
ALTER TABLE payments
ADD CONSTRAINT
FOREIGN KEY (song_id_fk)
REFERENCES songs(song_id)
ON DELETE CASCADE	
ON UPDATE CASCADE;
ALTER TABLE registrations
ADD CONSTRAINT
FOREIGN KEY (copyright_fk)
REFERENCES copyright_info(copyright_id)
ON DELETE CASCADE	
ON UPDATE CASCADE;
ALTER TABLE registrations
ADD CONSTRAINT
FOREIGN KEY (song_id_fk)
REFERENCES songs(song_id)
ON DELETE CASCADE	
ON UPDATE CASCADE;
ALTER TABLE songs
ADD CONSTRAINT
FOREIGN KEY (album_id_fk) REFERENCES album(album_id)
ON DELETE CASCADE
ON UPDATE CASCADE;
ALTER TABLE songs
ADD CONSTRAINT
FOREIGN KEY (artist_id_fk) REFERENCES artist(artist_id)
ON DELETE CASCADE
ON UPDATE CASCADE;
ALTER TABLE songs
ADD CONSTRAINT
FOREIGN KEY (genre_id_fk) REFERENCES genres(genre_id)
ON DELETE CASCADE
ON UPDATE CASCADE;
ALTER TABLE songs
ADD CONSTRAINT
FOREIGN KEY (publisher_id_fk) REFERENCES publisher(publisher_id)
ON DELETE CASCADE
ON UPDATE CASCADE;
ALTER TABLE songs
ADD CONSTRAINT
FOREIGN KEY (song_writer_id_fk) REFERENCES song_writers(song_writer_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

INSERT INTO genres (genre_id, genre_name) VALUES
(1, 'Rock'),
(2, 'Pop'),
(3, 'Hip Hop'),
(4, 'Electronic'),
(5, 'Country');

INSERT INTO album (album_id, album_title, release_date) VALUES
(1, 'Thriller', '1982-11-30'),
(2, 'Abbey Road', '1969-09-26'),
(3, 'Dark Side of the Moon', '1973-03-01'),
(4, 'Back in Black', '1980-07-25'),
(5, 'Rumours', '1977-02-04');

INSERT INTO artist (artist_id, first_name, last_name) VALUES
(1, 'Michael', 'Jackson'),
(2, 'The Beatles', ''),
(3, 'Pink Floyd', ''),
(4, 'AC/DC', ''),
(5, 'Fleetwood Mac', '');

INSERT INTO publisher (publisher_id, first_name, last_name) VALUES
(1, 'John', 'Smith'),
(2, 'Jane', 'Doe'),
(3, 'David', 'Johnson'),
(4, 'Emily', 'Williams'),
(5, 'Chris', 'Brown');

INSERT INTO song_writers (song_writer_id, username, f_name, l_name, email, pass) VALUES
(1, 'user1', 'John', 'Doe', 'john.doe@example.com', 'password1'),
(2, 'user2', 'Jane', 'Smith', 'jane.smith@example.com', 'password2'),
(3, 'user3', 'David', 'Johnson', 'david.johnson@example.com', 'password3'),
(4, 'user4', 'Emily', 'Williams', 'emily.williams@example.com', 'password4'),
(5, 'user5', 'Chris', 'Brown', 'chris.brown@example.com', 'password5');

INSERT INTO songs (song_id, song_title, album_id_fk, artist_id_fk, genre_id_fk, publisher_id_fk, song_writer_id_fk) VALUES
(1, 'Billie Jean', 1, 1, 2, 1, 1),
(2, 'Come Together', 2, 2, 1, 2, 2),
(3, 'Money', 3, 3, 4, 3, 3),
(4, 'Back in Black', 4, 4, 1, 4, 4),
(5, 'Go Your Own Way', 5, 5, 5, 5, 5);

INSERT INTO copyright_info (copyright_id, copyright_info) VALUES
(1, 'Copyright information for song 1'),
(2, 'Copyright information for song 2'),
(3, 'Copyright information for song 3'),
(4, 'Copyright information for song 4'),
(5, 'Copyright information for song 5');

INSERT INTO label (label_id, label_name, fk_song_id) VALUES
(1, 'Epic Records', 1),
(2, 'Apple Records', 2),
(3, 'Harvest Records', 3),
(4, 'Atlantic Records', 4),
(5, 'Warner Bros. Records', 5);

INSERT INTO song_metadata (metadata_id, release_date, duration, song_id_fk, language) VALUES
(1, '1982-01-01 00:00:00', '00:04:54', 1, 'English'),
(2, '1969-01-01 00:00:00', '00:04:20', 2, 'Spanish'),
(3, '1973-01-01 00:00:00', '00:06:22', 3, 'French'),
(4, '1980-01-01 00:00:00', '00:04:15', 4, 'German'),
(5, '1977-01-01 00:00:00', '00:03:43', 5, 'Italian');

INSERT INTO payments (payment_id, song_writer_id_fk, song_id_fk, amount, payment_date, payment_method) VALUES
(1, 1, 1, 1000.00, '2024-03-01', 'Credit Card'),
(2, 2, 2, 1500.00, '2024-03-02', 'PayPal'),
(3, 3, 3, 800.00, '2024-03-03', 'Bank Transfer'),
(4, 4, 4, 1200.00, '2024-03-04', 'Cheque'),
(5, 5, 5, 900.00, '2024-03-05', 'Cash');

INSERT INTO registrations (register_id, song_writer_id_fk, payment_id_fk, song_id_fk, copyright_fk) VALUES
(1, 1, 1, 1,1),
(2, 2, 2, 2,2),
(3, 3, 3, 3,3),
(4, 4, 4, 4,4),
(5, 5, 5, 5,5);

-- Create indexes for frequently searched columns
CREATE INDEX idx_artist_id_fk ON songs (artist_id_fk);
CREATE INDEX idx_genre_id_fk ON songs (genre_id_fk);

-- Create views for frequently joined tables
CREATE VIEW artist_album_view AS
SELECT a.album_title, ar.first_name, ar.last_name
FROM album a
JOIN songs s ON a.album_id = s.album_id_fk
JOIN artist ar ON s.artist_id_fk = ar.artist_id;

CREATE VIEW song_genre_view AS
SELECT s.song_title, g.genre_name
FROM songs s
JOIN genres g ON s.genre_id_fk = g.genre_id;

DELIMITER $$
CREATE PROCEDURE does_transactions()
BEGIN
DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET @do_rollback := 1;
SET autocommit = 0;
SET @do_rollback := 0;
START TRANSACTION;
INSERT INTO album (album_title, release_date) VALUES
('Greetings', '2023-04-11');
INSERT INTO songs (song_title, album_id_fk, artist_id_fk, genre_id_fk, publisher_id_fk, song_writer_id_fk) VALUES
('Hello', 6, 2, 2, 2, 2);
INSERT INTO song_metadata (release_date, duration, song_id_fk, language) VALUES 
('2023-04-11 00:10:00', '00:03:00', 6, 'Spanish');
INSERT INTO payments (song_writer_id_fk, song_id_fk, amount, payment_date, payment_method) VALUES
(2, 6, 350.00, '2024-03-25', 'Credit Card');
INSERT INTO copyright_info (copyright_info)
VALUES ('Copyright information for song 6');
INSERT INTO registrations (song_writer_id_fk, payment_id_fk, copyright_fk) VALUES
(2, LAST_INSERT_ID(), LAST_INSERT_ID());
IF (@do_rollback = 1) THEN
    ROLLBACK;
ELSE
    COMMIT;
END IF;
END $$
-- Prove of Rollback (there should still be 5 records in these tables
SELECT * FROM songs s
JOIN song_metadata sm ON sm.song_id_fk = s.song_id;