#!/usr/bin/python3

import psycopg2
from requete import *
from admin import *
from main_veterinaire import *
from client import *
from assistant import menu_assistant

HOST = "tuxa.sme.utc"
USER = input("identifiqnt 'nf18aXXX': ")
PASSWORD = input("mot de passe: ")
DATABASE = input("base de donnée 'dbnf18aXXX': ")

"""
USER = input("inserer le type d'utilisateur: admin | veterinaire | assistant | client : ")

PASSWORD = input("mot de passe utilisateur: ")

DATABASE = input("dbnf18aXXX")
"""

try:
    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
except psycopg2.OperationalError as e:
    raise(e)

if USER=="nf18a029":
    veterinaire(conn)
#elif USER=="assistant":
elif USER=="nf18a031":
    menu_assistant(conn)
elif USER=="nf18a037":
    client(conn)
elif USER=="nf18a043":
    admin(conn)
else :
    print("Erreur l'utilisateur n'est ni un admin, ni un client, ni un vétérinaire, ni un assistant vétérinaire")




conn.close()