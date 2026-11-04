import customtkinter as ctk
from datetime import datetime

# Ustawienia wyglądu aplikacji
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# --- PROFESJONALNA BAZA DANYCH POJAZDÓW V7.2 ---
TRUCKS_DB = {
    "Scania": {
        "Scania 143 Streamline (Klasyk)": {
            "engines": ["14.2L V8 - 400 KM", "14.2L V8 - 450 KM", "14.2L V8 - 500 KM"], 
            "axles": ["4x2", "6x2"], 
            "base_burn": 34.0
        },
        "Scania R-series (Gen 4 / 2004)": {
            "engines": ["11L - 340 KM", "12L - 420 KM", "16L V8 - 500 KM", "16L V8 - 580 KM"], 
            "axles": ["4x2", "6x2", "6x4"], 
            "base_burn": 30.5
        },
        "Scania R Streamline (2013)": {
            "engines": ["13L - 410 KM", "13L - 450 KM", "13L - 500 KM", "16L V8 - 580 KM", "16L V8 - 730 KM"], 
            "axles": ["4x2", "6x2"], 
            "base_burn": 27.5
        },
        "Scania S Next Gen (Nowa)": {
            "engines": ["13L - 410 KM", "13L - 450 KM", "13L - 500 KM", "13L - 540 KM", "16L V8 - 530 KM", "16L V8 - 590 KM", "16L V8 - 660 KM", "16L V8 - 770 KM"], 
            "axles": ["4x2", "6x2", "6x4"], 
            "base_burn": 26.0
        }
    },
    "Volvo": {
        "Volvo F12 (Klasyk lat 90.)": {
            "engines": ["12L - 320 KM", "12L - 360 KM", "12L - 400 KM"], 
            "axles": ["4x2", "6x2"], 
            "base_burn": 35.0
        },
        "Volvo FH12 (Gen 1 - 1993)": {
            "engines": ["12L - 340 KM", "12L - 380 KM", "12L - 420 KM", "12L - 460 KM"], 
            "axles": ["4x2", "6x2", "6x4"], 
            "base_burn": 32.0
        },
        "Volvo FH16 (Gen 3 - 2012)": {
            "engines": ["16L - 540 KM", "16L - 600 KM", "16L - 700 KM", "16L - 750 KM (Flagowiec)"], 
            "axles": ["6x4", "8x4"], 
            "base_burn": 33.0
        },
        "Volvo FH Aero (Najnowsza)": {
            "engines": ["13L - 420 KM", "13L - 460 KM", "13L - 500 KM", "13L - 540 KM", "17L - 600 KM", "17L - 700 KM", "17L - 780 KM"], 
            "axles": ["4x2", "6x2", "6x4"], 
            "base_burn": 25.2
        }
    },
    "MAN": {
        "MAN F2000 (Klasyk)": {
            "engines": ["10L - 370 KM", "12L - 400 KM", "12L - 460 KM"], 
            "axles": ["4x2", "6x2"], 
            "base_burn": 33.5
        },
        "MAN TGX Euro 5 (2008)": {
            "engines": ["10.5L - 360 KM", "12.4L - 400 KM", "12.4L - 440 KM", "12.4L - 480 KM", "15.2L V8 - 680 KM"], 
            "axles": ["4x2", "6x2", "6x4"], 
            "base_burn": 29.0
        },
        "MAN TGX EfficientLine (Euro 6)": {
            "engines": ["12.4L - 400 KM", "12.4L - 440 KM", "12.4L - 480 KM"], 
            "axles": ["4x2", "6x2"], 
            "base_burn": 26.0
        },
        "MAN TGX GX (Nowa generacja)": {
            "engines": ["12.4L - 360 KM", "12.4L - 400 KM", "12.4L - 440 KM", "12.4L - 480 KM", "12.4L - 520 KM", "15.2L - 640 KM"], 
            "axles": ["4x2", "6x2", "6x4"], 
            "base_burn": 24.5
        }
    },
    "Mercedes-Benz": {
        "Mercedes SK (Klasyk lat 90.)": {
            "engines": ["V6 - 340 KM", "V8 - 400 KM", "V8 - 480 KM"], 
            "axles": ["4x2", "6x4"], 
            "base_burn": 36.0
        },
        "Mercedes Actros MP2 / MP3": {
            "engines": ["12L - 320 KM", "12L - 360 KM", "12L - 400 KM", "12L - 440 KM", "16L V8 - 500 KM", "16L V8 - 550 KM", "16L V8 - 600 KM"], 
            "axles": ["4x2", "6x2"], 
            "base_burn": 31.0
        },
        "Mercedes Actros MP4": {
            "engines": ["10.7L - 320 KM", "10.7L - 360 KM", "12.8L - 420 KM", "12.8L - 450 KM", "12.8L - 510 KM", "15.6L - 580 KM", "15.6L - 625 KM"], 
            "axles": ["4x2", "6x2", "6x4"], 
            "base_burn": 27.0
        },
        "Mercedes Actros L (Najnowsza)": {
            "engines": ["12.8L - 420 KM", "12.8L - 450 KM", "12.8L - 480 KM", "12.8L - 530 KM (Gen 3 OM471)"], 
            "axles": ["4x2", "6x2"], 
            "base_burn": 24.8
        }
    },
    "DAF": {
        "DAF 95 XF (Klasyk)": {
            "engines": ["12.6L - 380 KM", "12.6L - 430 KM", "12.6L - 480 KM"], 
            "axles": ["4x2", "6x2"], 
            "base_burn": 33.0
        },
        "DAF XF 105": {
            "engines": ["12.9L - 410 KM", "12.9L - 460 KM", "12.9L - 510 KM"], 
            "axles": ["4x2", "6x2"], 
            "base_burn": 28.5
        },
        "DAF XF Euro 6": {
            "engines": ["10.8L - 400 KM", "10.8L - 440 KM", "12.9L - 480 KM", "12.9L - 510 KM"], 
            "axles": ["4x2", "6x2"], 
            "base_burn": 26.5
        },
        "DAF XG+ (Nowa generacja)": {
            "engines": ["10.8L - 370 KM", "10.8L - 410 KM", "10.8L - 450 KM", "12.9L - 480 KM", "12.9L - 530 KM"], 
            "axles": ["4x2", "6x2"], 
            "base_burn": 23.8
        }
    },
    "Renault": {
        "Renault Magnum (Legenda)": {
            "engines": ["12L Mack - 390 KM", "12L Mack - 430 KM", "12L Mack - 480 KM", "13L DXi - 460 KM", "13L DXi - 520 KM"], 
            "axles": ["4x2", "6x2"], 
            "base_burn": 32.5
        },
        "Renault Premium": {
            "engines": ["11L DXi - 370 KM", "11L DXi - 410 KM", "11L DXi - 450 KM"], 
            "axles": ["4x2", "6x2"], 
            "base_burn": 28.0
        },
        "Renault T High (Nowa generacja)": {
            "engines": ["11L - 380 KM", "11L - 430 KM", "13L - 440 KM", "13L - 480 KM", "13L - 520 KM"], 
            "axles": ["4x2", "6x2"], 
            "base_burn": 25.0
        }
    }
}

CARGO_MODIFIERS = {
    "Na pusto (0t)": -3.5,
    "Częściowy ładunek (~10t)": -1.2,
    "Pełny ładunek standard (~24t)": +3.0,
    "Gabaryt / Przeładowany (>28t)": +6.0
}

class TruckCalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Truck Cost Calculator - Professional Fleet Edition [V7.2]")
        self.geometry("1200x850")
        self.minsize(980, 700)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=15, pady=15)

        self.create_sidebar()
        
        self.content = ctk.CTkFrame(self.main_frame)
        self.content.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.show_welcome_screen()

    def create_sidebar(self):
        sidebar = ctk.CTkFrame(self.main_frame, width=220)
        sidebar.pack(side="left", fill="y", padx=10, pady=10)
        sidebar.pack_propagate(False)

        logo = ctk.CTkLabel(
            sidebar,
            text="TRUCK COST\nCALCULATOR\n[PRO V7.2]",
            font=("Arial", 16, "bold")
        )
        logo.pack(pady=30)

        ctk.CTkButton(sidebar, text="Nowa trasa", command=lambda: self.show_page("Nowa trasa")).pack(padx=15, pady=10, fill="x")
        ctk.CTkButton(sidebar, text="Historia tras", command=lambda: self.show_page("Historia tras")).pack(padx=15, pady=10, fill="x")
        ctk.CTkButton(sidebar, text="Statystyki", command=lambda: self.show_page("Statystyki")).pack(padx=15, pady=10, fill="x")
        ctk.CTkButton(sidebar, text="Baza pojazdów", command=lambda: self.show_page("Baza pojazdów")).pack(padx=15, pady=10, fill="x")

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        self.clear_content()
        welcome = ctk.CTkLabel(
            self.content,
            text="Witaj w Truck Cost Calculator (V7.2 Pro)!\nWybierz opcję z menu po lewej stronie.",
            font=("Arial", 20, "bold"),
            justify="left"
        )
        welcome.pack(pady=50, padx=30, anchor="w")

    def show_page(self, page_name):
        self.clear_content()

        page_title = ctk.CTkLabel(
            self.content,
            text=page_name,
            font=("Arial", 22, "bold")
        )
        page_title.pack(pady=15, anchor="w", padx=20)

        # ================= 1. NOWA TRASA =================
        if page_name == "Nowa trasa":
            form_frame = ctk.CTkScrollableFrame(self.content, width=840, height=560)
            form_frame.pack(padx=20, pady=10, fill="both", expand=True)

            ctk.CTkLabel(form_frame, text="KREATOR POJAZDU I ZESTAWU", font=("Arial", 14, "bold"), text_color="#1f6aa5").pack(anchor="w", padx=10, pady=(5,10))

            ctk.CTkLabel(form_frame, text="Marka pojazdu:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(5,0))
            brand_cb = ctk.CTkComboBox(form_frame, values=list(TRUCKS_DB.keys()), width=350, state="readonly")
            brand_cb.set("Scania")
            brand_cb.pack(anchor="w", padx=10, pady=5)

            ctk.CTkLabel(form_frame, text="Model pojazdu:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(5,0))
            model_cb = ctk.CTkComboBox(form_frame, values=[], width=350, state="readonly")
            model_cb.pack(anchor="w", padx=10, pady=5)

            ctk.CTkLabel(form_frame, text="Wybierz silnik i moc:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(5,0))
            engine_cb = ctk.CTkComboBox(form_frame, values=[], width=350, state="readonly")
            engine_cb.pack(anchor="w", padx=10, pady=5)

            ctk.CTkLabel(form_frame, text="Konfiguracja osi:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(5,0))
            axle_cb = ctk.CTkComboBox(form_frame, values=[], width=200, state="readonly")
            axle_cb.pack(anchor="w", padx=10, pady=5)

            ctk.CTkLabel(form_frame, text="Bazowe spalanie (l/100km - automatyczne dla modelu):", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(5,0))
            entry_base_burn = ctk.CTkEntry(form_frame, width=200)
            entry_base_burn.pack(anchor="w", padx=10, pady=5)

            def update_models(choice):
                models_list = list(TRUCKS_DB[choice].keys())
                model_cb.configure(values=models_list)
                if models_list:
                    model_cb.set(models_list[0])
                    update_specs(models_list[0])

            def update_specs(choice):
                current_brand = brand_cb.get()
                if current_brand in TRUCKS_DB and choice in TRUCKS_DB[current_brand]:
                    model_data = TRUCKS_DB[current_brand][choice]
                    
                    engines = model_data["engines"]
                    engine_cb.configure(values=engines)
                    engine_cb.set(engines[0])

                    axles = model_data["axles"]
                    axle_cb.configure(values=axles)
                    axle_cb.set(axles[0])

                    entry_base_burn.delete(0, "end")
                    entry_base_burn.insert(0, str(model_data["base_burn"]))

            brand_cb.configure(command=update_models)
            model_cb.configure(command=update_specs)

            update_models("Scania")

            ctk.CTkLabel(form_frame, text="Stan / Waga ładunku (wpływa na spalanie):", font=("Arial", 14, "bold"), text_color="#1f6aa5").pack(anchor="w", padx=10, pady=(15,10))
            cargo_cb = ctk.CTkComboBox(form_frame, values=list(CARGO_MODIFIERS.keys()), width=350, state="readonly")
            cargo_cb.set("Częściowy ładunek (~10t)")
            cargo_cb.pack(anchor="w", padx=10, pady=5)

            ctk.CTkLabel(form_frame, text="PARAMETRY TRASY I KOSZTY", font=("Arial", 14, "bold"), text_color="#1f6aa5").pack(anchor="w", padx=10, pady=(20,10))

            ctk.CTkLabel(form_frame, text="Miejscowość początkowa:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(5,0))
            entry_start = ctk.CTkEntry(form_frame, width=350, placeholder_text="np. Madryt")
            entry_start.pack(anchor="w", padx=10, pady=5)

            ctk.CTkLabel(form_frame, text="Miejscowość docelowa:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(5,0))
            entry_end = ctk.CTkEntry(form_frame, width=350, placeholder_text="np. Warszawa")
            entry_end.pack(anchor="w", padx=10, pady=5)

            ctk.CTkLabel(form_frame, text="Waluta rozliczeniowa:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(5,0))
            currency_cb = ctk.CTkComboBox(form_frame, values=["PLN", "EUR", "CZK"], width=150, state="readonly")
            currency_cb.set("PLN")
            currency_cb.pack(anchor="w", padx=10, pady=5)

            ctk.CTkLabel(form_frame, text="Kurs waluty (dla PLN = 1.0):", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(5,0))
            entry_rate = ctk.CTkEntry(form_frame, width=150)
            entry_rate.insert(0, "1.0")
            entry_rate.pack(anchor="w", padx=10, pady=5)

            ctk.CTkLabel(form_frame, text="Dystans trasy (km):", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(5,0))
            entry_dist = ctk.CTkEntry(form_frame, width=350)
            entry_dist.pack(anchor="w", padx=10, pady=5)

            ctk.CTkLabel(form_frame, text="Cena paliwa za litr:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(5,0))
            entry_fprice = ctk.CTkEntry(form_frame, width=350)
            entry_fprice.pack(anchor="w", padx=10, pady=5)

            ctk.CTkLabel(form_frame, text="Koszt opłat drogowych (myto):", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(5,0))
            entry_road = ctk.CTkEntry(form_frame, width=350)
            entry_road.insert(0, "0")
            entry_road.pack(anchor="w", padx=10, pady=5)

            ctk.CTkLabel(form_frame, text="Dodatkowe koszty (kierowca, przeprawy itp.):", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(5,0))
            entry_extra = ctk.CTkEntry(form_frame, width=350)
            entry_extra.insert(0, "0")
            entry_extra.pack(anchor="w", padx=10, pady=5)

            result_box = ctk.CTkTextbox(form_frame, width=760, height=220, font=("Arial", 12))
            result_box.pack(anchor="w", padx=10, pady=15)
            result_box.insert("0.0", "Wybierz model, silnik, uzupełnij trasę i kliknij 'Oblicz trasę'.")
            result_box.configure(state="disabled")

            def calculate_and_save():
                try:
                    brand = brand_cb.get()
                    model = model_cb.get()
                    engine = engine_cb.get()
                    axle = axle_cb.get()
                    cargo = cargo_cb.get()

                    base_consumption = float(entry_base_burn.get().replace(",", "."))
                    modifier = CARGO_MODIFIERS[cargo]
                    real_consumption = round(base_consumption + modifier, 2)
                    
                    start = entry_start.get().strip() or "Nieznana"
                    end = entry_end.get().strip() or "Nieznana"
                    currency = currency_cb.get()
                    exchange_rate = float(entry_rate.get().replace(",", "."))
                    distance = float(entry_dist.get().replace(",", "."))
                    fuel_price = float(entry_fprice.get().replace(",", "."))
                    road_cost = float(entry_road.get().replace(",", "."))
                    extra_cost = float(entry_extra.get().replace(",", "."))

                    if distance <= 0 or fuel_price < 0 or exchange_rate <= 0 or base_consumption <= 0:
                        raise ValueError("Błędne wartości liczbowe!")

                    fuel_used = distance * real_consumption / 100
                    fuel_cost = fuel_used * fuel_price
                    full_cost = fuel_cost + road_cost + extra_cost
                    full_cost_pln = full_cost * exchange_rate
                    cost_per_km = fuel_cost / distance

                    res_text = (
                        f"=== PROFESJONALNY RAPORT ZESTAWU (V7.2) ===\n"
                        f"Pojazd: {brand} {model}\n"
                        f"Wybrany silnik: {engine} | Osie: {axle}\n"
                        f"Ładunek: {cargo} | Spalanie bazowe: {base_consumption} l/100km\n"
                        f"Spalanie rzeczywiste (z ładunkiem): {real_consumption} l/100km\n"
                        f"Trasa: {start} -> {end} ({distance} km)\n"
                        f"Zużyte paliwo: {fuel_used:.2f} l | Koszt paliwa: {fuel_cost:.2f} {currency}\n"
                        f"Opłaty (myto + inne): {road_cost + extra_cost:.2f} {currency}\n"
                        f"CAŁKOWITY KOSZT: {full_cost:.2f} {currency} ({full_cost_pln:.2f} PLN)\n"
                        f"Koszt paliwa na 1 km: {cost_per_km:.2f} {currency}"
                    )

                    result_box.configure(state="normal")
                    result_box.delete("0.0", "end")
                    result_box.insert("0.0", res_text)
                    result_box.configure(state="disabled")

                    with open("historia.txt", "a", encoding="utf-8") as file:
                        file.write(f"Trasa: {start} -> {end} ({brand} {model}, {engine})\n")
                        file.write(f"Ciezarowka: {brand} {model} [{engine}]\n")
                        file.write(f"Dystans: {distance} km\n")
                        file.write(f"Zuzyte paliwo: {fuel_used:.2f} l\n")
                        file.write(f"Koszt calkowity: {full_cost_pln:.2f} zl\n")
                        file.write(f"Koszt w walucie: {full_cost:.2f} {currency}\n")
                        file.write("--------------------------\n")

                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    report_filename = f"raport_v7_{start}_{end}_{timestamp}.txt".replace(" ", "_")
                    with open(report_filename, "w", encoding="utf-8") as rep_file:
                        rep_file.write(res_text + f"\n\nWygenerowano przez Truck Cost Calculator V7.2 Pro")

                except ValueError:
                    result_box.configure(state="normal")
                    result_box.delete("0.0", "end")
                    result_box.insert("0.0", "BŁĄD: Sprawdź poprawność danych liczbowych w polach.")
                    result_box.configure(state="disabled")

            btn_calc = ctk.CTkButton(form_frame, text="Oblicz trasę i zapisz raport", fg_color="green", hover_color="darkgreen", command=calculate_and_save)
            btn_calc.pack(anchor="w", padx=10, pady=15)

        # ================= 2. HISTORIA TRAS =================
        elif page_name == "Historia tras":
            history_frame = ctk.CTkFrame(self.content)
            history_frame.pack(padx=20, pady=10, fill="both", expand=True)

            txt_history = ctk.CTkTextbox(history_frame, width=800, height=480, font=("Arial", 12))
            txt_history.pack(padx=10, pady=10, fill="both", expand=True)
            
            try:
                with open("historia.txt", "r", encoding="utf-8") as f:
                    txt_history.insert("0.0", f.read())
            except FileNotFoundError:
                txt_history.insert("0.0", "Historia tras jest jeszcze pusta. Wykonaj pierwszą kalkulację!")
            txt_history.configure(state="disabled")

            def clear_history():
                with open("historia.txt", "w", encoding="utf-8") as f:
                    f.write("")
                txt_history.configure(state="normal")
                txt_history.delete("0.0", "end")
                txt_history.insert("0.0", "Historia została wyczyszczona.")
                txt_history.configure(state="disabled")

            btn_clear = ctk.CTkButton(history_frame, text="Wyczyść historię", fg_color="darkred", hover_color="maroon", command=clear_history)
            btn_clear.pack(anchor="w", padx=10, pady=10)

        # ================= 3. STATYSTYKI =================
        elif page_name == "Statystyki":
            stats_box = ctk.CTkTextbox(self.content, width=800, height=520, font=("Arial", 13))
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

                avg_burn = (total_fuel / total_distance * 100) if total_distance > 0 else 0.0

                stats_text = (
                    f"=== STATYSTYKI OPERACYJNE FLOTY (V7.2) ===\n\n"
                    f"• Liczba wykonanych tras: {trips}\n"
                    f"• Łączny dystans floty: {total_distance:.2f} km\n"
                    f"• Łączne zużycie paliwa: {total_fuel:.2f} l\n"
                    f"• Średnie spalanie floty: {avg_burn:.2f} l / 100 km\n"
                    f"• Sumaryczny koszt operacyjny: {total_cost:.2f} zł\n"
                )
                stats_box.insert("0.0", stats_text)
            except FileNotFoundError:
                stats_box.insert("0.0", "Brak danych statystycznych. Oblicz trasę w pierwszym zakładzie.")
            stats_box.configure(state="disabled")

        # ================= 4. BAZA POJAZDÓW =================
        elif page_name == "Baza pojazdów":
            db_box = ctk.CTkTextbox(self.content, width=800, height=520, font=("Arial", 12))
            db_box.pack(padx=20, pady=10, fill="both", expand=True)

            db_report = "=== KATALOG DOSTĘPNYCH POJAZDÓW I SILNIKÓW (V7.2) ===\n\n"
            for brand, models in TRUCKS_DB.items():
                db_report += f"[{brand}]\n"
                for m_name, m_info in models.items():
                    db_report += f"  • {m_name}\n"
                    db_report += f"    - Dostępne silniki: {', '.join(m_info['engines'])}\n"
                    db_report += f"    - Opcje osi: {', '.join(m_info['axles'])}\n"
                    db_report += f"    - Bazowe spalanie: {m_info['base_burn']} l/100km\n"
                db_report += "\n"

            db_box.insert("0.0", db_report)
            db_box.configure(state="disabled")

if __name__ == "__main__":
    app = TruckCalculatorApp()
    app.mainloop()