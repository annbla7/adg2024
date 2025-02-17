def wyswietl_metadane(warstwa):
    if isinstance(warstwa, QgsVectorLayer): # metadane dla warstwy wektorowej
        metadane = {
            "Typ warstwy": "Wektorowa",
            "Nazwa": warstwa.name(),
            "Typ geometrii": warstwa.geometryType(),
            "Zakres przestrzenny": warstwa.extent().toString(),
            "Liczba obiektów": warstwa.featureCount(),
            "Liczba atrybutów": warstwa.fields().count(),
            "CRS": warstwa.crs().authid()
        }
    elif isinstance(warstwa, QgsRasterLayer): # metadane dla warstwy rastrowej
        metadane = {
            "Typ warstwy": "Rastrowa",
            "Nazwa": warstwa.name(),
            "Rozdzielczość": f"{warstwa.width()} x {warstwa.height()} (kolumny x wiersze)",
            "Zakres przestrzenny": warstwa.extent().toString(),
            "CRS": warstwa.crs().authid()
        }
    else:
        metadane = {"Błąd": "Nieprawidłowy typ warstwy"}
        
    for klucz, wartosc in metadane.items():
        print(f"{klucz}: {wartosc}")
    print("\n")  # separator między warstwami

sciezka_wektor = "powiaty.gpkg"
sciezka_raster = "DEM.tif"

wektor = QgsVectorLayer(sciezka_wektor, "wektor", "ogr")
raster = QgsRasterLayer(sciezka_raster, "raster")

wyswietl_metadane(wektor)
wyswietl_metadane(raster)