import csv
import os.path
import sys
found = False
def check_movies(name):
    global found
    with open("library.csv","r",encoding="UTF-8") as read:
        csvReader = csv.reader(read)
        for row in csvReader:
            if name == row[0]:
                print(row)
                found = True
        if not found:
            print("Nie zanleziono tego filmu")

def display_information_about_movie():
    if not os.path.exists("library.csv") or os.stat("library.csv").st_size == 0:
        print("Brak zapisanych filmów")
        return
    with open("library.csv","r", encoding="UTF-8") as read:
        csvReader = csv.reader(read)
        for row in csvReader:
            print(row)

def add_movie():
    titleMovie = input("Podaj tytuł filmu")
    NameAndSurname = input("Podaj imie i nazwisko rzeżysera tego filmu")
    YearPublic = int(input("Podaj rok wydania tej książki"))
    fileExit = os.path.exists("library.csv")
    with open("library.csv","a",newline="") as movie:
            textMovie=csv.writer(movie)
            if not fileExit:
                textMovie.writerow(["Tytuł filmu", "Imię i nazwisko reżysera", "Rok publikacji"])
            textMovie.writerow([titleMovie, NameAndSurname, YearPublic])
def edit_movie():
    movie = []
    global found
    nameMovie = input("Podaj nazwę filmu który ty chcesz zedytować")

    if not os.path.exists("library.csv") or os.stat("library.csv").st_size == 0:
        print("Brak zapisanych filmów")
        return
    with open("library.csv","r", encoding="UTF-8") as read:
        csvReader = csv.reader(read)
        for row in csvReader:
            if nameMovie == row[0]:
                textMovie = csv.writer(read)
                print("""
                Co chcesz zeedtytować ;)
                1.Nazwę filmu
                2.Autora Filmu
                3.Rok publikacji
                """)
                try:
                    question = int(input("Podaj opcje"))
                except ValueError:
                    print("Wartość musi być liczbę")
                if question == 1:
                    row[0] = input("Podaj nową nazwę filmu")
                elif question == 2:
                    row[1] = input("Podaj nazwę Autora filmu")
                elif question == 3:
                    while True:
                        new_year = input("Podaj nowy rok publikacji: ")
                        if new_year.isdigit() or new_year == "":
                            row[2] = new_year or row[2]
                            break
                        else:
                            print("Rok musi być liczbą!")
                found = True
        if not nameMovie:
            found=False
            print("Nie znaleziono tego filmu")
        movie.append(row)
        with open("library.csv","w",newline="",encoding="UTF-8") as file:
            textWrite = csv.writer(file)
            textWrite.writerows(movie)
def delete_movie():
    fileFound = False
    movieLibrary = []
    nameMovie = input("Podaj nazwę filmu który ty chcesz usunąć")
    if not os.path.exists("library.csv") or os.stat("library.csv").st_size == 0:
        print("Brak zapisanych filmów")
        return
    with open("library.csv","r") as file:
        textRead = csv.reader(file)
        header= next(textRead)
        movieLibrary.append(header)
        for row in textRead:
            if row and row[0].lower() == nameMovie.lower():
                fileFound = True
            else:
                movieLibrary.append(row)
    if not fileFound:
        print("Nie znaleziono takiego filmu")
    with open("library.csv","w",newline="",encoding="UTF-8") as file:
        textMovie = csv.writer(file)
        textMovie.writerows(movieLibrary)
def search_movie():
    name = input("Podaj nazwię filmu")
    check_movies(name)
while True:
    print("""
    Witamy w programie movies ;)
    1.Wyświetl informacje o filmie
    2.Dodaj film do albumu
    3.Edytuj istniejący film
    4.Usuń podany film
    5.Wyszukaj film po tytule
    6.Koniec programu""")
    choice = int(input("Wyberz opcje"))
    if choice==1:
        display_information_about_movie()
    elif choice==2:
        add_movie()
    elif choice==3:
        edit_movie()
    elif choice==4:
        delete_movie()
    elif choice==5:
        search_movie()
    elif choice==6:
        sys.exit()