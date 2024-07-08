--SELECT* FROM sys.databases;  --to show all dbs existing

--CREATE DATABASE world;

CREATE TABLE country (
  Code CHAR(3) NOT NULL DEFAULT '',
  Name VARCHAR(52) NOT NULL DEFAULT '',
  Continent VARCHAR(20) NOT NULL DEFAULT 'Asia',
  Region VARCHAR(26) NOT NULL DEFAULT '',
  SurfaceArea NUMERIC(10,2) NOT NULL DEFAULT 0.00,
  IndepYear SMALLINT DEFAULT NULL,
  Population INT NOT NULL DEFAULT 0,
  LifeExpectancy NUMERIC(3,1) DEFAULT NULL,
  GNP NUMERIC(10,2) DEFAULT NULL,
  GNPOld NUMERIC(10,2) DEFAULT NULL,
  LocalName VARCHAR(45) NOT NULL DEFAULT '',
  GovernmentForm VARCHAR(45) NOT NULL DEFAULT '',
  HeadOfState VARCHAR(60) DEFAULT NULL,
  Capital INT DEFAULT NULL,
  Code2 CHAR(2) NOT NULL DEFAULT '',
  PRIMARY KEY (Code),
  CHECK (Continent IN ('Asia', 'Europe', 'North America', 'Africa', 'Oceania', 'Antarctica', 'South America'))
);


