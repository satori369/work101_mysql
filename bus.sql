-- MySQL dump 10.13  Distrib 5.5.27, for Win64 (x86)
--
-- Host: localhost    Database: work101_bus
-- ------------------------------------------------------
-- Server version	5.5.27

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
-- Table structure for table `bus1`
--

DROP TABLE IF EXISTS `bus1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bus1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `chexing` varchar(32) NOT NULL,
  `picibianhao` varchar(32) NOT NULL,
  `VIN` int(10) unsigned DEFAULT NULL,
  `fadongji` int(10) unsigned DEFAULT NULL,
  `yanshoudate` date DEFAULT NULL,
  `fayundate` date DEFAULT NULL,
  `danhao` int(11) DEFAULT NULL,
  `jsdanwei` varchar(64) DEFAULT NULL,
  `danweidizhi` varchar(64) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `tel` decimal(11,0) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bus1`
--

LOCK TABLES `bus1` WRITE;
/*!40000 ALTER TABLE `bus1` DISABLE KEYS */;
INSERT INTO `bus1` VALUES (1,'J2','W2017-01#',123,1234,'2008-10-01','2008-11-01',12345,'123部队','湖北省荆州市','张三',17307160551),(2,'J1','Q2017-01#',456,4567,'2009-10-02','2009-11-02',45678,'123部队','湖北省荆州市','李四',17307160552),(3,'J3','E2017-01#',NULL,NULL,'2010-10-02','2010-11-02',NULL,'456部队','四川省成都市','王五',NULL),(5,'J3','D2017-01#',NULL,NULL,'2012-10-02','2012-11-02',NULL,'110部队','台湾省广岛市','陈七',NULL);
/*!40000 ALTER TABLE `bus1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bus2`
--

DROP TABLE IF EXISTS `bus2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bus2` (
  `序号` int(11) NOT NULL AUTO_INCREMENT,
  `维修时间` date DEFAULT NULL,
  `装备所在单位` varchar(64) DEFAULT NULL,
  `维修地址` varchar(64) DEFAULT NULL,
  `故障现象` varchar(64) DEFAULT NULL,
  `故障原因` varchar(128) DEFAULT NULL,
  `故障排除方式` varchar(32) DEFAULT NULL,
  `设备使用情况` varchar(32) DEFAULT NULL,
  `装备使用频率` varchar(32) DEFAULT NULL,
  `是否经历过大型演习` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`序号`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bus2`
--

LOCK TABLES `bus2` WRITE;
/*!40000 ALTER TABLE `bus2` DISABLE KEYS */;
INSERT INTO `bus2` VALUES (1,'2019-05-10','123部队','湖北省荆州市','无法挂挡',NULL,NULL,NULL,NULL,NULL),(2,'2019-07-05','456部队','四川省成都市','无法着车',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `bus2` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-06  1:05:52
