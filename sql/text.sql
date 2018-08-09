/*
Navicat MySQL Data Transfer

Source Server         : 192.168.2.137
Source Server Version : 50505
Source Host           : 192.168.2.137:3306
Source Database       : blog

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2018-07-18 11:35:36
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for text
-- ----------------------------
DROP TABLE IF EXISTS `text`;
CREATE TABLE `text` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `ArticleTitle` varchar(255) DEFAULT NULL,
  `HomeImage` varchar(255) DEFAULT NULL,
  `AllHtml` longtext,
  `WriteHtmlContent` longtext,
  `WriteHtml` longtext,
  `UserID` decimal(28,0) DEFAULT NULL,
  `CreateTime` varchar(30) DEFAULT NULL,
  `ArticleStatus` tinyint(4) DEFAULT NULL,
  `Version` int(11) DEFAULT NULL,
  `HomePage` tinyint(4) DEFAULT NULL,
  `Release` tinyint(4) DEFAULT NULL,
  `AllowComment` tinyint(4) DEFAULT NULL,
  `Top` tinyint(4) DEFAULT NULL,
  `AllowUserVisit` tinyint(4) DEFAULT NULL,
  `AllowPassword` tinyint(4) DEFAULT NULL,
  `Password` varchar(255) DEFAULT NULL,
  `Tag` varchar(255) DEFAULT NULL,
  `Friends` varchar(255) DEFAULT NULL,
  `CategoryID` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
