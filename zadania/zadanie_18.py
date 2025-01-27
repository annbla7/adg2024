import matplotlib.pyplot as plt

def transpozycja(wkt):
    geometry = QgsGeometry.fromWkt(wkt)
    geom_type = geometry.type()
    vertices = geometry.vertices()
    
    transponowane = []
    
    for vertex in vertices:
        new_x = vertex.y()
        new_y = vertex.x()
        transponowane.append(QgsPointXY(new_x, new_y))
    
    if geom_type == 0: #punkt
        return transponowane
    elif geom_type == 1: #linia
        new_geom = QgsGeometry.fromPolylineXY(transponowane)
    elif geom_type == 2: #poligon
        new_geom = QgsGeometry.fromPolygonXY([transponowane])
    return new_geom
    
    
def odbicie_pionowe(wkt, a):
    geometry = QgsGeometry.fromWkt(wkt)
    geom_type = geometry.type()
    vertices = geometry.vertices()
    
    odbite = []
    
    for vertex in vertices:
        new_x = 2 * a - vertex.x()
        new_y = vertex.y()
        odbite.append(QgsPointXY(new_x, new_y))
    if geom_type == 0:
        new_geom = QgsGeometry.fromPointXY(odbite)
    elif geom_type == 1:
        new_geom = QgsGeometry.fromPolylineXY(odbite)
    elif geom_type == 2:
        new_geom = QgsGeometry.fromPolygonXY([odbite])
    return new_geom


def geometry_to_coords(geometry):
    
    if isinstance(geometry, str):
        geometry = QgsGeometry.fromWkt(geometry)
    
    geom_type = geometry.type()
    
    if geom_type == 0:
        x, y = geometry.asPoint()
    elif geom_type == 1:
        points = geometry.asPolyline()
        x, y = zip(*points)
    elif geom_type == 2:
        points = geometry.asPolygon()
        for p in points:
            x, y = zip(*p)
    else:
        raise ValueError("Nieobsługiwana geometria!")
    
    return x, y


poligon = "POLYGON ((40 30, 60 30, 50 40, 40 30))"

transponowane = transpozycja(poligon)
odbite_pion = odbicie_pionowe(poligon, 3)

x1 = geometry_to_coords(poligon)[0]
y1 = geometry_to_coords(poligon)[1]
x2 = geometry_to_coords(transponowane)[0]
y2 = geometry_to_coords(transponowane)[1]
x3 = geometry_to_coords(odbite_pion)[0]
y3 = geometry_to_coords(odbite_pion)[1]


plt.figure(figsize = (4, 3))
plt.plot(x1, y1, color = "grey", linestyle = "dashed", zorder = 1, label = "Oryginalne")
plt.fill(x2, y2, color = "blue", zorder = 2, label = "Transpozycja")
plt.fill(x3, y3, color = "red", zorder = 2, label = "Odbicie pionowe")
plt.title("Transformacje geometrii")
plt.legend()
plt.show()

