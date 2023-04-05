#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 10:23:32 2021

@author: m21215366
"""
import os


def envir():
    """
    Fonction qui crée l'environnement de travail
    """
    os.mkdir("src")
    os.mkdir("src/Prog")
    os.mkdir("src/Prog/Codes")
    os.mkdir("src/Prog/Rsultats")
    os.mkdir("src/Prog/Donnees")
    os.mkdir("src/Prog/Donnees/Donnee_Brute")
    os.mkdir("src/Prog/Donnees/Donnee_pret")
def main():
    """
  Appel de la fonction qui va créer l'environnement de travail
    """
    envir()
    
    

# pour l'instant vous devez ajouter ces trois lignes sans vous poser
# de questions. La signification de ces lignes viendra plus tard.
if __name__ == '__main__':
    main()
