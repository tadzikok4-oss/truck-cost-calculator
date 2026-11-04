import customtkinter as ctk

# Ustawienia wygladu
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Słownik ciężarówek i ich spalania
TRUCKS = {
    "MAN TGX": 25,
    "Scania S770": 29,
    "Mercedes Actros": 27,
    "Volvo FH16": 28,
    "DAF XG+": 24,
    "Renault T": 25
}

# Glowne okno
app = ctk.CTk()
app.title("Truck Cost Calculator - V5")
app.geometry("1150x750")
app.minsize(950, 650)

# Glowny kontener
main_frame = ctk.CTkFrame(app)
main_frame.pack(fill="both", expand=True, padx=15, pady=15)

def show_page(page_name):
    # Usuwamy poprzednia zawartosc z obszaru roboczego
    for widget in content.winfo_children():
        widget.destroy()

    # Tytuł aktywnej strony
    page_title = ctk.CTkLabel(
        content,
        text=page_name,
        font=("Arial", 22, "bold")
    )
    page_title.pack(pady=15, anchor="w", padx=20)

    # ================= 1. NOWA TRASA =================
    if page_name == "Nowa trasa":
        form_frame = ctk.CTkScrollableFrame(content, width=800, height=520)
        form_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Pola formularza
        ctk.CTkLabel(form_frame, text="Wybierz ciężarówkę:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(5,0))
        truck_cb = ctk.CTkComboBox(form_frame, values=list(TRUCKS.keys()), width=300, state="readonly")
        truck_cb.set("MAN TGX")
        truck_cb.pack(anchor="w", padx=10, pady=5)

        ctk.CTkLabel(form_frame, text="Miejscowość początkowa:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10,0))
        entry_start = ctk.CTkEntry(form_frame, width=300, placeholder_text="np. Berlin")
        entry_start.pack(anchor="w", padx=10, pady=5)

        ctk.CTkLabel(form_frame, text="Miejscowość docelowa:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10,0))
        entry_end = ctk.CTkEntry(form_frame, width=300, placeholder_text="np. Warszawa")
        entry_end.pack(anchor="w", padx=10, pady=5)

        ctk.CTkLabel(form_frame, text="Waluta:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10,0))
        currency_cb = ctk.CTkComboBox(form_frame, values=["PLN", "EUR", "CZK"], width=150, state="readonly")
        currency_cb.set("PLN")
        currency_cb.pack(anchor="w", padx=10, pady=5)

        ctk.CTkLabel(form_frame, text="Kurs waluty (dla PLN wpisz 1.0, dla innych podaj kurs):", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10,0))
        entry_rate = ctk.CTkEntry(form_frame, width=150)
        entry_rate.insert(0, "1.0")
        entry_rate.pack(anchor="w", padx=10, pady=5)

        ctk.CTkLabel(form_frame, text="Dystans trasy (km):", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10,0))
        entry_dist = ctk.CTkEntry(form_frame, width=300)
        entry_dist.pack(anchor="w", padx=10, pady=5)

        ctk.CTkLabel(form_frame, text="Cena paliwa za litr:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10,0))
        entry_fprice = ctk.CTkEntry(form_frame, width=300)
        entry_fprice.pack(anchor="w", padx=10, pady=5)

        ctk.CTkLabel(form_frame, text="Koszt opłat drogowych (w wybranej walucie):", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10,0))
        entry_road = ctk.CTkEntry(form_frame, width=300)
        entry_road.insert(0, "0")
        entry_road.pack(anchor="w", padx=10, pady=5)

        # Wyniki po obliczeniu
        result_box = ctk.CTkTextbox(form_frame, width=700, height=180, font=("Arial", 12))
        result_box.pack(anchor="w", padx=10, pady=15)
        result_box.insert("0.0", "Uzupełnij dane i kliknij 'Oblicz trasę'.")
        result_box.configure(state="disabled")

        def calculate_and_save():
            try:
                truck = truck_cb.get()
                fuel_consumption = TRUCKS[truck]
                start = entry_start.get().strip() or "Nieznana"
                end = entry_end.get().strip() or "Nieznana"
                currency = currency_cb.get()
                exchange_rate = float(entry_rate.get().replace(",", "."))
                distance = float(entry_dist.get().replace(",", "."))
                fuel_price = float(entry_fprice.get().replace(",", "."))
                road_cost = float(entry_road.get().replace(",", "."))

                if distance <= 0 or fuel_price < 0 or exchange_rate <= 0:
                    raise ValueError("Wartości liczbowe muszą być poprawne!")

                fuel_used = distance * fuel_consumption / 100
                total_cost = fuel_used * fuel_price
                full_cost = total_cost + road_cost
                full_cost_pln = full_cost * exchange_rate
                round_trip_cost = total_cost * 2
                cost_per_km = total_cost / distance

                res_text = (
                    f"Trasa: {start} -> {end}\n"
                    f"Ciężarówka: {truck} ({fuel_consumption} l/100km)\n"
                    f"Zużyte paliwo: {fuel_used:.2f} l\n"
                    f"Koszt paliwa: {total_cost:.2f} {currency} (Łącznie z opłatami: {full_cost:.2f} {currency})\n"
                    f"Koszt w PLN: {full_cost_pln:.2f} zł | W obie strony: {round_trip_cost:.2f} {currency}\n"
                    f"Koszt paliwa na 1 km: {cost_per_km:.2f} {currency}"
                )

                result_box.configure(state="normal")
                result_box.delete("0.0", "end")
                result_box.insert("0.0", res_text)
                result_box.configure(state="disabled")

                # Zapis do pliku
                with open("historia.txt", "a", encoding="utf-8") as file:
                    file.write(f"Trasa: {start} -> {end}\n")
                    file.write(f"Ciezarowka: {truck}\n")
                    file.write(f"Dystans: {distance} km\n")
                    file.write(f"Zuzyte paliwo: {fuel_used:.2f} l\n")
                    file.write(f"Koszt calkowity: {full_cost_pln:.2f} zl\n")
                    file.write(f"Koszt w walucie: {full_cost:.2f} {currency}\n")
                    file.write("--------------------------\n")

            except ValueError:
                result_box.configure(state="normal")
                result_box.delete("0.0", "end")
                result_box.insert("0.0", "BŁĄD: Sprawdź poprawność wprowadzonych danych liczbowych!")
                result_box.configure(state="disabled")

        btn_calc = ctk.CTkButton(form_frame, text="Oblicz trasę i zapisz", fg_color="green", hover_color="darkgreen", command=calculate_and_save)
        btn_calc.pack(anchor="w", padx=10, pady=10)

    # ================= 2. HISTORIA TRAS =================
    elif page_name == "Historia tras":
        txt_history = ctk.CTkTextbox(content, width=780, height=500, font=("Arial", 12))
        txt_history.pack(padx=20, pady=10, fill="both", expand=True)
        try:
            with open("historia.txt", "r", encoding="utf-8") as f:
                txt_history.insert("0.0", f.read())
        except FileNotFoundError:
            txt_history.insert("0.0", "Historia tras jest jeszcze pusta. Oblicz swoją pierwszą trasę!")
        txt_history.configure(state="disabled")

    # ================= 3. STATYSTYKI =================
    elif page_name == "Statystyki":
        stats_box = ctk.CTkTextbox(content, width=780, height=500, font=("Arial", 13))
        stats_box.pack(padx=20, pady=10, fill="both", expand=True)

        try:
            with open("historia.txt", "r", encoding="utf-8") as file:
                history = file.read()

            trips = history.count("Ciezarowka:")
            total_distance = 0.0
            total_fuel = 0.0
            total_cost = 0.0

            for line in history.splitlines():
                if line.startswith("Dystans:"):
                    total_distance += float(line.split(":")[1].replace("km", "").strip())
                elif line.startswith("Zuzyte paliwo:"):
                    total_fuel += float(line.split(":")[1].replace("l", "").strip())
                elif line.startswith("Koszt calkowity:"):
                    total_cost += float(line.split(":")[1].replace("zl", "").strip())

            stats_text = (
                f"=== PODSUMOWANIE STATYSTYK ===\n\n"
                f"Liczba zapisanych tras: {trips}\n"
                f"Łączny pokonany dystans: {total_distance:.2f} km\n"
                f"Łączne zużycie paliwa: {total_fuel:.2f} l\n"
                f"Łączny koszt (w PLN): {total_cost:.2f} zł\n"
            )
            stats_box.insert("0.0", stats_text)
        except FileNotFoundError:
            stats_box.insert("0.0", "Brak historii tras. Oblicz chociaż jedną trasę, aby zobaczyć statystyki.")
        stats_box.configure(state="disabled")

    # ================= 4. PORÓWNAJ CIĘŻARÓWKI =================
    elif page_name == "Porownaj ciezarowki":
        trucks_box = ctk.CTkTextbox(content, width=780, height=500, font=("Arial", 13))
        trucks_box.pack(padx=20, pady=10, fill="both", expand=True)

        output = "===ZESTAWIENIE SPALANIA CIĘŻARÓWEK===\n\n"
        for name, burn in TRUCKS.items():
            output += f"• {name} — {burn} l / 100 km\n"

        best_truck = min(TRUCKS, key=TRUCKS.get)
        output += f"\nNajbardziej ekonomiczna ciężarówka: {best_truck} ({TRUCKS[best_truck]} l/100 km)"

        trucks_box.insert("0.0", output)
        trucks_box.configure(state="disabled")

    # ================= 5. PORÓWNAJ KOSZTY =================
    elif page_name == "Porownaj koszty":
        cost_frame = ctk.CTkScrollableFrame(content, width=800, height=520)
        cost_frame.pack(padx=20, pady=10, fill="both", expand=True)

        ctk.CTkLabel(cost_frame, text="Dystans próbny (km):", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(5,0))
        entry_cdist = ctk.CTkEntry(cost_frame, width=250)
        entry_cdist.insert(0, "1000")
        entry_cdist.pack(anchor="w", padx=10, pady=5)

        ctk.CTkLabel(cost_frame, text="Waluta:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10,0))
        ccurrency_cb = ctk.CTkComboBox(cost_frame, values=["PLN", "EUR", "CZK"], width=150, state="readonly")
        ccurrency_cb.set("PLN")
        ccurrency_cb.pack(anchor="w", padx=10, pady=5)

        ctk.CTkLabel(cost_frame, text="Kurs waluty (dla PLN = 1.0):", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10,0))
        entry_crate = ctk.CTkEntry(cost_frame, width=150)
        entry_crate.insert(0, "1.0")
        entry_crate.pack(anchor="w", padx=10, pady=5)

        ctk.CTkLabel(cost_frame, text="Cena paliwa za litr:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(10,0))
        entry_cprice = ctk.CTkEntry(cost_frame, width=250)
        entry_cprice.pack(anchor="w", padx=10, pady=5)

        c_result_box = ctk.CTkTextbox(cost_frame, width=700, height=200, font=("Arial", 12))
        c_result_box.pack(anchor="w", padx=10, pady=15)
        c_result_box.insert("0.0", "Wprowadź dane i kliknij 'Porównaj koszty'.")
        c_result_box.configure(state="disabled")

        def run_cost_comparison():
            try:
                dist = float(entry_cdist.get().replace(",", "."))
                curr = ccurrency_cb.get()
                rate = float(entry_crate.get().replace(",", "."))
                f_price = float(entry_cprice.get().replace(",", "."))

                if dist <= 0 or f_price < 0 or rate <= 0:
                    raise ValueError()

                report = f"Porównanie kosztów dla dystansu {dist} km:\n\n"
                for t_name, burn in TRUCKS.items():
                    fuel_used = dist * burn / 100
                    cost = fuel_used * f_price
                    cost_pln = cost * rate
                    report += f"{t_name}: {cost:.2f} {curr} ({cost_pln:.2f} PLN)\n"

                c_result_box.configure(state="normal")
                c_result_box.delete("0.0", "end")
                c_result_box.insert("0.0", report)
                c_result_box.configure(state="disabled")
            except ValueError:
                c_result_box.configure(state="normal")
                c_result_box.delete("0.0", "end")
                c_result_box.insert("0.0", "BŁĄD: Wprowadź poprawne wartości liczbowe.")
                c_result_box.configure(state="disabled")

        btn_run_compare = ctk.CTkButton(cost_frame, text="Porównaj koszty", fg_color="blue", command=run_cost_comparison)
        btn_run_compare.pack(anchor="w", padx=10, pady=10)

# Lewy panel nawigacyjny
sidebar = ctk.CTkFrame(main_frame, width=220)
sidebar.pack(side="left", fill="y", padx=10, pady=10)
sidebar.pack_propagate(False)

logo = ctk.CTkLabel(
    sidebar,
    text="TRUCK COST\nCALCULATOR",
    font=("Arial", 20, "bold")
)
logo.pack(pady=30)

# Przyciski menu
ctk.CTkButton(sidebar, text="Nowa trasa", command=lambda: show_page("Nowa trasa")).pack(padx=15, pady=10, fill="x")
ctk.CTkButton(sidebar, text="Historia tras", command=lambda: show_page("Historia tras")).pack(padx=15, pady=10, fill="x")
ctk.CTkButton(sidebar, text="Statystyki", command=lambda: show_page("Statystyki")).pack(padx=15, pady=10, fill="x")
ctk.CTkButton(sidebar, text="Porownaj ciezarowki", command=lambda: show_page("Porownaj ciezarowki")).pack(padx=15, pady=10, fill="x")
ctk.CTkButton(sidebar, text="Porownaj koszty", command=lambda: show_page("Porownaj koszty")).pack(padx=15, pady=10, fill="x")

# Glowny obszar roboczy
content = ctk.CTkFrame(main_frame)
content.pack(side="right", fill="both", expand=True, padx=10, pady=10)

welcome = ctk.CTkLabel(
    content,
    text="Witaj w Truck Cost Calculator!\nWybierz opcję z menu po lewej stronie.",
    font=("Arial", 20, "bold"),
    justify="left"
)
welcome.pack(pady=50, padx=30, anchor="w")

app.mainloop()