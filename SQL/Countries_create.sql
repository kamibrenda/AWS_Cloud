-- create tables
CREATE TABLE Countries
(
  code varchar (3) PRIMARY KEY,
  name varchar (50) NOT NULL,
  continent varchar (100) NOT NULL,
  Population integer NOT NULL
);
