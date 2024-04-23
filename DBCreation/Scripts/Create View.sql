USE world_happiness_1;
CREATE VIEW happiness_2023 AS
    SELECT 
        *
    FROM
        world_happiness_1.world_happiness_1_data h
            JOIN
        world_happiness_1.full_report_2023 f USING (Country)
            JOIN
        world_pollution_1.full_report_2023 p USING (Country)
    WHERE
        h.Year = '2023';
