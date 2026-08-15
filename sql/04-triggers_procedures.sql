USE CellCultureDB;

-- Stored Procedure: Get all active experiments for a specific Cell Line
DELIMITER //
CREATE PROCEDURE sp_GetActiveExperimentsByCellLine(IN p_CellLineID INT)
BEGIN
    SELECT E.ExperimentID, E.Title, E.StartDate, E.Status
    FROM EXPERIMENT E
    WHERE E.CellLineID = p_CellLineID AND E.Status = 'Active';
END //
DELIMITER ;

-- Trigger: Validate Cryostock Vial Count on INSERT to ensure non-negative quantity
DELIMITER //
CREATE TRIGGER trg_check_cryostock_vials
BEFORE INSERT ON CRYOSTOCK
FOR EACH ROW
BEGIN
    IF NEW.VialCount < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Vial count cannot be negative.';
    END IF;
END //
DELIMITER ;