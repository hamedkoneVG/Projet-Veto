-- Création de la table Personnels

CREATE TABLE Personnels (
    id_personnel INTEGER PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    date_naissance DATE NOT NULL,
    num INTEGER NOT NULL, 
    rue VARCHAR(255) NOT NULL, 
    ville VARCHAR(100) NOT NULL,
    code_postal INTEGER NOT NULL,
    telephone VARCHAR(50) NOT NULL,
    CHECK (date_naissance < current_date + 6575 )
);

-- Création de la table Clients
CREATE TABLE Clients (
    id_client INTEGER PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    date_naissance DATE NOT NULL,
    num INTEGER NOT NULL, 
    rue VARCHAR(255) NOT NULL, 
    ville VARCHAR(100) NOT NULL,
    code_postal INTEGER NOT NULL,
    telephone VARCHAR(50) NOT NULL,
    CHECK (date_naissance < current_date)

);

-- Création de la table Especes
CREATE TABLE Especes (
    id INTEGER PRIMARY KEY,
    type VARCHAR(100) NOT NULL,
    categorie VARCHAR(20) NOT NULL,
    CHECK (categorie IN ('félin', 'canidé', 'reptile', 'rongeurs', 'oiseaux', 'autres'))
);

-- Création de la table Dossier_med
CREATE TABLE Dossier_med (
    id_med INTEGER PRIMARY KEY
);

-- Création de la table Patients
CREATE TABLE Patients (
    id_patient INTEGER PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    date_naissance DATE ,
    num_puce INTEGER,
    passport VARCHAR(50),
    idEspece INTEGER NOT NULL,
    idDossierMed INTEGER NOT NULL,
    FOREIGN KEY (idEspece) REFERENCES Especes(id),
    FOREIGN KEY (idDossierMed) REFERENCES Dossier_med(id_med),
    CHECK (date_naissance < current_date )
);

-- Création de la table Medicaments
CREATE TABLE Medicaments (
    nom VARCHAR(255) PRIMARY KEY,
    effet TEXT NOT NULL
);

-- Création de la table Assistants
CREATE TABLE Assistants (
    id_assistant INTEGER PRIMARY KEY,
    FOREIGN KEY (id_assistant) REFERENCES Personnels(id_personnel)
);
-- Création de la table Veterinaires
CREATE TABLE Veterinaires (
    id_veterinaire INTEGER PRIMARY KEY,
    FOREIGN KEY (id_veterinaire) REFERENCES Personnels(id_personnel)
);

-- Création de la table Traitements
CREATE TABLE Traitements (
    id_traitement INTEGER PRIMARY KEY,
    start DATE NOT NULL,
    duree INTEGER NOT NULL,
    date TIMESTAMP NOT NULL,
    idVeterinaire INTEGER NOT NULL,
    idDosser_Med INTEGER NOT NULL,
    FOREIGN KEY (idVeterinaire) REFERENCES Veterinaires(id_veterinaire),
    FOREIGN KEY (idDosser_Med) REFERENCES Dossier_med(id_med),
    CHECK (duree>0)
);

-- Création de la table Quantite
CREATE TABLE Quantite (
    traitement INTEGER NOT NULL,
    medicament VARCHAR(255) NOT NULL,
    nbr INTEGER NOT NULL,
    PRIMARY KEY (traitement, medicament),
    FOREIGN KEY (traitement) REFERENCES Traitements(id_traitement),
    FOREIGN KEY (medicament) REFERENCES Medicaments(nom),
    CHECK (nbr>=0)
);

-- Création de la table Analyses
CREATE TABLE Analyses (
    id_analyses INTEGER PRIMARY KEY,
    lien VARCHAR(255) NOT NULL,
    date TIMESTAMP NOT NULL,
    dossier_med INTEGER NOT NULL,
    FOREIGN KEY (dossier_med) REFERENCES Dossier_med(id_med),
    CHECK (date<current_date)
);

-- Création de la table Observations
CREATE TABLE Observations (
    idObservations INTEGER PRIMARY KEY,
    observation TEXT NOT NULL,
    date TIMESTAMP NOT NULL,
    dossier_med INTEGER NOT NULL,
    FOREIGN KEY (dossier_med) REFERENCES Dossier_med(id_med),
    CHECK (date<current_date)
);

-- Création de la table Procedures
CREATE TABLE Procedures (
    id_procedures INTEGER PRIMARY KEY,
    description TEXT NOT NULL,
    date TIMESTAMP NOT NULL,
    dossier_med INTEGER NOT NULL,
    FOREIGN KEY (dossier_med) REFERENCES Dossier_med(id_med)
);

-- Création de la table Mesures
CREATE TABLE Mesures (
    id_mesures INTEGER PRIMARY KEY,
    dossier_med INTEGER NOT NULL,
    taille INTEGER,
    date_taille TIMESTAMP,
    poids INTEGER,
    date_poids TIMESTAMP,
    FOREIGN KEY (dossier_med) REFERENCES Dossier_med(id_med),
    CHECK ((taille IS NOT NULL AND date_taille IS NOT NULL) OR (taille IS NULL AND date_taille IS NULL)),
    CHECK ((poids IS NOT NULL AND date_poids IS NOT NULL) OR (poids IS NULL AND date_poids IS NULL))
);
-- Création de la table Autorise
CREATE TABLE Autorise (
    espece INTEGER NOT NULL,
    medicament VARCHAR(255) NOT NULL,
    PRIMARY KEY (espece, medicament),
    FOREIGN KEY (espece) REFERENCES Especes(id),
    FOREIGN KEY (medicament) REFERENCES Medicaments(nom)
);

-- Création de la table Suivi
CREATE TABLE Suivi (
    veterinaire INTEGER NOT NULL,
    patient INTEGER NOT NULL,
    start DATE NOT NULL,
    end_suivi DATE,
    PRIMARY KEY (veterinaire, patient, start),
    FOREIGN KEY (veterinaire) REFERENCES Veterinaires(id_veterinaire),
    FOREIGN KEY (patient) REFERENCES Patients(id_patient),
    CHECK (start < end_suivi)
);


-- Création de la table Appartient
CREATE TABLE Appartient (
    proprietaire INTEGER NOT NULL,
    animal INTEGER NOT NULL,
    start DATE NOT NULL,
    end_appartient DATE,
    PRIMARY KEY (proprietaire, animal, start),
    FOREIGN KEY (proprietaire) REFERENCES Clients(id_client),
    FOREIGN KEY (animal) REFERENCES Patients(id_patient),
    CHECK (start < end_appartient)
);


-- Création de la table Specialise
CREATE TABLE Specialise (
    personnel INTEGER NOT NULL,
    espece INTEGER NOT NULL,
    PRIMARY KEY (personnel, espece),
    FOREIGN KEY (personnel) REFERENCES Personnels(id_personnel),
    FOREIGN KEY (espece) REFERENCES Especes(id)
);
