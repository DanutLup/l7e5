import pickle
import os

CAUTARE=1
ADAUGARE=2
MODIFICARE=3
STERGERE=4
AFISARE=5
IESIRE=6

def main():
    table={}
    end_of_file= False
    if os.path.exists("DictionarAngajati.dat"):
        input_file=open('DictionarAngajati.dat','rb')
        while not end_of_file:
            try:
                table=pickle.load(input_file)
            except EOFError:
                end_of_file= True
        input_file.close()
    else:
        output_file=open('DictionarAngajati.dat','wb')
        pickle.dump(table,output_file)
        output_file.close()
    choice=0
    while choice != IESIRE:
        choice=menu_choice()
        if choice == CAUTARE:
            cautare(table)
        elif choice == ADAUGARE:
            adaugare(table)
        elif choice== MODIFICARE:
            modificare(table)
        elif choice == STERGERE:
            stergere(table)
        elif choice==ADAUGARE:
            adaugare(table)
        elif choice == IESIRE:
            output_file=open('DictionarAngajati.dat','wb')
            pickle.dump(table,output_file)
            output_file.close()

def menu_choice():
    print()
    print('Meniu Angajati')
    print('---------------------------')
    print('1. Cautarea unui angajat')
    print('2. Adaugarea unui nou angajat')
    print('3. Modificarea datelor unui angajat')
    print('4. Stergerea unui angajat')
    print('5. Iesirea din program')
    print()
    choice=int(input('Introduceti optiunea:'))
    while choice<CAUTARE or choice>IESIRE:
        choice=int(input('Eroare. Introduceti o optiune valida'))
    return choice

def cautare(table):
    ID=input('Introduceti ID-ul unui angajat:')
    print(table.get(ID,'Angajat inexistent'))
    
def adaugare(table):
    ID=input('Introduceti ID-ul noului angajat:')
    nume=input('Introduceti numele noului angajat:')
    departament=input('Introduceti departamentul noului angajat:')
    functie=input('Introduceti functia noului angajat:')
    if ID not in table:
        table[ID]=[nume,departament,functie]
    else:
        print('Eroare. ID existent')

def modificare(table):
    ID=input('Introduceti ID-ul angajatului:')
    if ID in table:
        nume=input('Modificati numele angajatului:')
        departament=input('Modificati departamentul angajatului:')
        functie=input('Modificati functia angajatului:')
        table[ID]=[nume,departament,functie]
    else:
        print('Eroare. ID inexistent')

def stergere(table):
    ID=input('Introduceti ID-ul angajatului:')
    if ID in table:
        del table[ID]
    else:
        print('Eroare. ID inexistent')

def afisare(table):
    print(table.items())
main()