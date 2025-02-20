# -*- coding: utf-8 -*-

def decimal_to_dms(decimal_znak, is_lat = True):
    if is_lat:
        if decimal_znak >= 0:
            direction = "N"
        else:
            direction = "S"
    else:
        if decimal_znak >= 0:
            direction = "E"
        else:
            direction = "W"
    decimal = abs(float(decimal_znak))
    degrees = int(decimal)
    minutes = int((decimal - degrees) * 60)
    seconds = round(((decimal - degrees) * 60 - minutes) * 60, 2)
    
    dms = f"{degrees}°{minutes}'{seconds}\""
    return f"{dms} {direction}"


print(decimal_to_dms(47.9274, is_lat = True)) #N
print(decimal_to_dms(-52.2296, is_lat = True)) #S
print(decimal_to_dms(21.0122, is_lat = False)) #E
print(decimal_to_dms(-6.1835, is_lat = False)) #W
