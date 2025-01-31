
// Afficher le nombre d'animaux par espèce triés par nombre décroissant (STATISTIQUES)
db.patient.aggregate([
  {
    $group: {
      _id: "$espece.type", 
      nombre_animaux: { $sum: 1 } 
    }
  },
  {
    $sort: { nombre_animaux: -1 } 
  }
]);


//Afficher le nombre total consommé de chaque médicament entre deux dates spécifiques (STATISTIQUES)
db.patient.aggregate([
  {
    $unwind: "$dossier_medical.traitements" 
  },
  {
    $match: {
      "dossier_medical.traitements.date": {
        $gte: new Date("{date_debut}"), 
        $lte: new Date("{date_fin}") 
      }
    }
  },
  {
    $unwind: "$dossier_medical.traitements.medicaments" 
  },
  {
    $group: {
      _id: "$dossier_medical.traitements.medicaments.nom", 
      total_consomme: { $sum: "$dossier_medical.traitements.medicaments.quantite" }
    }
  },
  {
    $sort: { total_consomme: -1 } 
  }
]);


//Afficher le nombre de traitements distincts pour chaque client entre deux dates spécifiques (STATISTIQUES)
db.patient.aggregate([
  {
    $unwind: "$proprietaire" 
  },
  {
    $unwind: "$dossier_medical.traitements"
  },
  {
    $match: {
      "dossier_medical.traitements.date": {
        $gte: new Date("{date_debut}"), 
        $lte: new Date("{date_fin}")  
      }
    }
  },
  {
    $group: {
      _id: "$proprietaire.id", 
      Nom_Client: { $first: "$proprietaire.nom" }, 
      Prenom_Client: { $first: "$proprietaire.prenom" }, 
      Nombre_Traitements: { $addToSet: "$dossier_medical.traitements.id_traitement" } 
  },
  {
    $project: {
      ID_Client: "$_id", 
      Nom_Client: 1, 
      Prenom_Client: 1, 
      Nombre_Traitements: { $size: "$Nombre_Traitements" } 
    }
  },
  {
    $sort: { Nombre_Traitements: -1 } 
  }
]);


//Supprimer les traitements dont la date est plus ancienne qu'un an (DELETE)
db.patient.updateMany(
  {
    "dossier_medical.traitements.date": {
      $lt: new Date(new Date().setFullYear(new Date().getFullYear() - 1)) 
    }
  },
  {
    $pull: {
      "dossier_medical.traitements": {
        "date": {
          $lt: new Date(new Date().setFullYear(new Date().getFullYear() - 1)) 
        }
      }
    }
  }
);

//Mettre à jour la durée d'un traitement  (UPDATE)
db.patient.updateOne(
  { "dossier_medical.traitements.id_traitement": 4 },
  {
    $set: { "dossier_medical.traitements.$.duree": 10 } 
  }
);


