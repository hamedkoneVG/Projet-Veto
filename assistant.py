#!/usr/bin/python3

import psycopg2


def menu_assistant(conn):
    while True:
        print("\n--- Menu Assistant Vétérinaire ---")
        print("1 - Ajouter un client")
        print("2 - Visualiser un client")
        print("3 - Visualiser les patients associés à un client")
        print("4 - Mettre à jour coordonée d'un client")
        print("5 - Quitter")

        try:
            choix = int(input("Choisissez une action: "))

            if choix == 1:
                ajouter_client(conn)
            elif choix == 2:
                visualiser_client(conn)
                input("Appuyez sur n'importe quel touche")
            elif choix == 3:
                id_client = input("Inserer l'identifiant du client: ")
                afficher_animal_client(conn, id_client)
                input("Appuyez sur n'importe quel touche")
            elif choix == 4:
                maj_info_client(conn)
                input("Appuyez sur n'importe quel touche")
            elif choix == 5:
                print("Fermeture du menu assistant vétérinaire.")
                break
            else:
                print("Option invalide. Veuillez choisir un nombre entre 1 et 5.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre valide.")


def verifie_champ_personne( codep= None, telephone= None):

    if telephone is not None:
        try:
            int(telephone)
        except ValueError:
            print ("Erreur : Ce n'est pas un numéro de téléphone")
        if telephone[0] != '0':
            print ("Erreur : Ue numéro de télephone commence forcément par un 0")
        if len(telephone) != 10:
            print ("Erreur : Le numéro de télephone doit contenir 10 chiffes")

        # vérification de la validité du code postal
    if codep is not None:
        try:
            int(codep)
        except ValueError:
            print("Erreur : Ce n'est pas un code postal, il ne contient pas que des chiffres")
        if len(codep) != 5:
            print("Erreur : Un code postal contient 5 chiffes")


def ajouter_client(conn):
    try:
        nom = input("Entrez le nom du client: ")
        prenom = input("Entrez le prénom du client: ")
        date_naissance = input("Entrez la date de naissance (YYYY-MM-DD): ")
        num = input("Entrez le numéro de la rue: ")
        rue = input("Entrez le nom de la rue: ")
        ville = input("Entrez la ville: ")
        code_postal = input("Entrez le code postal: ")
        telephone = input("Entrez le numéro de téléphone: ")

        verifie_champ_personne(code_postal,telephone)


        cur = conn.cursor()
        #on verifie que le client ne fait pas partie du personel car le personel ne peut pqs qvoir d'qnimaux de compagnie traité dans la clinique
        query = """
                SELECT COUNT(*) 
                FROM Personnels 
                WHERE nom = %s AND prenom = %s AND date_naissance = %s AND num = %s AND rue = %s AND ville = %s 
            """
        cur.execute(query, (nom, prenom, date_naissance,num,rue,ville))
        result = cur.fetchone()

        if result[0] > 0:
            print("Erreur : Le client existe déjà dans la liste des personnels.")
        else:
            query = """
                INSERT INTO Clients 
                VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s,%s)
            """
            cur.execute(query, (nom, prenom, date_naissance, num, rue, ville, code_postal, telephone))
            conn.commit()
            print("Client ajouté avec succès.")

    except ValueError:
        print("Erreur: la date est invalide.")
    except psycopg2.Error as e:
        print(f"Erreur lors de l'ajout du client: {e}")
    finally:
        cur.close()

        
def maj_info_client(conn):
    try:
        client_id = input("Entrez l'ID du client: ")
        cur = conn.cursor()
        print("Tapez 1 pour mettre à jour le numero du client")
        print("Tapez 2 pour mettre à jour l'addresse du client")
        choix = int(input("Choisissez une action: "))
        if choix == '2' :
            num = input("Entrez le numéro de la rue: ")
            rue = input("Entrez le nom de la rue: ")
            ville = input("Entrez la ville: ")
            code_postal = input("Entrez le code postal: ")
            verifie_champ_personne(codep=code_postal )
            query =  """
                UPDATE Clients SET num = %s, rue = %s,  ville = %s, code_postale = %s
                WHERE id_client = %s  
            """
            cur.execute(query, (num, rue, ville,code_postal,client_id))
            conn.commit()
        elif choix == '1' :
            telephone = input("Entrez le numéro de téléphone: ")
            verifie_champ_personne(telephone=telephone)
            query = """
                UPDATE Clients
                SET telephone = %s WHERE id_client = %s;  
                """
            cur.execute(query, (telephone,client_id))
            conn.commit()
    except psycopg2.Error as e:
        print(f"Erreur lors de la visualisation du client: {e}")
    finally:
        cur.close()
def afficher_animal_client(conn, id_client):
    cur= conn.cursor()
    query = f"""
        SELECT 
        p.id_patient, p.nom, p.date_naissance, p.num_puce, p.passport, e.type, e.categorie 
        FROM Appartient a INNER JOIN Patients p ON a.animal = p.id_patient
        INNER JOIN Especes e ON p.idEspece = e.id
        WHERE a.proprietaire = {id_client} and a.end_appartient is null;

        """
    cur.execute(query)
    raw = cur.fetchone()
    print(f"Les animaux associé à votre identifiant ({id_client}) sont : ")
    while raw :
        #print(f"- idPatient : {raw[0]}, nom : {raw[1]} date de naissance : {raw[2]} Numéro de Puce : ", raw[3] if raw[3] is not None else '', ", Passeport :  ", raw[4] if raw[4] is not None else '', f", Espèce : {raw[5]}\n\n") #a verifier que raw[9] est bien le nom de l'espece
        print(
            f"""
              #######################################################  
              idPatient : {raw[0]}
              Nom : {raw[1]}
              Date de naissance : {raw[2]}
              Numéro de Puce : {raw[3] if raw[3] is not None else ''}
              Passeport : {raw[4] if raw[4] is not None else ''}
              Espèce : {raw[5]}
              Categorie: {raw[6]}
              #######################################################  
            """
        )
        raw = cur.fetchone()


def visualiser_client(conn):
    try:
        client_id = input("Entrez l'ID du client: ")

        cur = conn.cursor()
        query = """
            SELECT * FROM Clients WHERE id_client = %s
        """
        cur.execute(query, (client_id,))
        client = cur.fetchone()

        if client:
            print("\n--- Informations du client ---")
            print(f"ID: {client[0]}, Nom: {client[1]}, Prénom: {client[2]}, Date de naissance: {client[3]}")
            print(f"Adresse: {client[4]} {client[5]}, {client[6]} {client[7]}")
            print(f"Téléphone: {client[8]}")
        else:
            print("Aucun client trouvé avec cet ID.")

    except psycopg2.Error as e:
        print(f"Erreur lors de la visualisation du client: {e}")
    finally:
        cur.close()





if __name__ == "__main__":
    HOST = "tuxa.sme.utc"
    USER = input("Utilisateur: ")
    PASSWORD = input("Mot de passe: ")
    DATABASE = input("Base de données: ")
    try:
        conn = psycopg2.connect(host=HOST, dbname=DATABASE, user=USER, password=PASSWORD)
        menu_assistant(conn)
    except psycopg2.OperationalError as e:
        print(f"Erreur de connexion: {e}")
    finally:
        if conn:
            conn.close()
