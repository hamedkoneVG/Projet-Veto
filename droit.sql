-- Étape 1 : Création des utilisateurs
CREATE USER admin WITH PASSWORD 'admin_password';
CREATE USER vet WITH PASSWORD 'vet_password';
CREATE USER assistant WITH PASSWORD 'assistant_password';
CREATE USER client WITH PASSWORD 'client_password';


-- Étape 2 : Configuration des privilèges

-- 2.1 : Privilèges pour admin_role (accès total)
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO admin;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO admin;

-- 2.2 : Privilèges pour veterinaire_role
-- Vétérinaire : Lire et écrire sur toutes les données nécessaires sauf suppression des clients/personnels
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO veterinaire;
-- Empêcher la suppression des clients et personnels
REVOKE DELETE ON Clients, Personnels FROM veterinaire;

-- 2.3 : Privilèges pour assistant_role
-- Assistant : Gérer les dossiers médicaux et les clients
GRANT SELECT, INSERT, UPDATE ON Dossier_med, Clients TO assistant;
-- Lecture sur les autres tables nécessaires
GRANT SELECT ON Patients, Observations, Analyses, Traitements, Medicaments, Especes TO assistant;

-- 2.4 : Privilèges pour client_role
-- Client : Accès à son propre dossier médical uniquement
GRANT SELECT ON Dossier_med TO client;

-- Étape 3 : Révocation des privilèges par défaut pour plus de sécurité
-- Retirer les droits par défaut pour le rôle PUBLIC
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM PUBLIC;
