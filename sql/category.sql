/*
Navicat MySQL Data Transfer

Source Server         : 192.168.2.137
Source Server Version : 50505
Source Host           : 192.168.2.137:3306
Source Database       : blog

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2018-07-18 11:35:47
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for category
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(255) DEFAULT NULL,
  `Description` varchar(500) DEFAULT NULL,
  `TitleStatus` int(11) DEFAULT NULL,
  `CreateTime` varchar(30) DEFAULT NULL,
  `UserID` decimal(28,0) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
