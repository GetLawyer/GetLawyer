# create-db.sql
# Create database and table structure
CREATE DATABASE IF NOT EXISTS GetLawyer;
USE GetLawyer;
CREATE TABLE IF NOT EXISTS `clients` (
    `id`           int(1) NOT NULL auto_increment,
    `name`         varchar(80) NOT NULL,
    `email`        varchar(80) NOT NULL,
    `password`     varchar(80) NOT NULL,
    `city`         varchar(40),
    `statecode`    char(2),
    PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS `lawyers` (
    `id`           int(1) NOT NULL auto_increment,
    `name`         varchar(80) NOT NULL,
    `organization` varchar(80),
    `address`      varchar(80),
    `telephone`    varchar(15),
    `email`        varchar(80) NOT NULL,
    `areas`        varchar(80),
    `bio`          text,
    `city`         varchar(40) NOT NULL,
    `statecode`    char(2) NOT NULL,
    `license`      varchar(80),
    `password`     varchar(80) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS `reviews` (
    `id`           int(1) NOT NULL auto_increment,
    `clientID`     int(1) NOT NULL,
    `lawyerID`     int(1) NOT NULL,
    `anonymous`    binary(1) NOT NULL,
    `rating`       float NOT NULL,
    `title`        varchar(80) NOT NULL,
    `content`      text,
    PRIMARY KEY(`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;
