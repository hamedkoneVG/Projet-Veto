

# Fonction d'insertion d'un client dans la Table Client
def inserer_client(conn, nom, prenom, date_naissance, numero, rue, ville, codep, telephone):
    # vérification de la validité du numéro de telephone
    try:
        int(telephone)
    except ValueError:
        raise ("Erreur : Ce n'est pas un numéro de téléphone")

    if telephone[0] != '0':
        raise ("Erreur : Ue numéro de télephone commence forcément par un 0")
    
    if len(telephone) != 10:
        raise ("Erreur : Le numéro de télephone doit contenir 10 chiffes")
    

    # vérification de la validité du code postal
    try:
        int(codep)
    except ValueError:
        raise ("Erreur : Ce n'est pas un code postal, il ne contient pas que des chiffres")

    if len(codep) != 5:
        raise ("Erreur : Un code postal contient 5 chiffes")

    cur = conn.cursor()

    # insertion du client dans la table Clients
    query1 = f"INSERT INTO Clients VALUES (DEFAULT, '{nom}', '{prenom}', '{date_naissance}', {numero}, '{rue}', '{ville}', {codep}, {telephone});"
    cur.execute(query1)
    conn.commit()


# Fonction d'insertion du personnel dans la table Personnels
def inserer_personnel(conn, nom, prenom, date_naissance, numero, rue, ville, codep, telephone, specialite, poste):
    # vérifications de la validité du numéro de telephone
    try:
        int(telephone)
    except ValueError:
        raise ("Erreur : Ce n'est pas un numéro de téléphone")

    if telephone[0] != '0':
        raise ("Erreur : Ue numéro de télephone commence forcément par un 0")
    
    if len(telephone) != 10:
        raise ("Erreur : Le numéro de télephone doit contenir 10 chiffes")

    # vérification de la validité du code postal
    try:
        int(codep)
    except ValueError:
        raise ("Erreur : le code postal ne doit contenir que des chiffres")

    if len(codep) != 5:
        raise ("Erreur : Le code postal doit contenir 5 chiffes")

    # vérification de la validité de la spécialité
    if not (specialite in ['félins', 'canidés', 'reptiles', 'rongeurs', 'oiseaux', 'autres']):
        raise ("specialite inexistante")

    # vérification de la validité du poste
    if not (poste in ['Veterinaire', 'Assistant']):
        raise ("poste inexistant")

    cur = conn.cursor()

    # insertion dans la table Personnels
    query1 = f"INSERT INTO Personnels VALUES (DEFAULT, '{nom}', '{prenom}', '{date_naissance}', {numero}, '{rue}', '{ville}', {codep}, {telephone});"
    cur.execute(query1)
    conn.commit()

    # récupération de l'id (généré automatiquement)
    query2 = f"SELECT id_personnels FROM Personnels WHERE telephone = {telephone};"
    # telephone peut etre utilisé pour identifier un membre du personnel, puisqu'il est unique
    cur.execute(query2)
    id = cur.fetchall()[0][0]


    if poste == 'Veterinaire':

        query3 = f"INSERT INTO Veterinaires VALUES ({id});"
        cur.execute(query3)
        conn.commit()

    else:
        query3 = f"INSERT INTO Assistants VALUES ({id});"
        cur.execute(query3)
        conn.commit()

# Fonction permettant d'insérer un nouveau médicament dans la table Medicament
def inserer_medicament(conn, nom, effets):
    cur = conn.cursor()
    
    query1 = f"INSERT INTO Medicament VALUES ('{nom}','{effets}')"
    cur.execute(query1)
    conn.commit()

    cur.close()


# Fonction permettant d'insérer un animal dans la table Patients
def inserer_animal(conn, nom, espece, date_naissance=None, puce=None, passeport=None):
    # véfificaton que la puce ne comporte que des chiffre ou traduit le type None de python puis le transforme en NULL sql
    if puce != None:
        try:
            int(puce)
        except ValueError:
            raise ("Erreur : Une puce ne contient que des chiffres")
    else:
        puce = 'NULL'

    # véfificaton que le numero de passeport ne comporte que des chiffre ou traduit le type None de python puis le transforme en NULL sql
    if passeport != None:
        try:
            int(passeport)
        except ValueError:
            raise ("Erreur : le numero de passeport ne contient que des chiffres")
    else:
        passeport = 'NULL'

    cur = conn.cursor()
    query1 = f"INSERT INTO Dossier_med VALUES (DEFAULT);"
    cur.execute(query1)
    DossierMed = cur.fetchone()[0]
    query2 = f"INSERT INTO Patients VALUES (DEFAULT,'{nom}','{date_naissance}',{puce},{passeport},'{espece}', {DossierMed});"

    cur.execute(query2)
    conn.commit()

    cur.close()


# Fonction permettant d'associer un animal a ses propriétaires
def inserer_appartenance(conn, animal, proprietaire, start, end=None):
    # verification que la date de début < date de fin à traiter
    if end == None:
        end = 'NULL'
    else:
        end = f"\'{dfin}\'"

    cur = conn.cursor()
    # insertion dans la table Appartient
    query1 = f"INSERT INTO Appartient VALUES ('{proprietaire}','{animal}','{start}',{end});"
    cur.execute(query1)
    conn.commit()
    cur.close()


# Fonction permettant d'insérer des mesures d'un animal dans la table Mesures
def inserer_mesures(conn, dossier, taille, poids):
    # vérification que le poids et la taille soient bien des flottants
    try:
        float(poids)
    except ValueError:
        raise ("Erreur : le poids n'est pas un flottant")
    
    try:
        float(taille)
    except ValueError:
        raise ("Erreur : la taille n'est pas un flottant")

    cur = conn.cursor()
    # insertion dans la table Mesures
    query1 = f"INSERT INTO Mesures VALUES (DEFAULT,{dossier},{taille},now(),{poids},now());"
    cur.execute(query1)
    conn.commit()
    cur.close()


# Fonction permettant d'insérer une analyse d'un animal dans la table Analyse
def inserer_analyse(conn, dossier, lien):
    cur = conn.cursor()
    query1 = f"INSERT INTO Analyses VALUES (DEFAULT,'{lien}', now(),{dossier});"
    cur.execute(query1)
    conn.commit()
    cur.close()


# Fonction permettant d'insérer une procédure de consultation d'un animal dans la table Procedures
def inserer_procedure(conn, dossier, desc):
    cur = conn.cursor()
    query1 = f"INSERT INTO Procedures VALUES (DEFAULT,'{desc}',now(),{dossier});"
    cur.execute(query1)
    conn.commit()
    cur.close()


# Fonction permettant d'insérer le traitement d'un animal dans la table Traitements
def inserer_traitement(conn, start, duree, veto, dossier):
    # vérification de la validité de la table durée
    try:
        int(duree)
    except ValueError:
        raise ("Erreur : duree n'est pas un entier")

    if int(duree) < 1:
        raise ("Erreur : un traitement dure minimum 1 jour")

    medicament = medicament.split(" ")

    cur = conn.cursor()
    # insertion dans la table Traitements
    query1 = f"INSERT INTO Traitement VALUES (DEFAULT,'{start}','{duree}',now(),{veto},{dossier});"
    cur.execute(query1)
    conn.commit()

    cur.close()

# Fonction permettant d'insérer une observation qu'un vétérinaire à effectuer lors d'une consultation dans la table Observations
def inserer_observation(conn, dossier, desc):
    cur = conn.cursor()
    query1 = f"INSERT INTO Observations VALUES (DEFAULT,'{desc}',now(),'{dossier}');"
    cur.execute(query1)
    conn.commit()
    cur.close()




#################################
##                             ##
##           Requetes          ##
##                             ##
#################################

# Fonction permettant d'afficher la quantité de médicament consommé entre 2 dates 
def medicament_consomme(conn, date_debut, date_fin):
    cur = conn.cursor()
    medicament = f"SELECT q.medicament AS Nom_medicament, SUM(q.nbr) AS Total_consomme FROM Quantite q JOIN Traitements t ON q.traitement = t.id_traitement WHERE t.date BETWEEN '{date_debut}' AND '{date_fin}' GROUP BY q.medicament ORDER BY Total_consomme DESC;"
    cur.execute(medicament)
    raw = cur.fetchone()
    while raw:
        print(f"[{raw[0]}] {raw[1]} ")
        raw = cur.fetchone()
    conn.commit()
    cur.close()

# Fonction permettant d'afficher le nombre de traitement suivi par un client sur une période
def traitement_periode(conn, date_debut, date_fin):
    cur = conn.cursor()
    traitement = f"SELECT c.id_client AS ID_Client, c.nom AS Nom_Client, c.prenom AS Prenom_Client, COUNT(DISTINCT t.id_traitement) AS Nombre_Traitements FROM Clients c JOIN Appartient a ON c.id_client = a.proprietaire JOIN Patients p ON a.animal = p.id_patient JOIN Traitements t ON p.id_patient = t.idDosser_Med WHERE t.date BETWEEN '{date_debut}' AND '{date_fin}' GROUP BY c.id_client, c.nom, c.prenom ORDER BY Nombre_Traitements DESC;"
    cur.execute(traitement)
    raw = cur.fetchone()
    while raw:
        print(f"{raw[0]} {raw[1]} {raw[2]} {raw[3]}")
        raw = cur.fetchone()
    conn.commit()
    cur.close()

# Fonction permettant d'afficher le traitement actuel d'un annimal
def traitement_actuel(conn, nom_animal):
    cur = conn.cursor()
    traitement = f"SELECT t.id_traitement AS ID_Traitement, t.start AS Date_Debut, t.duree AS Duree_Jours, t.date AS Date_Enregistrement, v.id_veterinaire AS ID_Veterinaire, p.nom AS Nom_Patient FROM Traitements t JOIN Veterinaires v ON t.idVeterinaire = v.id_veterinaire JOIN Patients p ON t.idDosser_Med = p.idDossierMed WHERE p.nom = '{nom_animal}' AND CURRENT_DATE BETWEEN t.start AND t.start + t.duree * INTERVAL '1 day' ORDER BY t.start DESC;"
    cur.execute(traitement)
    raw = cur.fetchone()
    print(f"[{nom_animal}]")
    while raw:
        print(f"{raw[0]} {raw[1]} {raw[2]} {raw[3]} {raw[4]} {raw[5]}")
        raw = cur.fetchone()
    conn.commit()
    cur.close()

# Fonction permettant de compter le nombre d'animaux traités groupés par espèce
def espece_traite(conn, date_debut, date_fin):
    cur = conn.cursor()
    espece = f"SELECT e.type AS Espece, COUNT(DISTINCT p.id_patient) AS Nombre_Animaux FROM Traitements t JOIN Patients p ON t.idDosser_Med = p.idDossierMed JOIN Especes e ON p.idEspece = e.id WHERE t.date BETWEEN '{date_debut}' AND '{date_fin}' GROUP BY e.type ORDER BY Nombre_Animaux DESC;"
    cur.execute(espece)
    raw = cur.fetchone()
    while raw:
        print(f"{raw[0]} {raw[1]}")
        raw = cur.fetchone()
    conn.commit()
    cur.close()

#Fonction qui va servir pour mettre à jour un traitement 
def update_traitement(conn, duree, idtraitement): 
   cur=conn.cursor()
   nv_duree= f"UPDATE Traitements SET duree = duree WHERE id_traitement = idtraitement"
   cur.execute(nv_duree)
	raw = cur.fetchone()
        conn.commit()
   cur.close()

# Fonction permettant de supprimer un dossier médical
def suppression_dossier(conn,dossier):
    cur = conn.cursor()
    query0 = f"DELETE FROM Dossier_med WHERE id_med = {dossier};"
    query1 = f"DELETE FROM Traitements WHERE idDosser_Med = {dossier};"
    query2 = f"DELETE FROM Analyses WHERE dossier_med = {dossier};"
    query3 = f"DELETE FROM Observations WHERE dossier_med = {dossier};"
    query4 = f"DELETE FROM Mesures WHERE dossier_med = {dossier};"
    query5 = f"DELETE FROM Dossier_med WHERE id_med = {dossier};"
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    cur.execute(query4)
    cur.execute(query5)
    cur.execute(query0)
    conn.commit()
    cur.close()

# Fonction permettant d'afficher tout les patiens associer à un client 
def afficher_animal_client(conn,id):
    cur = conn.cursor()
    query = f"""
            SELECT 
            p.id_patient, p.nom, p.date_naissance, p.num_puce, p.passport, e.categorie 
            FROM Appartient a INNER JOIN Patients p ON a.animal = p.id_patient
            INNER JOIN Especes e ON p.idEspece = e.id
            WHERE a.proprietaire = {id} AND a.end_appartient=NULL;

            """
    cur.execute(query)
    raw = cur.fetchone()
    while raw :
        print(f"- idPatient : {raw[0]}, nom : {raw[1]} date de naissance : {raw[2]} \n Numéro de Puce : {raw[3]}, Passeport :  {raw[4]}, Espèce : {raw[5]}\n\n")

    conn.commit()
    cur.close()

#Affiche le traitement actuel d'un patient d'un client
def afficher_traitement_actuel_client(conn, id_client):
    cur= conn.cursor()
    query = f"""
        SELECT 
        p.id_patient, p.nom, p.date_naissance, p.num_puce, p.passport, e.categorie 
        FROM Appartient a INNER JOIN Patients p ON a.animal = p.id_patient
        INNER JOIN Especes e ON p.idEspece = e.id
        WHERE a.proprietaire = {id_client} AND a.end_appartient=NULL;

        """
    cur.execute(query)
    raw = cur.fetchone()
    liste_animal = []
    print("Quel Animal voulez vous consultez ?")
    while raw :
        print(f"- idPatient : {raw[0]}, nom : {raw[1]} date de naissance : {raw[2]} \n Numéro de Puce : {raw[3]}, Passeport :  {raw[4]}, Espèce : {raw[5]}\n\n")
        liste_animal.append(raw[1])

    if liste_animal :
        choix_animal = str(input("Rentrez le nom de l'animal que vous voulez voir"))
        while choix_animal not in liste_animal:
            choix_animal = int(input("Rentrez votre choix"))
        traitement_actuel(conn, choix_animal)

    conn.commit()
    cur.close()


def afficher_nombre_traitement_client(conn, id_client, debut, fin):
    cur = conn.cursor()
    query = f"""
        SELECT 
        p.id_patient, p.nom, p.date_naissance, p.num_puce, p.passport, e.categorie 
        FROM Appartient a INNER JOIN Patients p ON a.animal = p.id_patient
        INNER JOIN Especes e ON p.idEspece = e.id
        WHERE a.proprietaire = {id_client} AND a.end_appartient=NULL;

        """
    cur.execute(query)
    raw = cur.fetchone()
    liste_animal = []
    print("Quel Animal voulez vous consultez ?")
    while raw:
        print(
            f"- idPatient : {raw[0]}, nom : {raw[1]} date de naissance : {raw[2]} \n Numéro de Puce : {raw[3]}, Passeport :  {raw[4]}, Espèce : {raw[5]}\n\n")
        liste_animal.append(raw[1])

    if liste_animal:
        choix_animal = str(input("Rentrez le nom de l'animal que vous voulez voir"))
        while choix_animal not in liste_animal:
            choix_animal = int(input("Rentrez votre choix"))


    conn.commit()
    cur.close()


def traitement_periode(conn, id_client, date_debut, date_fin):
    cur = conn.cursor()
    traitement = f"SELECT c.nom AS Nom_Client, c.prenom AS Prenom_Client, COUNT(DISTINCT t.id_traitement) AS Nombre_Traitements FROM Clients c JOIN Appartient a ON c.id_client = a.proprietaire JOIN Patients p ON a.animal = p.id_patient JOIN Traitements t ON p.id_patient = t.idDosser_Med WHERE t.date BETWEEN '{date_debut}' AND '{date_fin}' AND WHERE c.id_client= {id_client} GROUP BY c.id_client, c.nom, c.prenom ORDER BY Nombre_Traitements DESC;"
    cur.execute(traitement)
    raw = cur.fetchone()
    while raw:
        print(f"{raw[0]} {raw[1]} {raw[2]}")
        raw = cur.fetchone()
    conn.commit()
    cur.close()

