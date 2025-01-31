# Note de clarification

## Sujet

**Gestion d'une clinique vétérinaire**

On vous charge de réaliser une application de gestion pour une clinique vétérinaire. L'administrateur de la clinique souhaite pouvoir gérer ses patients (animaux), ses clients, son personnel soignant ainsi que les médicaments administrés. Les clients et les personnels ont tous des noms, prénoms, date de naissance, une adresse et un numéro de téléphone. Les personnels ont en plus un poste (vétérinaire ou assistant) et une spécialité : les espèces animales qu'ils savent le mieux traiter. La clinique se spécialise dans le traitement d'animaux domestiques de petites et moyennes tailles, ils peuvent être des félins, des canidés, des reptiles, des rongeurs, ou des oiseaux. Exceptionnellement, elle peut traiter des animaux qui ne figurent pas parmi ces catégories et les regroupe dans une classe « autres ».

Pour chaque animal traité, la clinique souhaite garder son nom, son espèce, sa date de naissance (qui peut être juste une année, ou inconnue), le numéro de sa puce d'identification (s'il en a), son numéro de passeport (s'il en a), la liste de ses propriétaires et la période durant laquelle l'animal était avec eux, ainsi que la liste des vétérinaires qui l'ont suivi et quand est-ce qu'ils l'ont fait. Il faut noter que le personnel de la clinique ne doit pas avoir d'animaux de compagnie traités dans la clinique.

La clinique souhaite aussi garder le dossier médical de ses patients. Un dossier médical contient plusieurs entrés de différents types :

Une mesure de sa taille ou de son poids.

Un traitement prescrit avec la date de début, la durée, le nom et la quantité à prendre par jour pour chaque médicament prescrit (on peut prescrire plusieurs molécules dans un traitement). Seul un vétérinaire peut prescrire un traitement.

Des résultats d'analyses (sous forme de lien vers un document électronique)

Une observation générale faite lors d'une consultation et qui l'a faite.

Une procédure réalisée sur le patient avec sa description.

Pour chaque entrée, on veut garder la date et l'heure auxquelles elle a été saisie.

Enfin, les médicaments sont identifiés par le nom de la molécule et sont accompagnés de quelques lignes de texte décrivant leurs effets. Un médicament n'est autorisé que pour certaines espèces.



## Détails du système

### Classes

**Personnes** 
nom,
prenom,
date_naissance,
adresse,
telephone.

**Clients** 

**Personnels**

**Assistants**

**Veterinaires**

**Traitements**
start,
duree,
date.

**Medicaments** 
nom,
effet.

**Especes**
type,
categorie{"félins","canidés","reptile","rongeurs","oiseaux","autres"}.

**Patients**
nom,
date_naissance,
id,
passeport.


**Dossiers_med**

**Mesures**

**Tailles** 
taille,
date.

**Poids**
poids,
date.


**Analyses**
lien,
date.


**Observations**
observation,
date.

**Procedures**
desc,
date.



### Associations

**Clients** et **Personnels** sont des humains, ils héritent donc de **Personnes**

**Assistants** et **Veterinaires** sont des personnels du cabinet, ils héritent donc de **Personnels**

**Tailles** et **Poids** sont des mesures prises par le peronnel lors d'une consultations, ils héritent donc de **Mesures**

**Mesures**, **Analyses**, **Observations**, **Procédures** et **Traitements** sont stockés dans le dossier médical du patient. Il y a donc une associations entre toutes ces classes et **Dossiers_med**. Comme à chaque consultations il y a des nouvelles mesures, analyses, observations, procédures et un nouveau traitement préscrit alors la cardinalité est 1 dossier médicale pour plusieurs données, d'où **(\*-1)**.

Chaque animal à son dossiers médical, il y a donc une association entre **Patients** et **Dossiers_med**, de cardinalité **(1-1)**.
  
Chaque anaimal appartient à une espèce, il y a donc une association entre **Patients** et **Especes** et comme un animal ne peut appartenir qu'à une espèce mais que plusieurs aniaux peuvent être de la même espèce, la cardinalité est **(\*-1)**.

Chaque membre du personnels est forcément spécialisé pour le traitement d'une espèce (qui peut être la même qu'un de ses collègue), il y a donc une association entre **Personnels** et **Especes**, de cardinalité **(\*-1..\*)**.

Chaque animal traité possède forcément un propriétaire et un humain ne peut pas être client s'il ne possède pas d'animal. Il y a donc une association entre **Clients** et **Patients**, de cardinalité **(1..\*-1..\*)**. Dans l'éventualité d'un changement de propriétaire, le cabinet souhaite archiver les propiétaire de l'animal avec la date d'acquisition et de cession. Pour cela, on crée la classe :
**Appartient** start, end.

Un traitement est obligatoirement préscrit par un vétérnaire, il y a donc une association entre **Veterinaires** et **Traitements** de cardinalité **(1-\*)** (un vétérinaire peut préscrire plusieurs traitements).

Un **Traitements** se compose d'au moins un **Médicaments**. Il y a donc une cardinalité **(\*-1..\*)**. De plus, le cabinet souhaite pouvoir archiver la quantité de médicaments préscrit par jour. Il faut donc créer une classe :  
**Quantite** nbr.

Un **Medicaments** est autorisé pour certaines **Especes**, il y a donc une cardinalité **(\*-\*)**.

Un **Veterinaires** suit au moins **Patients** et un patient est suivi par au moins vétérinaires, il nous faut donc une associations **(1..\*-1..\*)**. Le cabinet veterinaire souhaite archivé quel **Veterinaires** a suivi un **Patients**, il faut donc qu'on crée une classe :  
**Suivi** start, end.



