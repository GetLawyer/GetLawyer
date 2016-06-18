-- MySQL dump 10.13  Distrib 5.5.49, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: GetLawyer
-- ------------------------------------------------------
-- Server version	5.5.49-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clients` (
  `id` int(1) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `email` varchar(80) NOT NULL,
  `password` varchar(80) NOT NULL,
  `city` varchar(40) DEFAULT NULL,
  `statecode` char(2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5195 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

LOCK TABLES `clients` WRITE;
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
INSERT INTO `clients` VALUES (5194,'Skinner, Walter','wskinner@fbi.gov','foxiscrazy','Los Angeles','CA'),(5018,'Scully, Dana','dscully@fbi.gov','sensiblepasswd','New York','NY'),(5169,'Mulder, Spooky','smulder@fbi.gov','2spooky','Aurora','IL'),(5148,'Mulder, Fox','fmulder@fbi.gov','notspooky','New York','NY'),(5111,'Mulder, Samantha','sammulder@alienmail.com','amireal43','Salt Lake City','UT'),(5001,'Man, Smoking','smokingman@redacted.gov','smoking2life','Fairbanks','AK');
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lawyers`
--

DROP TABLE IF EXISTS `lawyers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lawyers` (
  `id` int(1) NOT NULL,
  `name` varchar(80) NOT NULL,
  `organization` varchar(80) DEFAULT NULL,
  `address` varchar(80) DEFAULT NULL,
  `telephone` varchar(15) DEFAULT NULL,
  `email` varchar(80) NOT NULL,
  `area` varchar(80) DEFAULT NULL,
  `bio` varchar(8000) DEFAULT NULL,
  `city` varchar(40) NOT NULL,
  `state` char(2) NOT NULL,
  `license` varchar(40) DEFAULT NULL,
  `password` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lawyers`
--

LOCK TABLES `lawyers` WRITE;
/*!40000 ALTER TABLE `lawyers` DISABLE KEYS */;
INSERT INTO `lawyers` VALUES (8041,'Johnny Ringo','Wild West Firm','5625 N Wilmot Rd Tucson, AZ 85750','1-800-514-9784','wwlawyers.net','Personal Injury','','Tucson','AZ','Degree from the University of Life','ringo1'),(8604,'Ringo Starr','Silver Beetle Lawyers','1 Apple Ln, New York, NY 10001','1-800-814-5199','LaywerHelp.net','Debt,','','New York','NY','Diploma from the School of Hard Knocks','password'),(8741,'Al Capone','Legit-Lawyers Inc.','718 Court St Pekin, IL 61554','1-800-844-8549','gangsterlawyer.com','Debt, Real Estate','','Perkin','IL','Degree from The College for Organized Cr','12345'),(8001,'Bonnie Parker','B&C Lawyers','1330 Nadene Dr Marysville, CA 95901','1-800-948-7448','dontgetsued.com','Debt, DUI, Bankruptcy','','Marysville','CA','Degree from The University of Finance','Clyde4ever');
/*!40000 ALTER TABLE `lawyers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reviews` (
  `id` int(1) NOT NULL AUTO_INCREMENT,
  `clientID` int(1) NOT NULL,
  `lawyerID` int(1) NOT NULL,
  `anonymous` binary(1) NOT NULL,
  `rating` float NOT NULL,
  `title` varchar(80) NOT NULL,
  `content` varchar(8000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1266 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1005,5194,8041,'0',4,'Thank you','Got me decent compensation for gettin\' shot on the job.'),(1068,5001,8604,'0',4.5,'Thanks','Got me out of debt, But I couldnt figure out if he was the walrus or not'),(1154,5111,8001,'0',1,'Thanks a lot','Got me arrested for attempted robbery during our consultory meeting'),(1265,5194,8601,'0',5,'Very Helpful','This lawyer was able to help me very well. Thank you!');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-06-17 11:53:10
