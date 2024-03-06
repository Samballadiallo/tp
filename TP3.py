import glob
"""
Fonction - Fichier - Liste :
Fichier nous permet de sauvegarder des données issues de l'execution du programme.
On peut aussi visualiser les données du fichier ou meme faire des opérations
de mise à jour
Tout Traitement à faire dans un fichier nécessite son ouverture
Tout fichier ouvert doit être fermé après traitement
Au moment d'ouvrir le fichier il faut spécifier son mode d'ouverture
Le mode d'ouverture utilisé dépend du traitement à lui appliquer
L'assignation est obligatoire entre le nom logique et le nom physique du fichier
Exercice : Ecrire un script python qui contient :
- une fonction de sasie des infos d'un annuaire
- une fonction qui affiche les infos d'un annuaire
- une fonction de création un fichier annuaire telephonique
- une fonction qui affiche le contenu du fichier
- ne foncion qui permet d'ajouter des contacts dans l'annuaire
- une fonction qui détermine et affiche le pourcentage de contacts par genre
- une fonction pour le menu
- Appeler le menu dans un autre fichier python
Contact (nom, prénom, genre, numero téléphonique, son mail)
"""
#- une fonction de sasie des infos d'un annuaire
def saisie():
    nom=input("entre votre nom:",)
    prenom=input("entre votre prenom:",)
    while True:
        genre=input("entre votre genre M/F:",)
        if genre.upper()=="M" or genre.upper()=="F":
            break
        else:
            print("sa doit estre M/F")
    numero_tel=input("entre votre numero de telephone:",)
    mail=input("entre votre mail:",)
    c=nom+":"+prenom+":"+genre+":"+numero_tel+":"+mail 
    return c
#c=saisie()
#print(c)
#une fonction qui affiche les infos d'un annuaire
def affichage(c):
    info=c.split(":")
    for i in info:
        print(i,end=" ")
#affichage(c)
# une fonction de création un fichier annuaire telephonique
def fichier():
    nom=input("entre le nom du fichier que vous souhaiter cree :",)
    with open(nom,"w") as f:
        n=int(input("vous souhaiter cree combien de contacte:",))
        for i in range(1,n+1):
            print("le contacte numero {}".format(i))
            print("entre les coordonne ")
            c=saisie()
            f.write(c + "\n")
#fichier()
#une fonction qui affiche le contenu du fichier
def affichagecontenu():
    entre=input("entre le nom du fichier que vous souhaiter consulter:",)
    info=glob.glob(entre)
    for i in info:
        with open(i,"r")as f:
            print(f.read())
#affichagecontenu()
#ne foncion qui permet d'ajouter des contacts dans l'annuaire
def ajoutcontacte():
    info=input("entre le nom du contacte a qui vous deve ajouter des contacte:",)
    act=glob.glob(info)
    for i in act:
        with open(i,"a")as f:
            n=int(input("combien de contacte vous vouler ajouter:",))
            for a in range(1,n+1):
                print("le contact numero{}".format(a))
                c=saisie()
                f.write(c)
#ajoutcontacte()
#une fonction qui détermine et affiche le pourcentage de contacts par genre
def detreminergenr():
    info=input("entre le nom du docier :")
    num=glob.glob(info)
    for i in num:
        with open (i,"r") as f:
            line=f.readlines()
            if len(line)==0:
                print("vous avez un docier vide")
            else:
                pMf=0
                for i in line:
                    genre=i.split(":")[2]
                    if genre.upper()=="F":
                        pMf+=1
                pfm=(pMf*100)/len(line)
                pmas=100-pfm
                print("le pourcentage du genre feminin est {}".format(pfm))
                print("le pourcentage du genre masculin est {}".format(pmas))
detreminergenr()




