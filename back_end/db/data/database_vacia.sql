-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: localhost    Database: cada_persona_es_un_mundo
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `correlation_experiences`
--

DROP TABLE IF EXISTS `correlation_experiences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `correlation_experiences` (
  `id_exp1` int(11) NOT NULL,
  `id_exp2` int(11) NOT NULL,
  `value` float DEFAULT NULL,
  PRIMARY KEY (`id_exp1`,`id_exp2`),
  KEY `FK_CORRELATION_EXPERIENCE_EXPERIENCES_idx` (`id_exp2`),
  CONSTRAINT `FK_CORRELATION_EXPERIENCE_EXPERIENCES` FOREIGN KEY (`id_exp1`) REFERENCES `experiences` (`id_exp`),
  CONSTRAINT `FK_CORRELATION_EXPERIENCE_EXPERIENCES2` FOREIGN KEY (`id_exp2`) REFERENCES `experiences` (`id_exp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `experiences`
--

DROP TABLE IF EXISTS `experiences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `experiences` (
  `id_exp` int(11) NOT NULL AUTO_INCREMENT,
  `name` longtext,
  `id_type` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_exp`),
  KEY `FK_EXPERIENCIAS_TIPO_EXPERIENCIAS_idx` (`id_type`),
  CONSTRAINT `FK_EXPERIENCES_TYPES_EXPERIENCES` FOREIGN KEY (`id_type`) REFERENCES `types_experiences` (`id_type`)
) ENGINE=InnoDB AUTO_INCREMENT=7961 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `recommendations`
--

DROP TABLE IF EXISTS `recommendations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `recommendations` (
  `id_user` int(11) NOT NULL,
  `id_exp` int(11) NOT NULL,
  `rating` float DEFAULT NULL,
  PRIMARY KEY (`id_user`,`id_exp`),
  KEY `FK_RECOMENDATION_EXPERIENCES_idx` (`id_exp`),
  CONSTRAINT `FK_RECOMENDATION_EXPERIENCES` FOREIGN KEY (`id_exp`) REFERENCES `experiences` (`id_exp`),
  CONSTRAINT `FK_RECOMENDATION_USERS` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `reviews` (
  `id_exp` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `rating` float DEFAULT NULL,
  PRIMARY KEY (`id_exp`,`id_user`),
  KEY `FK_REVIEWS_USERS_idx` (`id_user`),
  CONSTRAINT `FK_REVIEWS_EXPERIENCES` FOREIGN KEY (`id_exp`) REFERENCES `experiences` (`id_exp`),
  CONSTRAINT `FK_REVIEWS_USERS` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `types_experiences`
--

DROP TABLE IF EXISTS `types_experiences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `types_experiences` (
  `id_type` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_type`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `id_user` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_user`)
) ENGINE=InnoDB AUTO_INCREMENT=10860 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-25  9:40:02
