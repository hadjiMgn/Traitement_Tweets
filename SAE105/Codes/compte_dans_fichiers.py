#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 10:23:32 2021

@author: m21215366
"""
def compte_dans_fichiers(liste_fichiers):
    """
    Fonction qui intercale  les éléments de l2 et l1'
    """
    abc="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"  # liste des caractères 
    
    with open(liste_fichiers, "r") as fd:
        liste = fd.readlines()               # création de la liste qui a pour éléments chaque ligne 
        li = len(liste)           # va donner le nombre de lignes
        mo = 0                    # variables qui va compter le nombre de mots
        for i in liste:           # balayage de la liste 
            for a in range (len(i)):  # balayage d'un element de la liste
                if i[a] not in abc:   # Si caractere d'une ligne n'est pas dans abc
                    mo  +=1     
    res = [li,mo]
    return res

def main():
    """
  Appel de la fonction qui va intercaler les éléments
    """
    fc = input("Saisissez votre fichier : ")
    nbl = (compte_dans_fichiers(fc))
    print(nbl)
  
    
    

# pour l'instant vous devez ajouter ces trois lignes sans vous poser
# de questions. La signification de ces lignes viendra plus tard.
if __name__ == '__main__':
    main()