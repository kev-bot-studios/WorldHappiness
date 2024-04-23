CREATE TABLE world_pollution_1.full_report_2023 (
    pRank INT NULL,
    Country VARCHAR(100) NOT NULL,
    Pollution FLOAT NULL,
    pGrowthRate FLOAT NULL,
    LandArea FLOAT NULL,
    pDensity FLOAT NULL,
    Foreign KEY (Country) REFERENCES world_happiness_1.full_report_2023(Country)
);