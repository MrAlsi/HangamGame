import os
import AsciiArt
import listaParole
import random

#FUNZIONI
#Metodo per l'estrazione della parola
def parola_casuale(lista):
  if lista == "facile":
    return random.choice(listaParole.Facile)
  elif lista == "media":
    return random.choice(listaParole.Media)
  else:
    return random.choice(listaParole.Difficile)

#stampa un'Ascii art per la vittoria
def vittoria():
    print(AsciiArt.vittoria)
    input("Premi un tasto qualsiasi per continuare...")
    

#stampa un'Ascii art per la sconfitta
def sconfitta():
    print(AsciiArt.sconfitta)
    
#Trasforma la parola in carattere in '-'
def parola_oscurata1(parola_gioco):
    p_oscurata=[]
    for i in parola_gioco:
        p_oscurata.append("-")
    return p_oscurata

#Aggiusta la parola sostituendo '-' con il carattere
def parola_oscurata2(p_oscurata, parola_gioco, car):
    for i in range(0,len(parola_gioco)):
        if car == parola_gioco[i]:
            p_oscurata[i] = car
    return p_oscurata

# Funzione che gestisce una partita
def gioca(parolaSegreta):
    numVite = 6
    pss=parola_oscurata1(parolaSegreta)
    #Game loop
    while numVite > 0:
        print(pss)
        print(AsciiArt.stick[6-numVite])
        carattere = str(input("Digita una lettera:  "))
        #Controllo se il carattere è una e una sola lettera
        if carattere.isalpha() and len(carattere) == 1:
            if carattere in parolaSegreta:
                parola_oscurata2(pss, parolaSegreta, carattere)
                if ''.join(pss) == parolaSegreta:
                    vittoria()      #Chiama grafica per la vittoria
                    menu()          #Richiama il menu per ricominciare
            else:
                numVite-=1
        else:
            print("Per favore inserisci un carattere... stronzo")
            input("Premi un tasto qualsiasi per continuare...")
      
        #Pulisce il terminale
        os.system('cls')

    sconfitta()
    input("Premi un tasto qualsiasi per continuare...")


# Stampa le regole del gioco e aspetta un'azione dell'utente per andare avanti
def regole():
    os.system('cls')
    print('''Regole: Devi indovinare la parola nei tentativi richiesti dalla modalità\n che hai selezionato. 
         Ogni turno devi inserire una lettera e ti verrà detto se quest'ultima\n è presente o 
         meno all'interno della parola che devi indovinare.\n Se finisci tutte le vite prima di completare la parola avrai perso.''')
    continua = input("Premi un tasto qualsiasi per continuare...")
    menu()
   
# Seleziona la difficoltà, metodo ricorsivo nel caso l'utente inserisca un numero non valido
def selezionaDifficolta():
    os.system('cls')
    scelta=int(input("Scegli la difficoltà\n1: Facile  -  2: Media  -  3: Difficile\n"))
    if scelta == 1: 
       return "facile"
    elif scelta == 2: 
       return "media"
    elif(scelta == 3): 
       return "difficile"
    else: 
        return selezionaDifficolta()

#Funzione per mostrare il menu
def menu():
    os.system('cls')
    menuGioco = True
    difficolta = "media"
    #Menu
    while(menuGioco):
        os.system('cls')
        scelta=int(input("Scegli cosa vuoi fare\n1) Gioca\n2) Regole\n3) Opzioni\n4) Esci\n"))
        if scelta == 1: 
            gioca(parola_casuale(difficolta))
        elif scelta == 2: 
            regole()
        elif scelta == 3: 
            difficolta = selezionaDifficolta()
        elif scelta == 4:
           menuGioco = False
        else: 
            print("Non ho capito")
    


#Start del programma
menu()



