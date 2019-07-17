CREATE DATABASE  IF NOT EXISTS `discoteca` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `discoteca`;
-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: localhost    Database: discoteca
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
-- Table structure for table `cantantes`
--

DROP TABLE IF EXISTS `cantantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `cantantes` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cantantes`
--

LOCK TABLES `cantantes` WRITE;
/*!40000 ALTER TABLE `cantantes` DISABLE KEYS */;
INSERT INTO `cantantes` VALUES (1,'Andrea Bocelli'),(2,'Mago de Oz'),(3,'Queen'),(4,'Sonata Arctica'),(5,'Nightwish'),(6,'Cafe Quijano'),(7,'David Gueta'),(8,'Kid Cudi');
/*!40000 ALTER TABLE `cantantes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cds`
--

DROP TABLE IF EXISTS `cds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `cds` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `anyo` date NOT NULL,
  `idIdioma` int(10) NOT NULL,
  `idDiscografica` int(10) NOT NULL,
  `idcomprador` int(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_cds-compradores_idx` (`idcomprador`),
  KEY `FK_cds-idiomas_idx` (`idIdioma`),
  KEY `FK_cds-discograficas_idx` (`idDiscografica`),
  CONSTRAINT `FK_cds-compradores` FOREIGN KEY (`idcomprador`) REFERENCES `compradores` (`id`),
  CONSTRAINT `FK_cds-discograficas` FOREIGN KEY (`idDiscografica`) REFERENCES `discograficas` (`id`),
  CONSTRAINT `FK_cds-idiomas` FOREIGN KEY (`idIdioma`) REFERENCES `idiomas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cds`
--

LOCK TABLES `cds` WRITE;
/*!40000 ALTER TABLE `cds` DISABLE KEYS */;
INSERT INTO `cds` VALUES (1,'Wishmaster','2000-05-08',2,3,1),(2,'Endless Forms Most Beautiful','2016-05-27',2,3,2),(3,'Brocelli','1995-11-13',3,5,3),(4,'Gaia','2003-12-06',1,2,4),(5,'Gaia II: La voz dormida','2005-11-14',1,2,5),(6,'Gaia III: Atlantia','2010-04-06',1,2,1),(7,'Gaia: Epílogo','2010-11-30',1,2,2),(8,'A Night at the Opera','1975-11-21',2,4,3),(9,'The Works','1984-02-27',2,4,4),(10,'Ecliptica','1999-11-22',2,6,4),(11,'Stones Grow Her Name','2012-05-18',2,3,1),(12,'La taberna del buda','2001-11-01',1,2,2),(13,'Disco prohibido','2019-06-12',1,1,3),(14,'Disco CasiProhibido','2019-06-12',1,2,5),(15,'Dico SemiProhibido','2019-06-12',1,3,1);
/*!40000 ALTER TABLE `cds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cds_cantantes`
--

DROP TABLE IF EXISTS `cds_cantantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `cds_cantantes` (
  `id_cds` int(10) NOT NULL,
  `id_cantantes` int(10) NOT NULL,
  PRIMARY KEY (`id_cds`,`id_cantantes`),
  KEY `FK_cds_cantantes-cantantes_idx` (`id_cantantes`),
  CONSTRAINT `FK_cds_cantantes-cantantes` FOREIGN KEY (`id_cantantes`) REFERENCES `cantantes` (`id`),
  CONSTRAINT `FK_cds_cantantes-cds` FOREIGN KEY (`id_cds`) REFERENCES `cds` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cds_cantantes`
--

LOCK TABLES `cds_cantantes` WRITE;
/*!40000 ALTER TABLE `cds_cantantes` DISABLE KEYS */;
INSERT INTO `cds_cantantes` VALUES (3,1),(4,2),(5,2),(6,2),(7,2),(8,3),(9,3),(10,4),(11,4),(1,5),(2,5),(12,6),(13,7),(14,7),(13,8),(15,8);
/*!40000 ALTER TABLE `cds_cantantes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cds_generos`
--

DROP TABLE IF EXISTS `cds_generos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `cds_generos` (
  `idCD` int(10) NOT NULL,
  `idGenero` int(10) NOT NULL,
  PRIMARY KEY (`idCD`,`idGenero`),
  KEY `FK_cds_cantantes-cantantes_idx` (`idGenero`),
  CONSTRAINT `FK_cds_generos-cds` FOREIGN KEY (`idCD`) REFERENCES `cds` (`id`),
  CONSTRAINT `FK_cds_generos-generos` FOREIGN KEY (`idGenero`) REFERENCES `generos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cds_generos`
--

LOCK TABLES `cds_generos` WRITE;
/*!40000 ALTER TABLE `cds_generos` DISABLE KEYS */;
INSERT INTO `cds_generos` VALUES (12,1),(13,1),(14,1),(15,1),(4,2),(5,2),(6,2),(7,2),(8,2),(9,2),(12,2),(1,3),(2,3),(6,3),(8,3),(10,3),(11,3),(3,4),(5,5),(6,5),(7,5),(8,5);
/*!40000 ALTER TABLE `cds_generos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compradores`
--

DROP TABLE IF EXISTS `compradores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `compradores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compradores`
--

LOCK TABLES `compradores` WRITE;
/*!40000 ALTER TABLE `compradores` DISABLE KEYS */;
INSERT INTO `compradores` VALUES (1,'Yo'),(2,'Mama'),(3,'Papa'),(4,'Amigo invisible'),(5,'Robado');
/*!40000 ALTER TABLE `compradores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discograficas`
--

DROP TABLE IF EXISTS `discograficas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `discograficas` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discograficas`
--

LOCK TABLES `discograficas` WRITE;
/*!40000 ALTER TABLE `discograficas` DISABLE KEYS */;
INSERT INTO `discograficas` VALUES (1,'Sony'),(2,'Warner'),(3,'Nuclear Records'),(4,'EMI'),(5,'Polydor Records'),(6,'Spinefarm Records');
/*!40000 ALTER TABLE `discograficas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `generos`
--

DROP TABLE IF EXISTS `generos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `generos` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generos`
--

LOCK TABLES `generos` WRITE;
/*!40000 ALTER TABLE `generos` DISABLE KEYS */;
INSERT INTO `generos` VALUES (1,'Pop'),(2,'Rock'),(3,'Metal Sinfonico'),(4,'Crossover'),(5,'Folk Metal'),(8,'Rap'),(10,'Swing');
/*!40000 ALTER TABLE `generos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `idiomas`
--

DROP TABLE IF EXISTS `idiomas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `idiomas` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `idiomas`
--

LOCK TABLES `idiomas` WRITE;
/*!40000 ALTER TABLE `idiomas` DISABLE KEYS */;
INSERT INTO `idiomas` VALUES (1,'Espanyol'),(2,'Ingles'),(3,'Italiano');
/*!40000 ALTER TABLE `idiomas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-14 13:33:36
