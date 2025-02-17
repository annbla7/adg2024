# -*- coding: utf-8 -*-

def decimal_to_dms(decimal_str):
    decimal_str = decimal_str.replace("°", " ")
    parts = decimal_str.split()
    
    decimal = abs(float(parts[0]))
    direction = parts[1]
    
    degrees = int(decimal)
    minutes = int((decimal - degrees) * 60)
    seconds = round(((decimal - degrees) * 60 - minutes) * 60, 2)
    
    if direction in ["S", "W"]:
        degrees = -degrees
    
    dms = f"{degrees}°{minutes}'{seconds}\""
    return f"{dms} {direction}"


print(decimal_to_dms("-52.2296°W"))
print(decimal_to_dms("21.0122°E"))