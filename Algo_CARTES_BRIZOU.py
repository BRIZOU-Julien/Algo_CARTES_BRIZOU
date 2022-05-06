"""
J'importe la bibliothèque random afin de pouvoir créer des évènements aléatoires tels que :
-> faire piocher aléatoirement une carte dans ma pioche
"""

from json.tool import main
import random


"""
J'initialise une classe Carte Qui me permettra d'intéragir dans mon jeu
"""

class Carte:
    def __init__(self, nom, CoutMana, Description):
        self.nom = nom
        self.CoutMana = CoutMana
        self.Description = Description

    def getNom(self):
        return self.nom

    def  getCoutMana(self):
        return self.CoutMana

    def getDescription(self):
        return self.Description

"""
J'initialise une classe Mage qui permettra de gérer les actions de la personne qui joue
"""

class Mage : 
    def __init__(self, Nom, PointsDeVie, Total, ValeurMana):
        self.Nom = Nom
        self.PointsDeVie = PointsDeVie
        self.Total = Total
        self.ValeurMana = ValeurMana
        self.main=[]
        self.zoneDeJeu=[]

    def getNom(self):
        return self.Nom
    
    def getPointsDeVie(self):
        return self.PointsDeVie

    def getTotal(self):
        return self.Total

    def getValeurMana(self):
        return self.ValeurMana

    def getmain(self):
        return self.main

    def getZoneDeJeu(self):
        return self.zoneDeJeu
    
    def Piocher(self, CartePiochee):
        self.main.append(CartePiochee)

    def getCarteEnMain(self, nombre):
        return self.main[nombre]

    def jouerUneCarte(self, carteaJouer):                                               #Je définis une méthode qui permet de jouer une carte
        print(PremierJoueur.getNom(),"utilise une carte : ", carteaJouer.getNom())      #J'affiche la carte à utiliser
        self.ValeurMana -= carteaJouer.getCoutMana()                                    #Je soustrais la valeur en mana de la carte au mage
        self.ZoneDeJeu.append(carteaJouer)                                              #J'ajoute ma carte à la zone de jeu
        print("La carte", carteaJouer, "a été utilisée")                                #J'affiche la carte utilisée
        self.main.remove(carteaJouer)                                                   #Je retire la carte de la main du joueur
        Montour2 = False                                                                #J'empêche le joueur de pouvoir rejouer

    def perdrePv(self,nombre):
        if self.PointsDeVie <= self.PointsDeVie-nombre :
            PartieTerminee ==True
            print(PremierJoueur.getNom(),"n'a plus de vie,", DeuxièmeJoueur.getNom(), "remporte la partie")
"""
J'initialise une classe Cristal (héritant de la classe Carte)
"""

class Cristal(Carte) : 
    def __init__(self, nom, CoutMana, Description, Valeur, CoutEnMana):
        Carte.__init__(self, nom, CoutMana, Description)
        self.Valeur = Valeur
        self.CoutEnMana = CoutEnMana

    def getValeur(self):
        return self.Valeur

    def getCoutEnMana(self):
        return self.CoutEnMana





"""
J'initialise une classe Créature (héritant de la classe Carte)
Une créature peut être jouée sur la zone de jeu afin d'infliger des dégats (égal au score d'attaque)
"""

class Creature : 
    def __init__(self, Nomcreature, PV, ScoreAttaque, PrixMana, nom, CoutMana, Description,):
        Carte.__init__(self, nom, CoutMana, Description)
        self.Nomcreature = Nomcreature
        self.PV = PV
        self.ScoreAttaque = ScoreAttaque
        self.PrixMana = PrixMana

    def getNomcreature(self):
        return self.Nomcreature

    def getPV(self):
        return self.PV

    def getScoreAttaque(self):
        return self.ScoreAttaque

    def getPrixMana(self):
        return self.PrixMana

    def Combat(self):
        Endommager = int(input(print("Attaquer le Mage ou sa créature ? Mage = 1, Créature = 2")))
        if Endommager == 1:
            Endommager = DeuxièmeJoueur
        if Endommager == 2 :
            Creatureennemi = DeuxièmeJoueur.getZoneDeJeu()
            for i in range(len(Creatureennemi)):
                print("Attaquer cette créature? Oui = 1 Non = 2")
                print(Creatureennemi[i].getNomcreature())
                combat=int(input())
                if(combat==1):
                    Endommager = Creatureennemi[i]




"""
J'initialise une classe Blast (héritant de la classe Carte)
Un blast peut être invoqué pour infliger un certain nombre de points de dégâts
Ce qui enlèvera de la vie à l'adversaire ou sa créature
"""  

class Blast :
    def __init__(self, nom, CoutMana, Description, ValeurBlast, PointsDeVieBlast):
        Carte.__init__(self, nom, CoutMana, Description)
        self.ValeurBlast = ValeurBlast
        self.PointsDeVieBlast = PointsDeVieBlast

    def getValeurBlast(self):
        return self.ValeurBlast

    def getPointsDeVieBlast(self):
        return self.PointsDeVieBlast



"""
J'initialise des joueurs, crées à partir de la classe Mage
Ainsi, je leur affecte ce qui est précisé dans ma fonction __init__ de ma classe Mage :

def __init__(self, Nom, PointsDeVie, Total, ValeurMana):

Chaque Mage se verra attribuer un Nom, Des points de vie, un Total et une valeur de Mana
"""  

Joueur1 = Mage("Mage numéro 1", 30, 50, 30)
Joueur2 = Mage("Mage numéro 2", 20, 40, 30)

PremierJoueur = Joueur1
DeuxièmeJoueur = Joueur2

"""
Ensuite, J'initialise les différentes cartes qui seront intégrées dans mon jeu (correspondants aux classes)
Je crée des Blasts, des créatures, etc...
"""

Blast1 = Blast("Je suis le Blast 1", 5, "Description de ma Carte de Blast 1", 10)
Blast2 = Blast("Je suis le Blast 2", 10, "Description de ma Carte de Blast 2", 5)
Blast3 = Blast("Je suis le Blast 3", 20, "Description de ma Carte de Blast 3", 20)


"""
J'initialise une carte Abandon (issue de ma classe Carte)
Pour seulement 0 Mana, vous pouvez bandonner la partie ! Quelle aubaine
"""

Carte1 = Carte("Fin de partie", 0, "Partie terminée !")

"""
J'initialise une carte Cristal (issue de ma classe Cristal, elle-même issue de ma classe Carte)
"""

Cristal1 = Cristal("Bonjour, je suis le nom du cristal", 1, "Je suis la description du cristal",3)

"""
J'initialise ma première créature
"""
Creature1 = Creature("Je suis la créature 1", 2, "Description creature 1", 3, 5, 4)

"""
Ma pioche est composée de toutes mes cartes "Blast" et toutes mes cartes "Cartes"
"""

Pioche = [Blast1, Blast2, Blast3, Carte1]

"""
Début de la partie de jeu, Tant que ma variable "PartieTerminee" est égale à False, 
on effectue les actions suivantes
"""

PartieTerminee = False
carteaJouer = 0
while PartieTerminee == False:

    print(PremierJoueur.getNom()," s'apprête à jouer ! \n Vous disposez de PV :", PremierJoueur.getPointsDeVie(),"\n Vous disposez d'un total", PremierJoueur.getTotal(), "\n Vous disposez d'une valeur de Mana", PremierJoueur.getValeurMana())
    Montour = True

    Montour2 = True
    while Montour2 == True :
        Choix = int(input(PremierJoueur.getNom(), "Voulez-vous piocher une carte ou abandonner la partie ? Piocher = 1; Abandonner = 2 :"))
        if Choix == 2 : 
            print("Partie Terminée !\n Le joueur", PremierJoueur.getNom(), "a décidé d'abandonner la partie !")
            PartieTerminee = True
        elif Choix != 1:
            print("Partie Terminée !\n Le joueur", PremierJoueur.getNom(), "a entrer un mauvaix nombre !")
            PartieTerminee = True
        elif Choix == 1:

            print("Le joueur", PremierJoueur.getNom()," pioche une carte")
            CartePiochee = Pioche[random.randint(0,3)]
            PremierJoueur.Piocher(CartePiochee)
            print("Le joueur pioche une carte Cristal et une carte Creature")
            PremierJoueur.Piocher(Cristal1)
            PremierJoueur.Piocher(Creature1)  
        
            while Montour == True :
                print("Au tour de ",PremierJoueur.getNom()," de jouer!")
                ActionJoueur = int(input("Sélectionnr votre action entre utiliser une de vos cartes, Envoyer vos créatures à l'attaque ou finir ce tour ? Respectivement (1, 2 et 3) :"))
                if ActionJoueur == 1 : 
                    print("Sélectionnez une carte à utiliser")
                    print(PremierJoueur.getCarteEnMain(main))
                    if carteaJouer >= 0 and carteaJouer < len(PremierJoueur.getmain()) :
                        if carteaJouer.getCoutMana() < PremierJoueur.getValeurMana():
                            PremierJoueur.jouerUneCarte(PremierJoueur.getCarteEnMain(carteaJouer))
                        else :
                            print("Votre mana est inférieur au cout de man de la carte que vous essayez de jouer")
                            Montour2 = False
                    else :
                        print("Nombre incorrect")
                        Montour2 = False

                elif ActionJoueur == 2:
                    Nombrecreature = PremierJoueur.getZoneDeJeu()
                    for i in range(len(Nombrecreature)):
                        combattre = int(input("Attaquer avec", Nombrecreature[i].getNomcreature(), "? Oui = 1 Non = 2"))
                        if (combattre == 1):
                            Nombrecreature[i].Combat()

                else :
                    Montour = False
                    Montour2 = False

    
    PremierJoueur.ValeurMana = 30

    if PremierJoueur.getNom() == "Mage numéro 1" :
        print(PremierJoueur.getNom(), "a terminé son tour")
        PremierJoueur = Joueur2
        DeuxièmeJoueur = Joueur1
        
    else:
        print(PremierJoueur.getNom(), "a terminé son tour")
        PremierJoueur = Joueur1
        DeuxièmeJoueur = Joueur2