-- Insertion de valeurs dans la table Personnels
INSERT INTO Personnels (id_personnel, nom, prenom, date_naissance, num, rue, ville, code_postal, telephone)
VALUES
    (1, 'Martin', 'Dupont', '1980-05-12', 10, 'Rue des Lilas', 'Paris',75000, '0102030405'),
    (2, 'Leroy', 'Sophie', '1978-11-22', 15, 'Avenue des Champs', 'Lyon',69000, '0607080910'),
    (3, 'Dumas', 'Alain', '1985-08-30', 20, 'Boulevard Saint-Germain', 'Paris', 75000,'0506070809'),
    (4, 'Moreau', 'Isabelle', '1990-07-15', 5, 'Place de la République', 'Marseille',13000, '0708091011'),
    (5, 'Bernard', 'Pierre', '1992-02-18', 12, 'rue de la Gare', 'Lille',59000, '0908070605');

-- Insertion de valeurs dans la table Clients
INSERT INTO Clients (id_client, nom, prenom, date_naissance, num, rue, ville, code_postal, telephone)
VALUES
    (1, 'Durand', 'Emma', '1995-03-15', 8, 'Rue des Fleurs', 'Nantes', 44000,'0405060708'),
    (2, 'Petit', 'Lucas', '1989-06-21', 18, 'Rue de la Liberté', 'Lyon', 69000, '0203040506'),
    (3, 'Robert', 'Chloé', '2000-09-02', 25 ,'Rue Victor Hugo', 'Bordeaux',33000, '0304050607'),
    (4, 'Richard', 'Léo', '1987-12-10', 14, 'Rue des Rosiers', 'Nice', 06000, '0102030405'),
    (5, 'Morel', 'Manon', '1992-04-25', 30, 'Avenue des Frères Lumière', 'Toulouse', 31000, '0506070809');

-- Insertion de valeurs dans la table Especes
INSERT INTO Especes (id, type, categorie)
VALUES
    (1, 'Chat', 'félin'),
    (2, 'Chien', 'canidé'),
    (3, 'Serpent', 'reptile'),
    (4, 'Lapin', 'rongeurs'),
    (5, 'Perroquet', 'oiseaux');

-- Insertion de valeurs dans la table Dossier_med
INSERT INTO Dossier_med (id_med)
VALUES
    (1), (2), (3), (4), (5);

-- Insertion de valeurs dans la table Patients
INSERT INTO Patients (id_patient, nom, date_naissance, num_puce, passport, idEspece, idDossierMed)
VALUES
    (1, 'Felix', '2015-06-01', NULL, NULL, 1, 1),
    (2, 'Rex', '2018-09-15', NULL, 'P12345', 2, 2),
    (3, 'Slyther', '2020-05-05', NULL, NULL, 3, 3),
    (4, 'Bunny', '2019-01-10', NULL, 'P67890', 4, 4),
    (5, 'Coco', '2017-11-25', NULL, NULL, 5, 5);

-- Insertion de valeurs dans la table Medicaments
INSERT INTO Medicaments (nom, effet)
VALUES
    ('Amoxicilline', 'Antibiotique pour infections bactériennes'),
    ('Carprofène', 'Anti-inflammatoire pour douleur et inflammation'),
    ('Meloxicam', 'Soulage l’inflammation et la douleur chez les animaux'),
    ('Ivermectine', 'Antiparasitaire pour traiter les parasites internes et externes'),
    ('Metronidazole', 'Antibiotique pour infections gastro-intestinales');

-- Insertion de valeurs dans la table Assistants
INSERT INTO Assistants (id_assistant)
VALUES
    (2), (4), (5);

-- Insertion de valeurs dans la table Veterinaires
INSERT INTO Veterinaires (id_veterinaire)
VALUES
    (1), (3);

-- Insertion de valeurs dans la table Traitements
INSERT INTO Traitements (id_traitement, start, duree, date, idVeterinaire, idDosser_Med)
VALUES
    (1, '2023-01-15', 14, '2023-01-15 10:30:00', 1, 1),
    (2, '2023-04-20', 7, '2023-04-20 11:00:00', 3, 2),
    (3, '2023-06-10', 10, '2023-06-10 09:45:00', 1, 3),
    (4, '2023-08-25', 5, '2023-08-25 14:30:00', 3, 4),
    (5, '2023-10-15', 21, '2023-10-15 13:00:00', 1, 5);

-- Insertion de valeurs dans la table Quantite
INSERT INTO Quantite (traitement, medicament, nbr)
VALUES
    (1, 'Amoxicilline', 2),
    (2, 'Carprofène', 1),
    (3, 'Meloxicam', 1),
    (4, 'Ivermectine', 3),
    (5, 'Metronidazole', 2);

-- Insertion de valeurs dans la table Analyses
INSERT INTO Analyses (id_analyses, lien, date, dossier_med)
VALUES
    (1, 'lien_analyse1.pdf', '2023-01-15 11:00:00', 1),
    (2, 'lien_analyse2.pdf', '2023-04-20 12:00:00', 2),
    (3, 'lien_analyse3.pdf', '2023-06-10 10:30:00', 3),
    (4, 'lien_analyse4.pdf', '2023-08-25 15:00:00', 4),
    (5, 'lien_analyse5.pdf', '2023-10-15 14:00:00', 5);

-- Insertion de valeurs dans la table Observations
INSERT INTO Observations (idObservations, observation, date, dossier_med)
VALUES
    (1, 'Observation générale pour le patient Felix', '2023-01-16 09:00:00', 1),
    (2, 'Observation de suivi pour Rex', '2023-04-21 10:00:00', 2),
    (3, 'Observation sur Slyther', '2023-06-11 08:30:00', 3),
    (4, 'Observation pour Bunny', '2023-08-26 14:15:00', 4),
    (5, 'Observation pour Coco', '2023-10-16 13:45:00', 5);

-- Insertion de valeurs dans la table Procedures
INSERT INTO Procedures (id_procedures, description, date, dossier_med)
VALUES
    (1, 'Opération de stérilisation pour Felix', '2023-01-17 09:30:00', 1),
    (2, 'Vaccination pour Rex', '2023-04-22 11:30:00', 2),
    (3, 'Extraction de dents pour Slyther', '2023-06-12 10:00:00', 3),
    (4, 'Soins de la patte blessée pour Bunny', '2023-08-27 12:00:00', 4),
    (5, 'Examen de santé annuel pour Coco', '2023-10-17 11:00:00', 5);

-- Insertion de valeurs dans la table Mesures
INSERT INTO Mesures (id_mesures, dossier_med, taille, date_taille, poids, date_poids)
VALUES
    (1, 1, 40, '2023-01-15 10:00:00', 5, '2023-01-15 10:00:00'),
    (2, 2, 55, '2023-04-20 10:00:00', 20, '2023-04-20 10:00:00'),
    (3, 3, 120, '2023-06-10 09:00:00', 12, '2023-06-10 09:00:00'),
    (4, 4, 25, '2023-08-25 13:00:00', 3, '2023-08-25 13:00:00'),
    (5, 5, 60, '2023-10-15 12:30:00', 7, '2023-10-15 12:30:00');

-- Insertion de valeurs dans la table Suivi
INSERT INTO Suivi (veterinaire, patient, start, end_suivi)
VALUES
    (1, 1, '2023-01-15', '2023-01-29'), 
    (3, 2, '2023-04-20', '2023-04-27'), 
    (1, 3, '2023-06-10', '2023-06-20'), 
    (3, 4, '2023-08-25', '2023-08-30'), 
    (1, 5, '2023-10-15', '2023-11-05');

-- Insertion de valeurs dans la table Appartient 
INSERT INTO Appartient (proprietaire, animal, start, end_appartient) 
VALUES 
    (1, 1, '2023-01-15', NULL), 
    (2, 2, '2023-04-20', NULL), 
    (3, 3, '2023-06-10', NULL), 
    (4, 4, '2023-08-25', NULL), 
    (5, 5, '2023-10-15', NULL);

-- Insertion de valeurs dans la table Autorise 
INSERT INTO Autorise (espece, medicament) 
VALUES 
    (1, 'Amoxicilline'), 
    (2, 'Carprofène'), 
    (3, 'Meloxicam'), 
    (4, 'Ivermectine'), 
    (5, 'Metronidazole');

-- Insertion de valeurs dans la table Specialise 
INSERT INTO Specialise (personnel, espece) 
VALUES 
    (1, 1), 
    (2, 2), 
    (3, 3), 
    (4, 4), 
    (5, 5);
