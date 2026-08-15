USE CellCultureDB;

-- Query 1: Filter & Order
SELECT * FROM CELL_LINE WHERE BiosafetyLevel = 2 ORDER BY LineName ASC;

-- Query 2: LIKE Filtering
SELECT * FROM RESEARCHER WHERE LastName LIKE 'F%' OR LastName LIKE 'M%';

-- Query 3: Grouping & Having
SELECT CellLineID, SUM(VialCount) AS TotalVials
FROM CRYOSTOCK
GROUP BY CellLineID
HAVING SUM(VialCount) > 10;

-- Query 4: Multi-Table JOIN
SELECT E.ExperimentID, E.Title, R.FirstName, R.LastName, ER.Role
FROM EXPERIMENT E
JOIN EXPERIMENT_RESEARCHER ER ON E.ExperimentID = ER.ExperimentID
JOIN RESEARCHER R ON ER.ResearcherID = R.ResearcherID;

-- Query 5: Subquery with IN
SELECT FirstName, LastName, EmailAddress
FROM RESEARCHER
WHERE ResearcherID IN (
    SELECT ResearcherID FROM EXPERIMENT_RESEARCHER
);

-- Query 6: Test Views & Stored Procedure
SELECT * FROM vw_active_experiments;
SELECT * FROM vw_contamination_summary;
CALL sp_GetActiveExperimentsByCellLine(1);

-- Query 7: INSERT
-- Uses a new identifier so the operation can be demonstrated on the supplied test data.
INSERT INTO INCUBATOR (IncubatorID, Model, Location, Temperature, CO2Percentage)
VALUES (11, 'Test Incubator', 'Room 106', 37.0, 5.0);

-- Query 8: UPDATE
UPDATE INCUBATOR SET Temperature = 37.2 WHERE IncubatorID = 1;

-- Query 9: DELETE
DELETE FROM CONTAMINATION_TEST WHERE TestID = 10;