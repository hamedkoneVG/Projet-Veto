from requete import *


def admin(conn):
    choix = True
    while(choix):
        print('1 - Voir une table')
        print('2 - Ajout d un client')
        print('3 - Ajout d un personnel')
        print('4 - Ajout d un médicament')
        print('5 - Ajout d un animal')
        print('6 - Associer un animal à un client')
        print('7 - Ajout d une mesure')
        print('8 - Ajout d une analyse')
        print('9 - Ajout d une procédure')
        print('10 - Ajout d un traitement')
        print('11 - Ajout d une observation')
        print('12 - Afficher la quantité de médicament consommé entre 2 dates')
        print('13 - Afficher le nombre de traitement suivi par un client sur une période')
        print('14 - Afficher le traitement actuel d un annimal')
        print('15 - Compter le nombre d animaux traités groupés par espèce')
        print('16 - Supprimer un dossier médiacal')
        print('16 - Mettre à jour la durée d un traitement')
    


        try:
            choix = int(input("Choisir une action: "))

            #####################
            # Voir les tables   #
            #####################

            if choix ==1 :
                showTable(conn)
            #####################
            # Ajout client      #
            #####################
            elif choix ==2 :
                nom=input("Quelle est le nom du client ? ")
                prenom=input("Quelle est le prénom du client ? ")
                date_naissance=input("Quelle est la date de naissance du client ? ")
                numero=input("Quelle est le numéro de rue du client ? ")
                rue=input("Quelle est le nom de la rue du client ? ")
                ville=input("Quelle est la ville du client ? ")
                codep=input("Quelle est le code postal du client ? ")
                telephone=input("Quelle est le numéro de téléphone du client ? ")
                inserer_client(conn, nom, prenom, date_naissance, numero, rue, ville, codep, telephone)
            #####################
            # Ajout personnel   #  
            #####################
            elif choix ==3 :
                nom=input("Quelle est le nom du personnel ? ")
                prenom=input("Quelle est le prénom du personnel ? ")
                date_naissance=input("Quelle est la date de naissance du personnel ? ")
                numero=input("Quelle est le numéro de rue du personnel ? ")
                rue=input("Quelle est le nom de la rue du personnel ? ")
                ville=input("Quelle est la ville du personnel ? ")
                codep=input("Quelle est le code postal du personnel ? ")
                telephone=input("Quelle est le numéro de téléphone du personnel ? ")
                specialite=input("Quelle est la specialite du personnel ? ")
                poste=input("Quelle est le poste du personnel ? ")
                inserer_personnel(conn, nom, prenom, date_naissance, numero, rue, ville, codep, telephone, specialite, poste)
            #####################
            # Ajout médicament  #  
            #####################
            elif choix ==4 :
                nom=input("Quelle est le nom du médiacament ? ")
                effets=input("Quelle sont les effets du médicaments ? ")
                inserer_medicament(conn, nom, effets)
            #####################
            # Ajout animal      #
            #####################
            elif choix ==5 :
                nom=input("Quelle est le nom de l animal ? ")
                espece=input("Quelle est l espèce de l'animal ? ")
                date_naissance=input("Quelle est la date de naissance de l'animal ? ")
                puce=input("Quelle est le numéro de puce de l'animal ? ")
                passeport=input("Quelle est le numéro de passeport de l'animal ? ")
                inserer_animal(conn, nom, espece, date_naissance=None, puce=None, passeport=None)
            ###########################
            # Associer animal/client  #  
            ###########################
            elif choix ==6 :
                animal=int(input("Quelle est l'id de l animal ? "))
                proprietaire=int(input("Quelle est l'id du client ? "))
                start=input("Quelle est la date à laquelle le client et l'animal sont liés ? ")
                inserer_appartenance(conn, animal, proprietaire, start, end=None)
            #####################
            # Ajout mesure      #  
            #####################
            elif choix ==7 :
                dossier=int(input("Quelle est l'id du dossier médical ? "))
                taille=int(input("Quelle est la taille de l'animal ? "))
                poids=int(input("Quelle est le poids de l'animal ? "))
                inserer_mesures(conn, dossier, taille, poids)
            #####################
            # Ajout analyse     #  
            #####################
            elif choix ==8 :
                dossier=int(input("Quelle est l'id du dossier médical ? "))
                lien=input("Quelle est le lien ? ")
                inserer_analyse(conn, dossier, lien)
            #####################
            # Ajout procédure  #  
            #####################
            elif choix ==9 :
                dossier=int(input("Quelle est l'id du dossier médical ? "))
                desc=input("Quelle est la description de la procédure ? ")
                inserer_procedure(conn, dossier, desc)
            #####################
            # Ajout traitement  #  
            #####################
            elif choix ==10 :
                start=input("Quelle est la date de début du traitement ? ")
                duree=input("Quelle est la durée du traitement ? ")
                veto=input("Quelle est la date de début du traitement ? ")
                dossier=int(input("Quelle est l'id du dossier médical ? "))
                inserer_traitement(conn, start, duree, veto, dossier)
            #####################
            # Ajout observation #  
            #####################
            elif choix ==11 :
                dossier=int(input("Quelle est l'id du dossier médical ? "))
                desc=input("Quelle est la description de l'observation ? ")
                inserer_observation(conn, dossier, desc)
            ######################################
            # Afficher la quantité de médicament #  
            ######################################
            elif choix ==12 :
                date_debut=input("Quelle est la date de début ? ")
                date_fin=input("Quelle est la date de fin ? ")
                medicament_consomme(conn, date_debut, date_fin)
            ######################################
            # Afficher le nombre de traitement   #  
            ######################################
            elif choix ==13 :
                date_debut=input("Quelle est la date de début ? ")
                date_fin=input("Quelle est la date de fin ? ")
                traitement_periode(conn, date_debut, date_fin)
            ######################################
            # Afficher le traitement actuel      #  
            ######################################
            elif choix ==14 :
                nom_animal=input("Quelle est le nom de l animal ? ")
                traitement_actuel(conn, nom_animal)
            ######################################
            # Compte le nombre d animaux traités #  
            ######################################
            elif choix ==15 :
                date_debut=input("Quelle est la date de début ? ")
                date_fin=input("Quelle est la date de fin ? ")
                espece_traite(conn, date_debut, date_fin)
            ######################################
            # Supprimer un traitement            #  
            ######################################
            elif choix ==16 :
                dossier=int(input("Quelle est l'id du dossier médical ? "))
                suppression_dossier(conn,dossier)
            ######################################
            # Mettre à jour un traitement        #  
            ######################################
            elif choix ==16 :
                duree=int(input("Quelle est la nouvelle durée ? "))
                idtraitement=input("Quelle est l'id du traitement que vous voulez modifier? ")
                update_traitement(conn, duree, idtraitement)


            else :
                print("action invalide")
            conn.commit()
        except ValueError as e:
            print("Veuillez entrer un nombre entier.",e)
        
