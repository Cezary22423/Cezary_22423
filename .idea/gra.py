import random

# Tworzenie planszy
plansza_szerokosc = 10
plansza_wysokosc = 10

# Inicjalizacja pozycji gracza i punktów
gracz_x = random.randint(0, plansza_szerokosc - 1)
gracz_y = random.randint(0, plansza_wysokosc - 1)
punkty = 0

# Inicjalizacja pozycji punktu na planszy
punkt_x = random.randint(0, plansza_szerokosc - 1)
punkt_y = random.randint(0, plansza_wysokosc - 1)

# Główna pętla gry
while True:
    # Wyświetlanie planszy
    for y in range(plansza_wysokosc):
        for x in range(plansza_szerokosc):
            if x == gracz_x and y == gracz_y:
                print("P", end=" ")  # Gracz
            elif x == punkt_x and y == punkt_y:
                print("X", end=" ")  # Punkt
            else:
                print(".", end=" ")  # Puste pole
        print()

    # Poruszanie się gracza
    ruch = input("Wpisz kierunek (w - góra, s - dół, a - lewo, d - prawo): ")
    if ruch == "w" and gracz_y > 0:
        gracz_y -= 1
    elif ruch == "s" and gracz_y < plansza_wysokosc - 1:
        gracz_y += 1
    elif ruch == "a" and gracz_x > 0:
        gracz_x -= 1
    elif ruch == "d" and gracz_x < plansza_szerokosc - 1:
        gracz_x += 1

    # Sprawdzanie kolizji z punktem
    if gracz_x == punkt_x and gracz_y == punkt_y:
        punkty += 1
        print("Zdobyłeś punkt!")
        punkt_x = random.randint(0, plansza_szerokosc - 1)
        punkt_y = random.randint(0, plansza_wysokosc - 1)

    # Warunek zakończenia gry
    if punkty == 10:
        print("Gratulacje, zdobyłeś 10 punktów!")
        break
