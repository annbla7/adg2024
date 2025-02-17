from math import sin, cos, asin, sqrt, pi

pkt1 = (21.0122, 52.2296)
pkt2 = (12.5113, 41.8919)

pkt1 = QgsPointXY(pkt1[0], pkt1[1])
pkt2 = QgsPointXY(pkt2[0], pkt2[1])

def odleglosc_haversine(pkt1, pkt2):
    r = 6371009 #średni promień Ziemi w m
    coords = [pkt1.x(), pkt1.y(), pkt2.x(), pkt2.y()] #współrzędne
    coords = [coord * pi / 180 for coord in coords] #stopnie na radiany
    x1, y1, x2, y2 = coords
    cos_delta_x = cos(x2-x1)
    cos_delta_y =  cos(y2-y1)
    d_t = 1 - cos_delta_x + cos(x1) * cos(x2) * (1 - cos_delta_y)
    distance = 2 * r * asin(sqrt(d_t/2))
    distance = round(distance / 1000, 2) #wynik w km
    return distance

odleglosc_haversine(pkt1, pkt2)

#Odległość sferyczna (1315.51 km) jest najniższa, ponieważ zakłada, że Ziemia jest idealną kulą.
#Odległość elipsoidalna (1316.2 km) jest najdokładniejsza, biorąc pod uwagę rzeczywisty kształt Ziemi.
#Odległość Haversine (1449.78 km) jest największa, ponieważ metoda ta, mimo że jest bardziej precyzyjna od zwykłej sferycznej, wciąż nie uwzględnia elipsoidalnego kształtu Ziemi.
