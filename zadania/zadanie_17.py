import os
import math

path = os.path.join(os.path.expanduser("~"), "Documents", "algorytmy")
os.chdir(path)

filepath = os.path.join(path, "DEM.tif")
raster = QgsRasterLayer(filepath, "DEM")

def xy_from_colrow(raster, column, row):
    zasieg = raster.extent()
    x_min = zasieg.xMinimum()
    x_max = zasieg.xMaximum()
    y_min = zasieg.yMinimum()
    y_max = zasieg.yMaximum()
    x_res = raster.rasterUnitsPerPixelX()
    y_res = raster.rasterUnitsPerPixelY()
    #sprawdzenie czy parametry nie wychodzą poza zasięg rastra
    if column > x_max  or row > y_max:
        print("Parametry wychodzą poza zasięg rastra.")
    else:
        x = x_min + (column + 0.5) * x_res
        y = y_max - (row + 0.5) * y_res
    return x, y

xy_from_colrow(raster, 17, 30)


def colrow_from_xy(raster, x, y):
    zasieg = raster.extent()
    x_min = zasieg.xMinimum()
    x_max = zasieg.xMaximum()
    y_min = zasieg.yMinimum()
    y_max = zasieg.yMaximum()
    x_res = raster.rasterUnitsPerPixelX()
    y_res = raster.rasterUnitsPerPixelY()
    #sprawdzenie czy parametry nie wychodzą poza zasięg rastra
    if x > x_max  or y > y_max:
        print("Parametry wychodzą poza zasięg rastra.")
    else:
        column = math.floor((x - x_min) / x_res)
        row = math.floor((y_max - y) / y_res)
    return column, row
    
colrow_from_xy(raster, 4, 2)