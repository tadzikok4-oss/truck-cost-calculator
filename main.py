def get_positive_number(message):
    while True:
        try:
            value = float(input(message))

            if value <= 0:
                print("Blad! Wartosc musi byc wieksza od zera.")
            else:
                return value

        except ValueError:
            print("Blad! Wpisz poprawna liczbe.")

def get_non_negative_number(message):
    while True:
        try:
            value = float(input(message))

            if value < 0:
                print("Blad! Wartosc nie moze byc ujemna.")
            else:
                return value

        except ValueError:
            print("Blad! Wpisz poprawna liczbe.")


def get_valid_choice(message, min_value, max_value):
    while True:
        choice = input(message)

        if choice.isdigit():
            choice = int(choice)

            if min_value <= choice <= max_value:
                return choice

        print(f"Blad! Wybierz liczbe od {min_value} do {max_value}.")

def get_currency():
    print("Wybierz walute:")
    print("1. PLN")
    print("2. EUR")
    print("3. CZK")

    choice = get_valid_choice("Wybor (1-3): ", 1, 3)

    if choice == 1:
        return "PLN", 1.0

    elif choice == 2:
        rate = get_positive_number("Podaj kurs EUR (1 EUR = ile PLN?): ")
        return "EUR", rate

    elif choice == 3:
        rate = get_positive_number("Podaj kurs CZK (1 CZK = ile PLN?): ")
        return "CZK", rate
    
def show_menu():
    print("=== MENU GLOWNE ===")
    print("1. Oblicz nowa trase")
    print("2. Wyswietl historie tras")
    print("3. Wyjscie")
    print("4. Statystyki transportowe")
    print("5. Porownaj ciezarowki")
    print("6. Porownaj koszty przejazdu")

def show_history():
    try:
        with open("historia.txt", "r", encoding="utf-8") as file:
            print("\n=== HISTORIA TRAS ===")
            print(file.read())

    except FileNotFoundError:
        print("Historia jest jeszcze pusta.")


def show_statistics():
    print("=== STATYSTYKI TRANSPORTOWE ===")

    try:
        with open("historia.txt", "r", encoding="utf-8") as file:
            history = file.read()

        trips = history.count("Ciezarowka:")
        total_distance = 0
        total_fuel = 0
        total_cost = 0

        for line in history.splitlines():
            if line.startswith("Dystans:"):
                total_distance += float(line.split(":")[1].replace("km", "").strip())

            elif line.startswith("Zuzyte paliwo:"):
                total_fuel += float(line.split(":")[1].replace("l", "").strip())

            elif line.startswith("Koszt calkowity:"):
                total_cost += float(line.split(":")[1].replace("zl", "").strip())

        print("Liczba tras:", trips)
        print("Laczny dystans:", round(total_distance, 2), "km")
        print("Laczne zuzycie paliwa:", round(total_fuel, 2), "l")
        print("Laczny koszt:", round(total_cost, 2), "zl")

    except FileNotFoundError:
        print("Brak historii tras.")
def compare_trucks():
    print("=== POROWNANIE CIEZAROWEK ===")

    trucks = {
        "MAN TGX": 25,
        "Scania S770": 29,
        "Mercedes Actros": 27,
        "Volvo FH16": 28,
        "DAF XG+": 24,
        "Renault T": 25
    }

    print("Spalanie ciezarowek:")

    for truck_name, consumption in trucks.items():
        print(truck_name, "-", consumption, "l/100 km")

    best_truck = min(trucks, key=trucks.get)

    print("Najbardziej ekonomiczna ciezarowka:", best_truck)
    print("Spalanie:", trucks[best_truck], "l/100 km")
def compare_costs():
    print("=== POROWNANIE KOSZTOW PRZEJAZDU ===")

    currency, exchange_rate = get_currency()

    distance = get_positive_number("Podaj dystans w km: ")
    fuel_price = get_positive_number(f"Podaj cene paliwa za litr ({currency}): ")

    trucks = {
        "MAN TGX": 25,
        "Scania S770": 29,
        "Mercedes Actros": 27,
        "Volvo FH16": 28,
        "DAF XG+": 24,
        "Renault T": 25
    }

    for truck_name, consumption in trucks.items():
        fuel_used = distance * consumption / 100
        cost = fuel_used * fuel_price

        cost_pln = cost * exchange_rate
        print(truck_name, "-", round(cost, 2), currency, "(", round(cost_pln, 2), "PLN )")
def calculate_route():
    print("=== TRUCK COST CALCULATOR ===")

    print("--- WYBOR CIEZAROWKI ---")
    print("1. MAN TGX")
    print("2. Scania S770")
    print("3. Mercedes Actros")
    print("4. Volvo FH16")
    print("5. DAF XG+")
    print("6. Renault T")


    choice = str(get_valid_choice("Wybierz ciezarowke (1-6): ", 1, 6))

    if choice == "1":
        truck = "MAN TGX"
        fuel_consumption = 25

    elif choice == "2":
        truck = "Scania S770"
        fuel_consumption = 29

    elif choice == "3":
        truck = "Mercedes Actros"
        fuel_consumption = 27

    elif choice == "4":
        truck = "Volvo FH16"
        fuel_consumption = 28

    elif choice == "5":
        truck = "DAF XG+"
        fuel_consumption = 24

    elif choice == "6":
        truck = "Renault T"
        fuel_consumption = 25

    else:
        print("Nieprawidlowy wybor")
        exit()

    print("Wybrano:", truck)

    print("--- DANE TRASY ---")

    start_city = input("Podaj miejscowosc poczatkowa: ")
    end_city = input("Podaj miejscowosc docelowa: ")

    currency, exchange_rate = get_currency()

    distance = get_positive_number("Podaj dystans trasy (km): ")
    fuel_price = get_positive_number(f"Podaj cene paliwa za litr ({currency}): ")
    road_cost = get_non_negative_number(f"Podaj koszt oplat drogowych ({currency}): ")

    fuel_used = distance * fuel_consumption / 100
    total_cost = fuel_used * fuel_price
    full_cost = total_cost + road_cost
    full_cost_pln = full_cost * exchange_rate
    round_trip_cost = total_cost * 2
    cost_per_km = total_cost / distance

    print("--- WYNIKI ---")
    print("Trasa:", start_city, "->", end_city)
    print("Ciezarowka:", truck)
    print("Spalanie:", fuel_consumption, "l/100 km")
    print("Dystans:", distance, "km")
    print("Zuzyte paliwo:", round(fuel_used, 2), "l")
    print("Koszt paliwa:", round(total_cost, 2), currency)
    print("Koszt paliwa na 1 km:", round(cost_per_km, 2), currency)
    print("Koszt paliwa w obie strony:", round(round_trip_cost, 2), currency)
    print("Calkowity koszt trasy z oplatami:", round(full_cost, 2), currency)

    with open("historia.txt", "a", encoding="utf-8") as file:
        file.write(f"Trasa: {start_city} -> {end_city}\n")
        file.write(f"Ciezarowka: {truck}\n")
        file.write(f"Dystans: {distance} km\n")
        file.write(f"Zuzyte paliwo: {fuel_used:.2f} l\n")
        file.write(f"Koszt calkowity: {full_cost_pln:.2f} zl\n")
        file.write(f"Koszt w walucie: {full_cost:.2f} {currency}\n")
        file.write("--------------------------\n")

    print("Trasa zostala zapisana w historii!")

show_menu()
menu = str(get_valid_choice("Wybierz opcje (1-6): ", 1, 6))

if menu == "2":
    show_history()
    exit()

elif menu == "3":
    print("Do zobaczenia!")
    exit()

elif menu == "4":
    show_statistics()
    exit()

elif menu == "5":
    compare_trucks()
    exit()

elif menu == "6":
    compare_costs()
    exit()

elif menu == "1":
    calculate_route()
    exit()  