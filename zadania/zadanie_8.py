import numpy as np

def oblicz_statystyki(obiekty, typ_geometrii):
    wartosci = []
    for obiekt in obiekty:
        geom = obiekt.geometry()
        if geom is not None:
            if typ_geometrii == "powierzchnia" and geom.type() == 2:
                wartosci.append(geom.area())
            elif typ_geometrii == "długość" and geom.type() == 1:
                wartosci.append(geom.length())
    # Statystyki opisowe
    srednia = np.mean(wartosci)
    minimum = np.min(wartosci)
    maksimum = np.max(wartosci)
    odchylenie = np.std(wartosci)
    liczba_wartosci = len(wartosci)
    return(f"Średnia: {srednia}, Min: {minimum}, Max: {maksimum}, Odchylenie: {odchylenie}, Liczba: {liczba_wartosci}")

sciezka_wektor = "powiaty.gpkg"

warstwa = QgsVectorLayer(sciezka_wektor, "wektor", "ogr")

obiekty = list(warstwa.getFeatures())

# Obliczenie statystyk dla powierzchni (poligony)
statystyki_powierzchni = oblicz_statystyki(obiekty, "powierzchnia")
print("Statystyki powierzchni:", statystyki_powierzchni)

# Obliczenie statystyk dla długości - potrzebna warstwa liniowa
statystyki_dlugosci = oblicz_statystyki(obiekty, "długość")
print("Statystyki długości:", statystyki_dlugosci)