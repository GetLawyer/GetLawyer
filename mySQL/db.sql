/*file is for creating our tables and inserting the data*/
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
) ENGINE=MyISAM DEFAULT CHARSET=utf8m4 AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS `lawyers` (
    `id`           int(1) NOT NULL,
    `name`         varchar(80) NOT NULL,
    `organization` varchar(80),
    `address`      varchar(80),
    `telephone`    varchar(15),
    `email`        varchar(80) NOT NULL,
    `area`         varchar(80),
    `bio`          text,
    `city`         varchar(40) NOT NULL,
    `state`        char(2) NOT NULL,
    `password`     varchar(80) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8m4 AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS `reviews` (
    `id`           int(1) NOT NULL auto_increment,
    `client-id`    int(1) NOT NULL,
    `lawyer-id`    int(1) NOT NULL,
    `anonymous`    binary(1) NOT NULL,
    `rating`       float NOT NULL,
    `title`        varchar(80) NOT NULL,
    `content`      varchar(8000),
    PRIMARY KEY(`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8m4 AUTO_INCREMENT=1;
