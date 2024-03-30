
# song writers table 
CREATE TABLE song_writers (
song_writer_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
username VARCHAR(30) NOT NULL,
f_name VARCHAR(30) NOT NULL,
l_name VARCHAR(30) NOT NULL,
email VARCHAR(50) NOT NULL,
pass VARCHAR(20) NOT NULL
);

# payments table 
CREATE TABLE payments (
payment_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
song_writer_id_fk INT NOT NULL,
song_id_fk INT NOT NULL,
amount DOUBLE NOT NULL,
payment_date DATE NOT NULL,
payment_method VARCHAR(20)
);
# foreign key song writer id 
ALTER TABLE payments
ADD CONSTRAINT
FOREIGN KEY (song_writer_id_fk)
REFERENCES song_writers(song_writer_id)
ON DELETE CASCADE	
ON UPDATE CASCADE;
# foreign key song id 
ALTER TABLE payments
ADD CONSTRAINT
FOREIGN KEY (song_id_fk)
REFERENCES songs(song_id)
ON DELETE CASCADE	
ON UPDATE CASCADE;

# registrations table 
CREATE TABLE registrations (
register_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
song_writer_id_fk INT NOT NULL,
payment_id_fk INT NOT NULL,
song_id_fk INT NOT NULL
);
# foreign key song writer id
ALTER TABLE registrations
ADD CONSTRAINT
FOREIGN KEY (song_writer_id_fk)
REFERENCES song_writers(song_writer_id)
ON DELETE CASCADE	
ON UPDATE CASCADE;
# foreign key payment id
ALTER TABLE registrations
ADD CONSTRAINT
FOREIGN KEY (payment_id_fk)
REFERENCES payments(payment_id)
ON DELETE CASCADE	
ON UPDATE CASCADE;
# foreign key song id
ALTER TABLE registrations
ADD CONSTRAINT
FOREIGN KEY (song_id_fk)
REFERENCES songs(song_id)
ON DELETE CASCADE	
ON UPDATE CASCADE;

# copyright table 
CREATE TABLE copyright_info (
copyright_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
copyright_info TEXT NOT NULL,
register_id_fk INT NOT NULL
);
# foreign key register id
ALTER TABLE copyright_info
ADD CONSTRAINT
FOREIGN KEY (register_id_fk)
REFERENCES registrations(register_id)
ON DELETE CASCADE	
ON UPDATE CASCADE;

# label table 
CREATE TABLE label (
label_id INT PRIMARY KEY NOT NULL,
label_name VARCHAR(20) NOT NULL,
fk_song_id INT NOT NULL,
FOREIGN KEY (fk_song_id)
REFERENCES songs (song_id)
ON DELETE CASCADE
ON UPDATE CASCADE
);

# publisher table 
CREATE TABLE publisher (
publisher_id INT PRIMARY KEY NOT NULL,
first_name VARCHAR(20) NOT NULL,
last_name VARCHAR(20) NOT NULL
);

# song metadata table 
CREATE TABLE song_metadata (
 metadata_id INT PRIMARY KEY NOT NULL,
release_date DATETIME NOT NULL,
duration TIME NOT NULL,
language VARCHAR(20) NOT NULL,
FOREIGN KEY (fk_song_id)
REFERENCES songs (song_id)
ON DELETE CASCADE
ON UPDATE CASCADE
);