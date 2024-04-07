-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 164.90.137.194    Database: mfb56
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `album`
--

DROP TABLE IF EXISTS album;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE album (
  album_id int NOT NULL AUTO_INCREMENT,
  album_title varchar(255) NOT NULL,
  release_date date NOT NULL,
  PRIMARY KEY (album_id)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album`
--

LOCK TABLES album WRITE;
/*!40000 ALTER TABLE album DISABLE KEYS */;
INSERT INTO album VALUES (1,'Thriller','1982-11-30'),(2,'Abbey Road','1969-09-26'),(3,'Dark Side of the Moon','1973-03-01'),(4,'Back in Black','1980-07-25'),(5,'Rumours','1977-02-04');
/*!40000 ALTER TABLE album ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artist`
--

DROP TABLE IF EXISTS artist;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE artist (
  artist_id int NOT NULL AUTO_INCREMENT,
  first_name varchar(255) NOT NULL,
  last_name varchar(255) NOT NULL,
  PRIMARY KEY (artist_id)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artist`
--

LOCK TABLES artist WRITE;
/*!40000 ALTER TABLE artist DISABLE KEYS */;
INSERT INTO artist VALUES (1,'Michael','Jackson'),(2,'The Beatles',''),(3,'Pink Floyd',''),(4,'AC/DC',''),(5,'Fleetwood Mac','');
/*!40000 ALTER TABLE artist ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `copyright_info`
--

DROP TABLE IF EXISTS copyright_info;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE copyright_info (
  copyright_id int NOT NULL AUTO_INCREMENT,
  copyright_info text NOT NULL,
  register_id_fk int NOT NULL,
  PRIMARY KEY (copyright_id),
  KEY register_id_fk (register_id_fk),
  CONSTRAINT copyright_info_ibfk_1 FOREIGN KEY (register_id_fk) REFERENCES registrations (register_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `copyright_info`
--

LOCK TABLES copyright_info WRITE;
/*!40000 ALTER TABLE copyright_info DISABLE KEYS */;
/*!40000 ALTER TABLE copyright_info ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genres`
--

DROP TABLE IF EXISTS genres;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE genres (
  genre_id int NOT NULL AUTO_INCREMENT,
  genre_name varchar(255) NOT NULL,
  PRIMARY KEY (genre_id)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genres`
--

LOCK TABLES genres WRITE;
/*!40000 ALTER TABLE genres DISABLE KEYS */;
INSERT INTO genres VALUES (1,'Rock'),(2,'Pop'),(3,'Hip Hop'),(4,'Electronic'),(5,'Country');
/*!40000 ALTER TABLE genres ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `label`
--

DROP TABLE IF EXISTS label;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE label (
  label_id int NOT NULL,
  label_name varchar(20) NOT NULL,
  fk_song_id int NOT NULL,
  PRIMARY KEY (label_id),
  KEY fk_song_id (fk_song_id),
  CONSTRAINT label_ibfk_1 FOREIGN KEY (fk_song_id) REFERENCES songs (song_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `label`
--

LOCK TABLES label WRITE;
/*!40000 ALTER TABLE label DISABLE KEYS */;
/*!40000 ALTER TABLE label ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS payments;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE payments (
  payment_id int NOT NULL AUTO_INCREMENT,
  song_writer_id_fk int NOT NULL,
  song_id_fk int NOT NULL,
  amount double NOT NULL,
  payment_date date NOT NULL,
  payment_method varchar(20) DEFAULT NULL,
  PRIMARY KEY (payment_id),
  KEY song_writer_id_fk (song_writer_id_fk),
  KEY song_id_fk (song_id_fk),
  CONSTRAINT payments_ibfk_1 FOREIGN KEY (song_writer_id_fk) REFERENCES song_writers (song_writer_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT payments_ibfk_2 FOREIGN KEY (song_id_fk) REFERENCES songs (song_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT payments_ibfk_3 FOREIGN KEY (song_writer_id_fk) REFERENCES song_writers (song_writer_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT payments_ibfk_4 FOREIGN KEY (song_id_fk) REFERENCES songs (song_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES payments WRITE;
/*!40000 ALTER TABLE payments DISABLE KEYS */;
/*!40000 ALTER TABLE payments ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `publisher`
--

DROP TABLE IF EXISTS publisher;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE publisher (
  publisher_id int NOT NULL,
  first_name varchar(20) NOT NULL,
  last_name varchar(20) NOT NULL,
  PRIMARY KEY (publisher_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publisher`
--

LOCK TABLES publisher WRITE;
/*!40000 ALTER TABLE publisher DISABLE KEYS */;
INSERT INTO publisher VALUES (1,'John','Smith'),(2,'Jane','Doe'),(3,'David','Johnson'),(4,'Emily','Williams'),(5,'Chris','Brown');
/*!40000 ALTER TABLE publisher ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registrations`
--

DROP TABLE IF EXISTS registrations;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE registrations (
  register_id int NOT NULL AUTO_INCREMENT,
  song_writer_id_fk int NOT NULL,
  payment_id_fk int NOT NULL,
  song_id_fk int NOT NULL,
  fk_copyright_id int DEFAULT NULL,
  PRIMARY KEY (register_id),
  KEY song_writer_id_fk (song_writer_id_fk),
  KEY payment_id_fk (payment_id_fk),
  KEY fk_copyright_id (fk_copyright_id),
  KEY song_id_fk (song_id_fk),
  CONSTRAINT registrations_ibfk_1 FOREIGN KEY (song_writer_id_fk) REFERENCES song_writers (song_writer_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT registrations_ibfk_2 FOREIGN KEY (payment_id_fk) REFERENCES payments (payment_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT registrations_ibfk_3 FOREIGN KEY (song_id_fk) REFERENCES songs (song_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT registrations_ibfk_4 FOREIGN KEY (song_writer_id_fk) REFERENCES song_writers (song_writer_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT registrations_ibfk_5 FOREIGN KEY (payment_id_fk) REFERENCES payments (payment_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT registrations_ibfk_6 FOREIGN KEY (fk_copyright_id) REFERENCES copyright_info (copyright_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT registrations_ibfk_7 FOREIGN KEY (song_id_fk) REFERENCES songs (song_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registrations`
--

LOCK TABLES registrations WRITE;
/*!40000 ALTER TABLE registrations DISABLE KEYS */;
/*!40000 ALTER TABLE registrations ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `song_artist`
--

DROP TABLE IF EXISTS song_artist;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE song_artist (
  fk_song_id int NOT NULL,
  fk_artist_id int NOT NULL,
  PRIMARY KEY (fk_song_id,fk_artist_id),
  KEY fk_artist_id (fk_artist_id),
  CONSTRAINT song_artist_ibfk_1 FOREIGN KEY (fk_song_id) REFERENCES songs (song_id),
  CONSTRAINT song_artist_ibfk_2 FOREIGN KEY (fk_artist_id) REFERENCES artist (artist_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `song_artist`
--

LOCK TABLES song_artist WRITE;
/*!40000 ALTER TABLE song_artist DISABLE KEYS */;
INSERT INTO song_artist VALUES (1,1);
/*!40000 ALTER TABLE song_artist ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `song_metadata`
--

DROP TABLE IF EXISTS song_metadata;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE song_metadata (
  metadata_id int NOT NULL,
  release_date datetime NOT NULL,
  duration time NOT NULL,
  song_language varchar(20) NOT NULL,
  fk_song_id int NOT NULL,
  PRIMARY KEY (metadata_id),
  KEY fk_song_id (fk_song_id),
  CONSTRAINT song_metadata_ibfk_1 FOREIGN KEY (fk_song_id) REFERENCES songs (song_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `song_metadata`
--

LOCK TABLES song_metadata WRITE;
/*!40000 ALTER TABLE song_metadata DISABLE KEYS */;
/*!40000 ALTER TABLE song_metadata ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `song_writers`
--

DROP TABLE IF EXISTS song_writers;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE song_writers (
  song_writer_id int NOT NULL AUTO_INCREMENT,
  username varchar(30) NOT NULL,
  f_name varchar(30) NOT NULL,
  l_name varchar(30) NOT NULL,
  email varchar(50) NOT NULL,
  pass varchar(20) NOT NULL,
  PRIMARY KEY (song_writer_id)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `song_writers`
--

LOCK TABLES song_writers WRITE;
/*!40000 ALTER TABLE song_writers DISABLE KEYS */;
INSERT INTO song_writers VALUES (1,'mubarakfb','Mubarak','Fahad','mubarak@abcd.com','abcd1234');
/*!40000 ALTER TABLE song_writers ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `songs`
--

DROP TABLE IF EXISTS songs;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE songs (
  song_id int NOT NULL AUTO_INCREMENT,
  song_title varchar(255) DEFAULT NULL,
  fk_genre_id int DEFAULT NULL,
  fk_album_id int DEFAULT NULL,
  fk_publisher_id int DEFAULT NULL,
  PRIMARY KEY (song_id),
  KEY fk_genre_id (fk_genre_id),
  KEY fk_album_id (fk_album_id),
  KEY fk_publisher_id (fk_publisher_id),
  CONSTRAINT fk_album_id FOREIGN KEY (fk_album_id) REFERENCES album (album_id),
  CONSTRAINT fk_genre_id FOREIGN KEY (fk_genre_id) REFERENCES genres (genre_id),
  CONSTRAINT fk_publisher_id FOREIGN KEY (fk_publisher_id) REFERENCES publisher (publisher_id)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songs`
--

LOCK TABLES songs WRITE;
/*!40000 ALTER TABLE songs DISABLE KEYS */;
INSERT INTO songs VALUES (1,'Billie Jean',NULL,NULL,NULL),(2,'Come Together',NULL,NULL,NULL),(3,'Money',NULL,NULL,NULL),(4,'Back in Black',NULL,NULL,NULL),(5,'Go Your Own Way',NULL,NULL,NULL);
/*!40000 ALTER TABLE songs ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `songwriters_songs`
--

DROP TABLE IF EXISTS songwriters_songs;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE songwriters_songs (
  fk_songwriter_id int NOT NULL,
  fk_song_id int NOT NULL,
  PRIMARY KEY (fk_songwriter_id,fk_song_id),
  KEY fk_song_id (fk_song_id),
  CONSTRAINT songwriters_songs_ibfk_1 FOREIGN KEY (fk_songwriter_id) REFERENCES song_writers (song_writer_id),
  CONSTRAINT songwriters_songs_ibfk_2 FOREIGN KEY (fk_song_id) REFERENCES songs (song_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songwriters_songs`
--

LOCK TABLES songwriters_songs WRITE;
/*!40000 ALTER TABLE songwriters_songs DISABLE KEYS */;
INSERT INTO songwriters_songs VALUES (1,1);
/*!40000 ALTER TABLE songwriters_songs ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-07  3:51:49
