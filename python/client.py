from requete import *
import psycopg2

def client(conn):
    try:
        identified = False
        cur = conn.cursor()
        id_client = -1

        while not identified:
            try:
                id_client = int(input("Rentrez votre id_client : "))
            except ValueError:
                print("Veuillez entrer un identifiant valide (numérique).")
                continue

            verif_client = f"SELECT * FROM client WHERE id_client = {id_client}"
            cur.execute(verif_client)

            if cur.fetchone():
                identified = True
                print("Identifiant trouvé, vous êtes connecté.")
            else:
                print("L'identifiant est introuvable. Veuillez réessayer.")

        while True:
            print('\nMenu:')
            print('1 - Afficher vos animaux')
            print('2 - Afficher le traitement actuel d\'un animal')
            print('3 - Afficher le nombre de traitements suivis à une période donnée')
            print('4 - Quitter')

            try:
                choix = int(input("Choisir une action: "))

                if choix == 1:
                    # Afficher les animaux du client
                    afficher_animal_client(conn, id_client)

                elif choix == 2:
                    # Afficher le traitement actuel d'un animal
                    date_debut = input("Quelle est la date de début (YYYY-MM-DD) ? ")
                    date_fin = input("Quelle est la date de fin (YYYY-MM-DD) ? ")
                    afficher_traitement_actuel_client(conn, id_client, date_debut, date_fin)

                elif choix == 3:
                    # Afficher le nombre de traitements suivis à une période donnée
                    date_debut = input("Quelle est la date de début (YYYY-MM-DD) ? ")
                    date_fin = input("Quelle est la date de fin (YYYY-MM-DD) ? ")
                    afficher_nombre_traitement_client(conn, id_client, date_debut, date_fin)

                elif choix == 4:
                    print("Déconnexion...")
                    break

                else:
                    print("Action invalide. Veuillez choisir une option entre 1 et 4.")

            except ValueError as e:
                print("Erreur : Veuillez entrer un nombre entier valide.")

            conn.commit()

    except psycopg2.Error as db_error:
        print("Erreur lors de l'accès à la base de données :", db_error)

    finally:
        conn.close()
