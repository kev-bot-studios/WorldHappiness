CREATE TABLE world_happiness_1.world_happiness_1_data (
    Country VARCHAR(100) NOT NULL,
    Year INT NOT NULL,
    HappinessIndex FLOAT NULL,
    HappinessRank INT NULL,
    PRIMARY KEY (Country , Year)
);