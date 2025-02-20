from math import sin, cos, asin, sqrt, pi

pkt1 = (21.0122, 52.2296)
pkt2 = (12.5113, 41.8919)

pkt1 = QgsPointXY(pkt1[0], pkt1[1])
pkt2 = QgsPointXY(pkt2[0], pkt2[1])

#Odległość Haversine

def odleglosc_haversine(pkt1, pkt2):
    r = 6371009 #średni promień Ziemi w m
    coords = [pkt1.x(), pkt1.y(), pkt2.x(), pkt2.y()] #współrzędne
    coords = [coord * pi / 180 for coord in coords] #stopnie na radiany
    x1, y1, x2, y2 = coords
    cos_delta_y = cos(y2-y1) #szerokość geograficzna
    cos_delta_x =  cos(x2-x1) #długość geograficzna
    d_t = 1 - cos_delta_y + cos(y1) * cos(y2) * (1 - cos_delta_x)
    distance = 2 * r * asin(sqrt(d_t/2))
    distance = round(distance / 1000, 2) #wynik w km
    return distance

print("Odległość Haversine między Warszawą a Rzymem:", odleglosc_haversine(pkt1, pkt2), "km")


#Odległość sferyczna (1315.51 km) zakłada, że Ziemia jest idealną kulą.
#Odległość elipsoidalna (1316.2 km) jest najdokładniejsza, biorąc pod uwagę rzeczywisty kształt Ziemi.
#Odległość Haversine (1315.51 km) jest taka sama jak odległość sferyczna, ponieważ również zakłada, że Ziemia jest kulą i nie uwzględnia jej spłaszczenia jak w przypadku metody elipsoidalnej.
