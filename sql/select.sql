SELECT * 
FROM Clients;


SELECT * 
FROM Clients
WHERE nom = 'Durand';


SELECT p.nom AS patient, p.date_naissance, e.type AS espece
FROM Patients p
JOIN Appartient a ON p.id_patient = a.animal
JOIN Clients c ON a.proprietaire = c.id_client
JOIN Especes e ON p.idEspece = e.id
WHERE c.id_client = 1;


SELECT o.observation, o.date
FROM Observations o
JOIN Patients p ON o.dossier_med = p.idDossierMed
WHERE p.nom = 'Felix';


SELECT m.nom AS medicament, q.nbr AS quantite, m.effet
FROM Quantite q
JOIN Medicaments m ON q.medicament = m.nom
WHERE q.traitement = 1;


SELECT CASE 
           WHEN COUNT(*) > 0 THEN 'Autorisé'
           ELSE 'Non autorisé'
       END AS statut
FROM Autorise a
JOIN Especes e ON a.espece = e.id
WHERE e.categorie = 'félin' AND a.medicament = 'Amoxicilline';


SELECT p.nom AS patient, p.date_naissance, e.type AS espece, s.start, s.end_suivi
FROM Suivi s
JOIN Patients p ON s.patient = p.id_patient
JOIN Especes e ON p.idEspece = e.id
WHERE s.veterinaire = 1;


SELECT d.id_med AS dossier, MAX(a.date) AS derniere_analyse
FROM Dossier_med d
LEFT JOIN Analyses a ON d.id_med = a.dossier_med
GROUP BY d.id_med;


SELECT p.nom, p.prenom, e.type AS espece
FROM Specialise s
JOIN Personnels p ON s.personnel = p.id_personnel
JOIN Especes e ON s.espece = e.id
WHERE e.categorie = 'canidé';


SELECT v.id_veterinaire, p.nom AS nom_veterinaire, COUNT(t.id_traitement) AS nombre_traitements
FROM Veterinaires v
JOIN Personnels p ON v.id_veterinaire = p.id_personnel
LEFT JOIN Traitements t ON v.id_veterinaire = t.idVeterinaire
GROUP BY v.id_veterinaire, p.nom;


SELECT p.nom AS patient, t.start AS date_traitement, m.nom AS medicament, q.nbr AS quantite, 
       o.observation, pr.description AS procedure
FROM Patients p
LEFT JOIN Traitements t ON p.idDossierMed = t.idDosser_Med
LEFT JOIN Quantite q ON t.id_traitement = q.traitement
LEFT JOIN Medicaments m ON q.medicament = m.nom
LEFT JOIN Observations o ON p.idDossierMed = o.dossier_med
LEFT JOIN Procedures pr ON p.idDossierMed = pr.dossier_med
WHERE p.nom = 'Rex';






