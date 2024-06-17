import pickle

filename = 'betalinger.pk'

fodboldtur = {}

def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")

def printliste():
    for item in fodboldtur.items():
        print(item)
    menu()

def betaling():
    navn = input("Indtast navn: ")
    if navn in fodboldtur:
        beløb = float(input("Indtast beløb: "))
        fodboldtur[navn] += beløb
        afslut()
        menu()
    else:
        if navn not in fodboldtur:
            print("Navnet findes ikke i listen")
            menu()

def menu():
    print("MENU")
    print("1: Print liste")
    print("2: Tilføj betaling")
    print("3: Afslut program")
    valg = input("Indtast dit valg: ")
    if (valg == '1'):
        printliste()
    if (valg == '2'):
        betaling()
    if (valg == '3'):
        afslut()

infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()
menu()
