-- Example dropping tables if need be
# DROP TABLE world_happiness.world_hapiness_data;

# DROP TABLE world_happiness.full_report_2020;

# Create Schema for Project
CREATE SCHEMA world_happiness_1;
CREATE SCHEMA world_pollution_1;

########################################################
CREATE TABLE world_happiness_table1.world_happiness_1_data (
    Country VARCHAR(100) NOT NULL,
    Year INT NOT NULL,
    HappinessIndex FLOAT NULL,
    HappinessRank INT NULL,
    PRIMARY KEY (Country , Year)
);
CREATE TABLE world_happiness_1.full_report_2020 (
    Country VARCHAR(100) NOT NULL,
    LadderScore FLOAT NULL,
    StandardError FLOAT NULL,
    Economy FLOAT NULL,
    Family FLOAT NULL,
    Health FLOAT NULL,
    Freedom FLOAT NULL,
    Generosity FLOAT NULL,
    Trust FLOAT NULL,
    DystopiaResidual FLOAT NULL,
    PRIMARY KEY (Country)
);

CREATE TABLE world_happiness_1.full_report_2021 (
    Country VARCHAR(100) NOT NULL,
    LadderScore FLOAT NULL,
    UpperWhisker FLOAT NULL,
    LowerWhisker FLOAT NULL,
    Economy FLOAT NULL,
    Family FLOAT NULL,
    Health FLOAT NULL,
    Freedom FLOAT NULL,
    Generosity FLOAT NULL,
    Trust FLOAT NULL,
    DystopiaResidual FLOAT NULL,
    PRIMARY KEY (Country)
);


CREATE TABLE world_happiness_1.full_report_2022 (
    Ranking INT NULL,
    Country VARCHAR(100) NOT NULL,
    HappinessScore FLOAT NULL,
    LowerWhisker FLOAT NULL,
    UpperWhisker FLOAT NULL,
    Economy FLOAT NULL,
    Family FLOAT NULL,
    Health FLOAT NULL,
    Freedom FLOAT NULL,
    Generosity FLOAT NULL,
    Trust FLOAT NULL,
    DystopiaResidual FLOAT NULL,
    PRIMARY KEY (Country)
);

CREATE TABLE world_happiness_1.full_report_2023 (
    Country VARCHAR(100) NOT NULL,
    LadderScore FLOAT NULL,
    UpperWhisker FLOAT NULL,
    LowerWhisker FLOAT NULL,
    Economy FLOAT NULL,
    Family FLOAT NULL,
    Health FLOAT NULL,
    Freedom FLOAT NULL,
    Generosity FLOAT NULL,
    Trust FLOAT NULL,
    PRIMARY KEY (Country)
);

CREATE TABLE world_pollution_1.full_report_2023 (
    pRank INT NULL,
    Country VARCHAR(100) NOT NULL,
    Pollution FLOAT NULL,
    pGrowthRate FLOAT NULL,
    LandArea FLOAT NULL,
    pDensity FLOAT NULL,
    PRIMARY KEY (Country)
);

CREATE TABLE world_happiness_1.index_2013_2023 (
    Ranking INT NULL,
    Country VARCHAR(100) NOT NULL,
    Year INT NOT NULL,
    HappinessIndex FLOAT NULL,
    PRIMARY KEY (Country , Year)
);



