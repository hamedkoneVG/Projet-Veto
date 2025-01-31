UPDATE Clients
SET telephone = '0999887766'
WHERE id_client = 1;

UPDATE Mesures
SET poids = 25, date_poids = '2024-12-16 10:00:00'
WHERE id_mesures = 3;

UPDATE Traitements
SET duree = 10
WHERE id_traitement = 4;

UPDATE Personnels
SET num = 50, rue = 'Rue de la Paix', ville = 'Lille', code_postal = 59000
WHERE id_personnel = 3;

UPDATE Suivi
SET end_suivi = '2024-12-15'
WHERE veterinaire = 1 AND patient = 1;
