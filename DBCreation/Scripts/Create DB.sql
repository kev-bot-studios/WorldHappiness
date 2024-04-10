-- Example dropping tables if need be
# DROP TABLE world_happiness.world_hapiness_data;

# DROP TABLE world_happiness.full_report_2015;

# Create Schema for Project
CREATE SCHEMA world_happiness;

########################################################
### Create table with all scores and ranks over time ###
########################################################
CREATE TABLE world_happiness.world_happiness_data (
Country VARCHAR(100) NOT NULL,
Year INT NOT NULL,
HappinessIndex Float NULL,
HappinessRank INT NULL,
PRIMARY KEY (Country, Year)
);

########################################################
### Create tables with all scores and ranks over time ###
########################################################

CREATE TABLE world_happiness.full_report_2015 (
Country VARCHAR(100) NOT NULL,
Region VARCHAR(100) NOT NULL,
StandardError Float NULL,
Economy Float NULL,
Family Float NULL,
Health Float NULL,
Freedom Float NULL,
Trust Float NULL,
Generosity Float NULL,
DystopiaResidual Float NULL,
Primary Key (Country)
);

CREATE TABLE world_happiness.full_report_2016 (
Country VARCHAR(100) NOT NULL,
Region VARCHAR(100) NOT NULL,
LowerConfidence Float NULL,
UpperConfidence Float NULL,
Economy Float NULL,
Family Float NULL,
Health Float NULL,
Freedom Float NULL,
Trust Float NULL,
Generosity Float NULL,
DystopiaResidual Float NULL,
Primary Key (Country)
);

CREATE TABLE world_happiness.full_report_2017 (
Country VARCHAR(100) NOT NULL,
LowerConfidence Float NULL,
UpperConfidence Float NULL,
Economy Float NULL,
Family Float NULL,
Health Float NULL,
Freedom Float NULL,
Generosity Float NULL,
Trust Float NULL,
DystopiaResidual Float NULL,
Primary Key (Country)
);

CREATE TABLE world_happiness.full_report_2017 (
Country VARCHAR(100) NOT NULL,
LowerConfidence Float NULL,
UpperConfidence Float NULL,
Economy Float NULL,
Family Float NULL,
Health Float NULL,
Freedom Float NULL,
Generosity Float NULL,
Trust Float NULL,
DystopiaResidual Float NULL,
Primary Key (Country)
);

CREATE TABLE world_happiness.full_report_2018 (
Country VARCHAR(100) NOT NULL,
Economy Float NULL,
Family Float NULL,
Health Float NULL,
Freedom Float NULL,
Generosity Float NULL,
Trust Float NULL,
Primary Key (Country)
);

CREATE TABLE world_happiness.full_report_2019 (
Country VARCHAR(100) NOT NULL,
Economy Float NULL,
Family Float NULL,
Health Float NULL,
Freedom Float NULL,
Generosity Float NULL,
Trust Float NULL,
Primary Key (Country)
);



