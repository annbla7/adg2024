import os
import csv
import math

path = os.path.join(os.path.expanduser("~"), "Documents", "algorytmy")
os.chdir(path)

profil_csv = "profil.csv"

def surface_distance(file):
    points = []
    with open(profil_csv, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            x, y, z = map(float, row[1:])
            points.append((x, y, z))
    total_distance = 0
    for i in range(len(points) - 1):
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[i + 1]
        total_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return round(total_distance, 2)

surface_distance(profil_csv)