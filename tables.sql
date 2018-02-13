################
# database ntp #
################


## drop database ##
DROP DATABASE ntp;


CREATE DATABASE IF NOT EXISTS ntp 
CHARACTER SET 'utf8' COLLATE 'utf8_bin';

USE ntp;


CREATE TABLE IF NOT EXISTS udpinfo (
	tid INT AUTO_INCREMENT,
	srcport SMALLINT UNSIGNED DEFAULT 123,
	dstport SMALLINT UNSIGNED NOT NULL,
	length SMALLINT UNSIGNED NOT NULL,
	checksum BIGINT NOT NULL COMMENT 'Display in hexadecimal, Saved by data type: BIGINT.',
	stream INT UNSIGNED NOT NULL,
	PRIMARY KEY (tid),
	KEY ind_srcport (srcport),
	KEY ind_dstport (dstport)
);

## NOTE ##
## we use tid as the tables primary key.

CREATE TABLE IF NOT EXISTS ipinfo (
	tid INT AUTO_INCREMENT,
	version TINYINT DEFAULT 4,
	hdr_len TINYINT UNSIGNED DEFAULT 20,
	dsfield_dscp INT NOT NULL,
	dsfield_ecn INT NOT NULL,
	len SMALLINT UNSIGNED NOT NULL,
	id BIGINT NOT NULL COMMENT 'Display in hexadecimal, Saved by data type: BIGINT.',
	flags_rb TINYINT DEFAULT 0 COMMENT 'reserved bit default 0.',
	flags_df TINYINT NOT NULL COMMENT 'Don\'t fragment flag.',
	flags_mf TINYINT NOT NULL COMMENT 'More fragment flag.',
	frag_offset INT NOT NULL,
	ttl SMALLINT UNSIGNED NOT NULL,
	proto SMALLINT UNSIGNED NOT NULL,
	checksum INT NOT NULL COMMENT 'Display in hexadecimal, checksum is 16 bits.' ,
	src INT UNSIGNED NOT NULL,
	dst INT UNSIGNED NOT NULL,
	PRIMARY KEY (tid),
	KEY ind_id (id),
	KEY ind_src (src),
	KEY ind_dst (dst)
);


CREATE TABLE IF NOT EXISTS ntpinfo (
	tid INT AUTO_INCREMENT,
	priv_flags_r TINYINT UNSIGNED NOT NULL,
	priv_flags_more TINYINT UNSIGNED NOT NULL,
	flags_vn TINYINT UNSIGNED NOT NULL,
	flags_mode TINYINT UNSIGNED NOT NULL,
	priv_auth TINYINT UNSIGNED NOT NULL,
	priv_seq TINYINT UNSIGNED NOT NULL,
	priv_impl TINYINT UNSIGNED NOT NULL,
	priv_reqcode TINYINT UNSIGNED NOT NULL,
	priv_numitems TINYINT UNSIGNED NOT NULL,
	priv_reserved BIGINT NOT NULL COMMENT 'Display in hexadecimal.',
    priv_monlist_itemsize BIGINT NOT NULL COMMENT 'Display in hexadecimal.',
	priv_monlist_avgint INT NOT NULL,
	priv_monlist_lsint INT NOT NULL,
	priv_monlist_restr BIGINT NOT NULL COMMENT 'Display in hexadecimal.',
	priv_monlist_count INT NOT NULL,
	priv_monlist_remote_address INT UNSIGNED NOT NULL,
	priv_monlist_local_address INT UNSIGNED NOT NULL,
	priv_monlist_flags BIGINT NOT NULL COMMENT 'Display in hexadecimal.',
	priv_monlist_port SMALLINT UNSIGNED DEFAULT 123,
	priv_monlist_mode SMALLINT UNSIGNED NOT NULL,
	priv_monlist_version SMALLINT UNSIGNED NOT NULL,
	priv_monlist_ipv6 TINYINT UNSIGNED NOT NULL,
	PRIMARY KEY (tid),
	KEY ind_remote_addr (priv_monlist_remote_address),
	KEY ind_local_addr (priv_monlist_local_address),
	KEY ind_avgint (priv_monlist_avgint),
	KEY ind_lsint (priv_monlist_lsint),
	KEY ind_count (priv_monlist_count),
	CONSTRAINT `FK_ntpinfo_ipinfo_src` FOREIGN KEY (priv_monlist_remote_address) REFERENCES ipinfo (src),
## what is src mean?
	CONSTRAINT `FK_ntpinfo_ipinfo_dst` FOREIGN KEY (priv_monlist_local_address) REFERENCES ipinfo (dst)
);


CREATE TABLE IF NOT EXISTS frameinfo (
	tid INT AUTO_INCREMENT,
	time_delta DEC(16,9) NOT NULL,
	time_delta_displayed DEC(16,9) NOT NULL,
	time_relative DEC(16,9) NOT NULL,
	number INT UNSIGNED NOT NULL,
	len SMALLINT UNSIGNED NOT NULL,
	cap_len SMALLINT UNSIGNED NOT NULL,
	PRIMARY KEY (tid)
);

## NOTE ##
## THIS TABLE NEED TO BE CHANGED.

CREATE TABLE IF NOT EXISTS ethernetinfo (
	tid INT AUTO_INCREMENT,
	src CHAR(17) NOT NULL,
	dst CHAR(17) NOT NULL,
	lg CHAR(3) DEFAULT '0,1',
	ig CHAR(3) DEFAULT '0,0',
	type BIGINT DEFAULT 0x800,
	PRIMARY KEY (tid)
);
