

CREATE TABLE song_writers (
song_writer_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
username VARCHAR(30) NOT NULL,
f_name VARCHAR(30) NOT NULL,
l_name VARCHAR(30) NOT NULL,
email VARCHAR(50) NOT NULL,
pass VARCHAR(20) NOT NULL
);

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

