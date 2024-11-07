""" Module a pour but de vérifier si un entier est un nombre premier ou pas. """
from math import sqrt

#### Fonction secondaire


def isprime(p):
    # votre code ici
    """
    isprime  a pour but de vérifier si un entier est un nombre premier ou pas.
    Args:
        p: entier dont on veut vérifier s'il est premier ou non
    return:
        isprime(p): True ou False
    
    """
    premier = True # on définie la variable premier qui vaut true par défaut
    if p == 1:
        return False
    for i in range(2,int(sqrt(p))+1): # on parcours tout les potentiels diviseurs de p [2, √p]
        if p % i == 0: # si le reste de la division entre p et un des potentiels diviseurs est nulle
            premier = False # la variable devient donc False
            return premier # retourne le boolean qui définit si p est premier
    return premier # retourne le boolean qui définit si p est premier


#### Fonction principale


def main():
    """
    fonction main

    """
    # vos appels à la fonction secondaire ici
    print("1",isprime(1))
    print("4",isprime(4))
    print("18",isprime(18))
    print("7",isprime(7))
    print("3",isprime(3))
    print("0",isprime(0))
    print("3",isprime(3))
    print("9",isprime(9))
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()
if __name__ == "__main__":
    main()
