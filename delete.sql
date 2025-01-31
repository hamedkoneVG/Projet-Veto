//DELETE
DELETE FROM Veterinaires
WHERE id_veterinaire = 3;

DELETE FROM Traitements
WHERE start < CURRENT_DATE - INTERVAL '1 year';


DELETE FROM Patients
WHERE id_patient = 5;


DELETE FROM Observations
WHERE dossier_med = 2;
