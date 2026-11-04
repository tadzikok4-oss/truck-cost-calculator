import streamlit as st
from datetime import datetime

# Konfiguracja strony
st.set_page_config(
    page_title="Truck Cost Calculator - Web Pro",
    page_icon="🚛",
    layout="wide"
)

# --- BAZA DANYCH POJAZDÓW V7.2 (WEB) ---
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

# Panel boczny (Nawigacja)
st.sidebar.title("TRUCK COST CALCULATOR")
st.sidebar.markdown("**Professional Fleet Edition [Web V1.0]**")
menu = st.sidebar.radio("Wybierz zakładkę:", ["Nowa trasa", "Historia tras", "Statystyki", "Baza pojazdów"])

# ================= 1. NOWA TRASA =================
if menu == "Nowa trasa":
    st.title("🚛 Kreator Trasy i Kalkulator Kosztów")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Konfiguracja Pojazdu")
        brand = st.selectbox("Marka pojazdu", list(TRUCKS_DB.keys()))
        models_list = list(TRUCKS_DB[brand].keys())
        model = st.selectbox("Model pojazdu", models_list)
        
        model_data = TRUCKS_DB[brand][model]
        engine = st.selectbox("Wybierz silnik i moc", model_data["engines"])
        axle = st.selectbox("Konfiguracja osi", model_data["axles"])
        
        base_burn = st.number_input("Bazowe spalanie (l/100km)", value=float(model_data["base_burn"]), step=0.1)
        cargo = st.selectbox("Stan / Waga ładunku", list(CARGO_MODIFIERS.keys()))

    with col2:
        st.subheader("Parametry Trasy i Koszty")
        start_city = st.text_input("Miejscowość początkowa", "Madryt")
        end_city = st.text_input("Miejscowość docelowa", "Warszawa")
        
        col_cur1, col_cur2 = st.columns(2)
        with col_cur1:
            currency = st.selectbox("Waluta", ["PLN", "EUR", "CZK"])
        with col_cur2:
            exchange_rate = st.number_input("Kurs waluty (dla PLN = 1.0)", value=1.0, step=0.01)
            
        distance = st.number_input("Dystans trasy (km)", value=1000.0, step=10.0)
        fuel_price = st.number_input("Cena paliwa za litr", value=6.50, step=0.05)
        road_cost = st.number_input("Koszt opłat drogowych (myto)", value=0.0, step=50.0)
        extra_cost = st.number_input("Dodatkowe koszty (kierowca, przeprawy)", value=0.0, step=50.0)

    st.markdown("---")
    
    if st.button("Oblicz trasę i zapisz raport", type="primary", use_container_width=True):
        if distance <= 0 or fuel_price < 0 or exchange_rate <= 0:
            st.error("BŁĄD: Sprawdź poprawność wprowadzonych wartości liczbowych!")
        else:
            modifier = CARGO_MODIFIERS[cargo]
            real_consumption = round(base_burn + modifier, 2)
            
            fuel_used = distance * real_consumption / 100
            fuel_cost = fuel_used * fuel_price
            full_cost = fuel_cost + road_cost + extra_cost
            full_cost_pln = full_cost * exchange_rate
            cost_per_km = fuel_cost / distance

            st.success("Obliczenia wykonane pomyślnie!")
            
            # Wyświetlenie raportu w kafelkach
            rcol1, rcol2, rcol3 = st.columns(3)
            rcol1.metric("Zużyte paliwo", f"{fuel_used:.2f} l")
            rcol2.metric("Całkowity koszt", f"{full_cost:.2f} {currency}", f"{full_cost_pln:.2f} PLN")
            rcol3.metric("Koszt paliwa / km", f"{cost_per_km:.2f} {currency}")

            res_text = (
                f"=== PROFESJONALNY RAPORT ZESTAWU (Web V1.0) ===\n"
                f"Pojazd: {brand} {model}\n"
                f"Wybrany silnik: {engine} | Osie: {axle}\n"
                f"Ładunek: {cargo} | Spalanie bazowe: {base_burn} l/100km\n"
                f"Spalanie rzeczywiste (z ładunkiem): {real_consumption} l/100km\n"
                f"Trasa: {start_city} -> {end_city} ({distance} km)\n"
                f"Zużyte paliwo: {fuel_used:.2f} l | Koszt paliwa: {fuel_cost:.2f} {currency}\n"
                f"Opłaty (myto + inne): {road_cost + extra_cost:.2f} {currency}\n"
                f"CAŁKOWITY KOSZT: {full_cost:.2f} {currency} ({full_cost_pln:.2f} PLN)\n"
                f"Koszt paliwa na 1 km: {cost_per_km:.2f} {currency}"
            )

            # Zapis do historii
            with open("historia.txt", "a", encoding="utf-8") as file:
                file.write(f"Trasa: {start_city} -> {end_city} ({brand} {model}, {engine})\n")
                file.write(f"Ciezarowka: {brand} {model} [{engine}]\n")
                file.write(f"Dystans: {distance} km\n")
                file.write(f"Zuzyte paliwo: {fuel_used:.2f} l\n")
                file.write(f"Koszt calkowity: {full_cost_pln:.2f} zl\n")
                file.write(f"Koszt w walucie: {full_cost:.2f} {currency}\n")
                file.write("--------------------------\n")

            st.text_area("Szczegółowy raport tekstowy:", res_text, height=200)

# ================= 2. HISTORIA TRAS =================
elif menu == "Historia tras":
    st.title("📜 Historia Trasa i Raportów")
    
    try:
        with open("historia.txt", "r", encoding="utf-8") as f:
            history_data = f.read()
        if history_data.strip():
            st.text_area("Zapisane trasy:", history_data, height=400)
            if st.button("Wyczyść historię", type="secondary"):
                with open("historia.txt", "w", encoding="utf-8") as f:
                    f.write("")
                st.rerun()
        else:
            st.info("Historia tras jest pusta. Oblicz pierwszą trasę w zakładce 'Nowa trasa'.")
    except FileNotFoundError:
        st.info("Brak pliku historii. Wykonaj pierwszą kalkulację!")

# ================= 3. STATYSTYKI =================
elif menu == "Statystyki":
    st.title("📊 Statystyki Operacyjne Floty")
    
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

        sc1, sc2, sc3 = st.columns(3)
        sc1.metric("Liczba tras", trips)
        sc2.metric("Łączny dystans", f"{total_distance:.2f} km")
        sc3.metric("Średnie spalanie floty", f"{avg_burn:.2f} l/100km")

        st.metric("Sumaryczny koszt operacyjny", f"{total_cost:.2f} PLN")

    except FileNotFoundError:
        st.info("Brak danych statystycznych. Oblicz trasę w pierwszym zakładzie.")

# ================= 4. BAZA POJAZDÓW =================
elif menu == "Baza pojazdów":
    st.title("📚 Katalog Pojazdów i Silników")
    
    for brand, models in TRUCKS_DB.items():
        with st.expander(f"Marka: {brand}"):
            for m_name, m_info in models.items():
                st.markdown(f"**{m_name}**")
                st.write(f"- Dostępne silniki: {', '.join(m_info['engines'])}")
                st.write(f"- Opcje osi: {', '.join(m_info['axles'])}")
                st.write(f"- Bazowe spalanie: {m_info['base_burn']} l/100km")
                st.markdown("---")