-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: under_sound_db
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `albums`
--
--

DROP TABLE IF EXISTS `albums`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `albums` (
  `album_id` int NOT NULL AUTO_INCREMENT,
  `artist` int NOT NULL,
  `title` varchar(100) NOT NULL,
  `launch_date` date NOT NULL,
  `cover` text,
  `price` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`album_id`),
  KEY `albums_ibfk_1` (`artist`),
  CONSTRAINT `albums_ibfk_1` FOREIGN KEY (`artist`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `albums`
--

LOCK TABLES `albums` WRITE;
/*!40000 ALTER TABLE `albums` DISABLE KEYS */;
INSERT INTO `albums` VALUES (1,5,'Tribute','2013-10-14','tribute.jpg',9.99),(2,1,'V','2014-08-29','v.jpg',10.99),(3,4,'A Head Full of Dreams','2015-12-04','head_full_dreams.jpg',11.99),(4,3,'Boulevard of Broken Dreams','2004-09-21','broken_dreams.jpg',8.99),(5,1,'Overexposed Track By Track','2012-06-26','overexposed.jpg',9.49),(6,6,'(What\'s The Story) Morning Glory?','1995-10-02','morning_glory.jpg',10.50),(7,2,'Favourite Worst Nightmare','2007-04-23','fwn.jpg',8.75);
/*!40000 ALTER TABLE `albums` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cds`
--

DROP TABLE IF EXISTS `cds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cds` (
  `cd_id` int NOT NULL AUTO_INCREMENT,
  `price` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`cd_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cds`
--

LOCK TABLES `cds` WRITE;
/*!40000 ALTER TABLE `cds` DISABLE KEYS */;
/*!40000 ALTER TABLE `cds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `merchandising`
--

DROP TABLE IF EXISTS `merchandising`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `merchandising` (
  `merchandising_id` int NOT NULL AUTO_INCREMENT,
  `merchandising_type` text NOT NULL,
  `price` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`merchandising_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `merchandising`
--

LOCK TABLES `merchandising` WRITE;
/*!40000 ALTER TABLE `merchandising` DISABLE KEYS */;
/*!40000 ALTER TABLE `merchandising` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plays`
--

DROP TABLE IF EXISTS `plays`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plays` (
  `play_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `song` int NOT NULL,
  `play_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`play_id`),
  KEY `username` (`username`),
  KEY `song` (`song`),
  CONSTRAINT `plays_ibfk_2` FOREIGN KEY (`song`) REFERENCES `songs` (`song_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plays`
--

LOCK TABLES `plays` WRITE;
/*!40000 ALTER TABLE `plays` DISABLE KEYS */;
/*!40000 ALTER TABLE `plays` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchases`
--

DROP TABLE IF EXISTS `purchases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchases` (
  `purchase_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `album` int DEFAULT NULL,
  `song` int DEFAULT NULL,
  `purchase_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `monto_total` decimal(5,2) NOT NULL,
  PRIMARY KEY (`purchase_id`),
  KEY `username` (`username`),
  KEY `album` (`album`),
  KEY `song` (`song`),
  CONSTRAINT `purchases_ibfk_1` FOREIGN KEY (`purchase_id`) REFERENCES `users` (`id`),
  CONSTRAINT `purchases_ibfk_2` FOREIGN KEY (`album`) REFERENCES `albums` (`album_id`),
  CONSTRAINT `purchases_ibfk_3` FOREIGN KEY (`song`) REFERENCES `songs` (`song_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchases`
--

LOCK TABLES `purchases` WRITE;
/*!40000 ALTER TABLE `purchases` DISABLE KEYS */;
/*!40000 ALTER TABLE `purchases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `songs`
--

DROP TABLE IF EXISTS `songs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `songs` (
  `song_id` int NOT NULL AUTO_INCREMENT,
  `artist` int NOT NULL,
  `album` int NOT NULL,
  `title` varchar(100) NOT NULL,
  `duration` time NOT NULL,
  `audio_file` varchar(255) NOT NULL,
  `price` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`song_id`),
  KEY `album` (`album`),
  KEY `songs_ibfk_1` (`artist`),
  CONSTRAINT `songs_ibfk_1` FOREIGN KEY (`artist`) REFERENCES `users` (`id`),
  CONSTRAINT `songs_ibfk_2` FOREIGN KEY (`album`) REFERENCES `albums` (`album_id`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songs`
--

LOCK TABLES `songs` WRITE;
/*!40000 ALTER TABLE `songs` DISABLE KEYS */;
INSERT INTO `songs` VALUES (1,5,1,'Tribute','00:04:10','tribute.mp3',1.29),(2,5,1,'Love Me Again','00:04:00','love_me_again.mp3',1.29),(3,5,1,'Losing Sleep','00:03:42','losing_sleep.mp3',1.29),(4,5,1,'Easy','00:03:40','easy.mp3',1.29),(5,5,1,'Try','00:03:40','try.mp3',1.29),(6,5,1,'Out of My Head','00:03:50','out_of_my_head.mp3',1.29),(7,5,1,'Cheating','00:03:42','cheating.mp3',1.29),(8,5,1,'Running','00:03:40','running.mp3',1.29),(9,5,1,'Gold Dust','00:03:40','gold_dust.mp3',1.29),(10,5,1,'Goodnight Goodbye','00:03:40','goodnight_goodbye.mp3',1.29),(11,5,1,'All I Need Is You','00:03:40','all_i_need_is_you.mp3',1.29),(12,1,2,'Maps','00:03:10','maps.mp3',1.29),(13,1,2,'Animals','00:03:51','animals.mp3',1.29),(14,1,2,'It Was Always You','00:04:00','it_was_always_you.mp3',1.29),(15,1,2,'Unkiss Me','00:03:58','unkiss_me.mp3',1.29),(16,1,2,'Sugar','00:03:55','sugar.mp3',1.29),(17,1,2,'Leaving California','00:03:23','leaving_california.mp3',1.29),(18,1,2,'In Your Pocket','00:03:39','in_your_pocket.mp3',1.29),(19,1,2,'New Love','00:03:16','new_love.mp3',1.29),(20,1,2,'Coming Back for You','00:03:47','coming_back_for_you.mp3',1.29),(21,1,2,'Feelings','00:03:14','feelings.mp3',1.29),(22,1,2,'My Heart Is Open','00:03:57','my_heart_is_open.mp3',1.29),(23,4,3,'A Head Full of Dreams','00:03:44','a_head_full_of_dreams.mp3',1.29),(24,4,3,'Birds','00:03:49','birds.mp3',1.29),(25,4,3,'Hymn for the Weekend','00:04:18','hymn_for_the_weekend.mp3',1.29),(26,4,3,'Everglow','00:04:42','everglow.mp3',1.29),(27,4,3,'Adventure of a Lifetime','00:04:23','adventure_of_a_lifetime.mp3',1.29),(28,4,3,'Fun','00:04:27','fun.mp3',1.29),(29,4,3,'Kaleidoscope','00:01:51','kaleidoscope.mp3',1.29),(30,4,3,'Army of One','00:06:16','army_of_one.mp3',1.29),(31,4,3,'Amazing Day','00:04:27','amazing_day.mp3',1.29),(32,4,3,'Colour Spectrum','00:01:00','colour_spectrum.mp3',1.29),(33,4,3,'Up&Up','00:06:45','up_and_up.mp3',1.29),(34,3,4,'American Idiot','00:02:54','american_idiot.mp3',1.29),(35,3,4,'Jesus of Suburbia','00:09:08','jesus_of_suburbia.mp3',1.29),(36,3,4,'Holiday','00:03:52','holiday.mp3',1.29),(37,3,4,'Boulevard of Broken Dreams','00:04:20','boulevard_of_broken_dreams.mp3',1.29),(38,3,4,'Are We the Waiting','00:02:42','are_we_the_waiting.mp3',1.29),(39,3,4,'St. Jimmy','00:02:55','st_jimmy.mp3',1.29),(40,3,4,'Give Me Novacaine','00:03:25','give_me_novacaine.mp3',1.29),(41,3,4,'She’s a Rebel','00:02:00','shes_a_rebel.mp3',1.29),(42,3,4,'Extraordinary Girl','00:03:33','extraordinary_girl.mp3',1.29),(43,3,4,'Letterbomb','00:04:06','letterbomb.mp3',1.29),(44,3,4,'Wake Me Up When September Ends','00:04:45','wake_me_up_when_september_ends.mp3',1.29),(45,3,4,'Homecoming','00:09:18','homecoming.mp3',1.29),(46,3,4,'Whatsername','00:04:12','whatsername.mp3',1.29),(47,1,5,'One More Night','00:03:39','one_more_night.mp3',1.29),(48,1,5,'Payphone','00:03:51','payphone.mp3',1.29),(49,1,5,'Daylight','00:03:46','daylight.mp3',1.29),(50,1,5,'Lucky Strike','00:03:05','lucky_strike.mp3',1.29),(51,1,5,'The Man Who Never Lied','00:03:25','the_man_who_never_lied.mp3',1.29),(52,1,5,'Love Somebody','00:03:49','love_somebody.mp3',1.29),(53,1,5,'Ladykiller','00:02:45','ladykiller.mp3',1.29),(54,1,5,'Fortune Teller','00:03:23','fortune_teller.mp3',1.29),(55,1,5,'Sad','00:03:14','sad.mp3',1.29),(56,1,5,'Tickets','00:03:29','tickets.mp3',1.29),(57,1,5,'Doin’ Dirt','00:03:32','doin_dirt.mp3',1.29),(58,1,5,'Beautiful Goodbye','00:04:15','beautiful_goodbye.mp3',1.29),(59,6,6,'Hello','00:03:21','hello.mp3',1.29),(60,6,6,'Roll with It','00:03:59','roll_with_it.mp3',1.29),(61,6,6,'Wonderwall','00:04:18','wonderwall.mp3',1.29),(62,6,6,'Don\'t Look Back in Anger','00:04:48','dont_look_back_in_anger.mp3',1.29),(63,6,6,'Hey Now!','00:05:41','hey_now.mp3',1.29),(64,6,6,'The Swamp Song – Excerpt 1','00:00:44','the_swamp_song_excerpt_1.mp3',1.29),(65,6,6,'Some Might Say','00:05:29','some_might_say.mp3',1.29),(66,6,6,'Cast No Shadow','00:04:51','cast_no_shadow.mp3',1.29),(67,6,6,'She\'s Electric','00:03:40','shes_electric.mp3',1.29),(68,6,6,'Morning Glory','00:05:03','morning_glory.mp3',1.29),(69,6,6,'The Swamp Song – Excerpt 2','00:00:39','the_swamp_song_excerpt_2.mp3',1.29),(70,6,6,'Champagne Supernova','00:07:27','champagne_supernova.mp3',1.29),(71,2,7,'Brianstorm','00:02:50','brianstorm.mp3',1.29),(72,2,7,'Teddy Picker','00:02:43','teddy_picker.mp3',1.29),(73,2,7,'D Is for Dangerous','00:02:15','d_is_for_dangerous.mp3',1.29),(74,2,7,'Balaclava','00:02:49','balaclava.mp3',1.29),(75,2,7,'Fluorescent Adolescent','00:03:03','fluorescent_adolescent.mp3',1.29),(76,2,7,'Only Ones Who Know','00:03:04','only_ones_who_know.mp3',1.29),(77,2,7,'Do Me a Favour','00:03:27','do_me_a_favour.mp3',1.29),(78,2,7,'This House Is a Circus','00:03:09','this_house_is_a_circus.mp3',1.29),(79,2,7,'If You Were There, Beware','00:04:34','if_you_were_there_beware.mp3',1.29),(80,2,7,'The Bad Thing','00:02:23','the_bad_thing.mp3',1.29),(81,2,7,'Old Yellow Bricks','00:03:11','old_yellow_bricks.mp3',1.29),(82,2,7,'505','00:04:13','505.mp3',1.29);
/*!40000 ALTER TABLE `songs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `fullname` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `user_type` varchar(50) NOT NULL,
  `password_hash` varchar(50) NOT NULL,
  `signup_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `biography` text,
  `profile_image` text,
  `record` varchar(100) DEFAULT NULL,
  `genre` varchar(100) DEFAULT NULL,
  `birthdate` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  CONSTRAINT `user_type_check` CHECK ((`user_type` in (_utf8mb4'artist',_utf8mb4'customer',_utf8mb4'admin'))),
  CONSTRAINT `users_chk_1` CHECK ((`user_type` in (_utf8mb4'artist',_utf8mb4'customer',_utf8mb4'admin')))
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'artista01','Ana Torres','ana.torres@example.com','artist','hash123','2025-04-14 21:25:56',NULL,NULL,NULL,NULL,'2000-01-01'),(2,'cliente01','Carlos Pérez','carlos.perez@example.com','customer','hash456','2025-04-14 21:25:56',NULL,'https://upload.wikimedia.org/wikipedia/commons/6/66/The_Leaning_Tower_of_Pisa_SB.jpeg',NULL,NULL,'2000-01-01'),(3,'jotaelfuego','Jota \"El Fuego\"','jota.fuego@email.com','artist','hash888','2025-04-15 11:37:19','Directo desde Barcelona, este referente del rap urbano destaca por sus letras cargadas de crítica social y un flow inconfundible.','https://upload.wikimedia.org/wikipedia/commons/3/3a/Bonfire_in_Kladow_17.04.2011_20-41-54.JPG','Barrio Beats Music','Rap conciencia, Hip-Hop','2000-01-01'),(4,'admin01','Laura Gómez','laura.gomez@example.com','admin','hash789','2025-04-14 21:25:56',NULL,NULL,NULL,NULL,'2000-01-01'),(5,'artista02','Luis Rivera','luis.rivera@example.com','artist','hash321','2025-04-14 21:25:56',NULL,NULL,NULL,NULL,'2000-01-01'),(6,'cliente02','Sofía Díaz','sofia.diaz@example.com','customer','hash654','2025-04-14 21:25:56',NULL,NULL,NULL,NULL,'2000-01-01'),(7,'sofiadelmar','Sofía del Mar','sofia.mar@email.com','artist','hash111','2025-04-15 11:37:17','Desde Cádiz, su voz melódica y emotiva ha conquistado escenarios locales con baladas conmovedoras, preparándose para su esperado álbum debut.','https://img.freepik.com/foto-gratis/hermosa-foto-olas-mar_58702-10670.jpg','Melodia Records','Pop melódico con influencias de Flamenco','2000-01-01');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vinyls`
--

DROP TABLE IF EXISTS `vinyls`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vinyls` (
  `vinyl_id` int NOT NULL AUTO_INCREMENT,
  `price` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`vinyl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vinyls`
--

LOCK TABLES `vinyls` WRITE;
/*!40000 ALTER TABLE `vinyls` DISABLE KEYS */;
/*!40000 ALTER TABLE `vinyls` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-15 17:45:52
