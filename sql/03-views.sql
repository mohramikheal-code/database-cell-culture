USE CellCultureDB;

-- View 1: Active Experiments with Cell Line Details
CREATE VIEW vw_active_experiments AS
SELECT 
    E.ExperimentID,
    E.Title,
    C.LineName,
    E.StartDate
FROM EXPERIMENT E
INNER JOIN CELL_LINE C ON E.CellLineID = C.CellLineID
WHERE E.Status = 'Active';

-- View 2: Contamination Tests Summary
CREATE VIEW vw_contamination_summary AS
SELECT 
    T.TestID,
    T.TestDate,
    T.ContaminantType,
    T.Result,
    P.PassageNumber,
    P.ExperimentID
FROM CONTAMINATION_TEST T
INNER JOIN PASSAGE P ON T.PassageID = P.PassageID;