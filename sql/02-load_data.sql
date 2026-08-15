USE CellCultureDB;

INSERT INTO RESEARCHER VALUES
(1, 'Mohamed', 'Fahmy', 'm.fahmy@lab.edu', '01001111111'),
(2, 'Aya', 'Mohamed', 'a.mohamed@lab.edu', '01002222222'),
(3, 'Alaa', 'Fahmy', 'a.fahmy@lab.edu', '01003333333'),
(4, 'Wafaa', 'Kahky', 'w.kahky@lab.edu', '01004444444'),
(5, 'Samir', 'Khaled', 's.khaled@lab.edu', '01005555555'),
(6, 'Hussam', 'Ali', 'h.ali@lab.edu', '01006666666'),
(7, 'Ayman', 'Hassan', 'a.hassan@lab.edu', '01007777777'),
(8, 'Amany', 'Said', 'a.said@lab.edu', '01008888888'),
(9, 'Ahmed', 'Ibrahim', 'a.ibrahim@lab.edu', '01009999999'),
(10, 'Mona', 'Zaki', 'm.zaki@lab.edu', '01010000000');

INSERT INTO INCUBATOR VALUES
(1, 'Thermo Forma 310', 'Room 101', 37.0, 5.0),
(2, 'Eppendorf CellXpert', 'Room 101', 37.0, 5.0),
(3, 'Binder C150', 'Room 102', 36.5, 5.0),
(4, 'PHCbi MCO-170', 'Room 102', 37.0, 5.5),
(5, 'Memmert ICO50', 'Room 103', 37.0, 5.0),
(6, 'Thermo Heracell 150', 'Room 103', 37.0, 5.0),
(7, 'Esco CelCulture', 'Room 104', 37.5, 5.0),
(8, 'Bionex Incu', 'Room 104', 37.0, 4.5),
(9, 'Labocon CO2-100', 'Room 105', 37.0, 5.0),
(10, 'Sheldon XL', 'Room 105', 38.0, 6.0);

INSERT INTO MEDIA VALUES
(1, 'DMEM High Glucose', 'FBS 10%', 'BATCH-001', '2026-12-31'),
(2, 'RPMI-1640', 'FBS 10%', 'BATCH-002', '2026-11-30'),
(3, 'EMEM', 'FBS 5%', 'BATCH-003', '2026-10-15'),
(4, 'F-12K Medium', 'FBS 10%', 'BATCH-004', '2026-09-20'),
(5, 'IMDM', 'FBS 20%', 'BATCH-005', '2027-01-15'),
(6, 'McCoy 5A', 'FBS 10%', 'BATCH-006', '2026-08-10'),
(7, 'Leibovitz L-15', 'None', 'BATCH-007', '2026-07-01'),
(8, 'DMEM/F12', 'FBS 10%', 'BATCH-008', '2027-02-28'),
(9, 'Ham F-12', 'FBS 10%', 'BATCH-009', '2026-06-30'),
(10, 'Opti-MEM', 'Reduced Serum', 'BATCH-010', '2027-03-31');

INSERT INTO CELL_LINE VALUES
(1, 'HeLa', 'Human', 'Cervix', 2),
(2, 'HEK293', 'Human', 'Kidney', 2),
(3, 'CHO-K1', 'Hamster', 'Ovary', 1),
(4, 'MCF-7', 'Human', 'Breast', 1),
(5, 'A549', 'Human', 'Lung', 2),
(6, 'NIH/3T3', 'Mouse', 'Embryo', 1),
(7, 'COS-7', 'Monkey', 'Kidney', 2),
(8, 'HepG2', 'Human', 'Liver', 2),
(9, 'RAW 264.7', 'Mouse', 'Macrophage', 2),
(10, 'Jurkat', 'Human', 'T-lymphocyte', 2);

INSERT INTO EXPERIMENT VALUES
(1, 'Gene Expression Assay A', '2026-01-10', 'Active', 1),
(2, 'Toxicity Test B', '2026-01-15', 'Active', 2),
(3, 'Protein Yield Optimization', '2026-02-01', 'Completed', 3),
(4, 'Drug Resistance Screen', '2026-02-10', 'Active', 4),
(5, 'Viral Vector Transfection', '2026-03-01', 'Active', 2),
(6, 'Hypoxia Response Study', '2026-03-15', 'Completed', 5),
(7, 'Proliferation Assay', '2026-04-01', 'Active', 6),
(8, 'Receptor Binding Test', '2026-04-10', 'Active', 7),
(9, 'Apoptosis Induction', '2026-05-01', 'Terminated', 8),
(10, 'Immune Response Test', '2026-05-20', 'Active', 9);

INSERT INTO EXPERIMENT_RESEARCHER VALUES
(1, 1, 'Lead Investigator'),
(1, 2, 'Co-Investigator'),
(2, 2, 'Lead Investigator'),
(3, 3, 'Lead Investigator'),
(4, 1, 'Lead Investigator'),
(5, 4, 'Lead Investigator'),
(6, 5, 'Lead Investigator'),
(7, 6, 'Lead Investigator'),
(8, 7, 'Lead Investigator'),
(9, 8, 'Lead Investigator');

INSERT INTO PASSAGE VALUES
(1, 1, '2026-01-12', '1:3', 1, 1, 1),
(2, 2, '2026-01-16', '1:4', 1, 1, 1),
(3, 1, '2026-01-18', '1:2', 2, 2, 2),
(4, 1, '2026-02-03', '1:5', 3, 3, 3),
(5, 2, '2026-02-08', '1:5', 3, 3, 3),
(6, 1, '2026-02-12', '1:3', 4, 1, 4),
(7, 1, '2026-03-03', '1:2', 5, 8, 2),
(8, 1, '2026-03-18', '1:4', 6, 1, 5),
(9, 1, '2026-04-03', '1:3', 7, 1, 6),
(10, 1, '2026-04-12', '1:2', 8, 4, 7);

INSERT INTO CONTAMINATION_TEST VALUES
(1, '2026-01-13', 'Mycoplasma', 'Negative', 1),
(2, '2026-01-17', 'Bacterial', 'Negative', 2),
(3, '2026-01-19', 'Fungal', 'Negative', 3),
(4, '2026-02-04', 'Mycoplasma', 'Negative', 4),
(5, '2026-02-09', 'Bacterial', 'Negative', 5),
(6, '2026-02-14', 'Mycoplasma', 'Positive', 6),
(7, '2026-03-05', 'Viral', 'Negative', 7),
(8, '2026-03-20', 'Fungal', 'Negative', 8),
(9, '2026-04-05', 'Mycoplasma', 'Negative', 9),
(10, '2026-04-15', 'Bacterial', 'Negative', 10);

INSERT INTO CRYOSTOCK VALUES
(1, 20, 'Dewar A - Rack 1', '2026-01-05', 1),
(2, 15, 'Dewar A - Rack 2', '2026-01-08', 2),
(3, 30, 'Dewar B - Rack 1', '2026-01-20', 3),
(4, 10, 'Dewar B - Rack 2', '2026-02-01', 4),
(5, 25, 'Dewar C - Rack 1', '2026-02-15', 5),
(6, 12, 'Dewar C - Rack 2', '2026-03-01', 6),
(7, 18, 'Dewar D - Rack 1', '2026-03-10', 7),
(8, 22, 'Dewar D - Rack 2', '2026-04-01', 8),
(9, 8,  'Dewar E - Rack 1', '2026-04-15', 9),
(10, 14, 'Dewar E - Rack 2', '2026-05-01', 10);