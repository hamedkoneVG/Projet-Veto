db.patient.insertMany([
  {
    "id_patient": 2,
    "proprietaire": [
      {
        "nom": "Doe",
        "prenom": "John",
        "date_naissance": "1990-06-20",
        "adresse": {
          "num": 12,
          "rue": "rue des lilas",
          "ville": "Paris",
          "code_postal": 75000
        },
        "telephone": "0765432109",
        "start": "01/01/2020",
        "end": "01/01/2023"
      }
    ],
    "nom": "Misty",
    "date_naissance": "2018-05-20",
    "num_puce": 654321,
    "passport": "Passport456",
    "espece": {
      "type": "chat",
      "categorie": "felides"
    },
    "dossier_medical": {
      "analyses": [
        {
          "lien": "lien2.pdf",
          "date": "2024-12-31T12:00:00"
        }
      ]
    }
  },
  {
    "id_patient": 3,
    "proprietaire": [
      {
        "nom": "Smith",
        "prenom": "Anna",
        "date_naissance": "1985-11-30",
        "adresse": {
          "num": 45,
          "rue": "avenue des tulipes",
          "ville": "Lyon",
          "code_postal": 69000
        },
        "telephone": "0754321098",
        "start": "15/06/2019"
      }
    ],
    "nom": "Shadow",
    "date_naissance": "2021-07-15",
    "num_puce": 987654,
    "passport": "Passport789",
    "espece": {
      "type": "cheval",
      "categorie": "equides"
    },
    "dossier_medical": {
      "analyses": [
        {
          "lien": "lien3.pdf",
          "date": "2023-08-15T12:00:00"
        }
      ]
    }
  },
  {
    "id_patient": 4,
    "proprietaire": [
      {
        "nom": "Brown",
        "prenom": "Emily",
        "date_naissance": "1992-02-15",
        "adresse": {
          "num": 7,
          "rue": "rue des érables",
          "ville": "Marseille",
          "code_postal": 13000
        },
        "telephone": "0743210987",
        "start": "01/03/2022"
      }
    ],
    "nom": "Luna",
    "date_naissance": "2020-03-10",
    "num_puce": 112233,
    "passport": "Passport321",
    "espece": {
      "type": "lapin",
      "categorie": "lagomorphes"
    },
    "dossier_medical": {
      "analyses": [
        {
          "lien": "lien4.pdf",
          "date": "2025-05-01T12:00:00"
        }
      ]
    }
  }
]);