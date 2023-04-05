def ouioui(chemin):
    """
    Fonction qui intercale  les éléments de l2 et l1'
    """
    with open(chemin, "r") as fd:
        liste = fd.readlines()
        c = len(liste)
        return c
    
   
    
        
def main():
    """
  Appel de la fonction qui va intercaler les éléments
    """
    
   
    print(ouioui("C:/Users/hamou/OneDrive - Aix-Marseille Université/Bureau/Programmes pyhton/tp7/students.txt"))
    
    

# pour l'instant vous devez ajouter ces trois lignes sans vous poser
# de questions. La signification de ces lignes viendra plus tard.
if __name__ == '__main__':
    main()