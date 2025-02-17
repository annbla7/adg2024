wektor = "powiaty.gpkg"
powiaty = QgsVectorLayer(wektor, "powiaty", "ogr")

pola = [
    QgsField("ID", QVariant.Int),
    QgsField("centroid_x", QVariant.Double),
    QgsField("centroid_y", QVariant.Double)
]

centroidy = QgsVectorLayer("Point?crs=EPSG:4326", "centroidy", "memory")
provider = centroidy.dataProvider()

provider.addAttributes(pola)
centroidy.updateFields()

obiekty = powiaty.getFeatures()

for obiekt in obiekty:
    geometry = obiekt.geometry()
    if geometry.type() == 2:
        centroid = geometry.centroid()
        nowy_obiekt = QgsFeature()
        nowy_obiekt.setGeometry(centroid)
        nowy_obiekt.setAttributes([obiekt.id(), centroid.asPoint().x(), centroid.asPoint().y()])
        provider.addFeature(nowy_obiekt)


sciezka_do_zapisu = "centroidy.gpkg"

QgsVectorFileWriter.writeAsVectorFormat(centroidy, sciezka_do_zapisu, "UTF-8", centroidy.crs(), "GPKG")
