raster = QgsRasterLayer("DEM.tif", "dem")
print(raster.isValid())

def oblicz_wielkosc_komorki(raster):
    zakres = raster.extent()
    liczba_kolumn = raster.width()
    liczba_wierszy = raster.height()
    szerokosc_komorki = zakres.width() / liczba_kolumn
    wysokosc_komorki = zakres.height() / liczba_wierszy
    return szerokosc_komorki, wysokosc_komorki

oblicz_wielkosc_komorki(raster)