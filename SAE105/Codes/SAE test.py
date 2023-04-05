def compte_lignes_mots(nom_fichier):
    """
    Fonction qui intercale  les éléments de l2 et l1'
    """
    with open(nom_fichier, "r") as fd:
        liste = fd.readlines()
        c = len(liste)
        
    
   
    print(compte_lignes_mots("/amuhome/m21215366/Documents/src/Python/R107/TP7/students.txt"))
    
    
def main():
    """
  Appel de la fonction qui va intercaler les éléments
    """
    
   
    print(compte_lignes_mots("/amuhome/m21215366/Documents/src/Python/R107/TP7/students.txt"))
    
    

# pour l'instant vous devez ajouter ces trois lignes sans vous poser
# de questions. La signification de ces lignes viendra plus tard.
if __name__ == '__main__':
    main()