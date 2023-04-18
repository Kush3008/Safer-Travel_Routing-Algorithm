import gmplot
import pandas as pd
import webbrowser

apikey = 'AIzaSyC_XVkaoiYS4sfRPC4aoYcDvPADxxVeNfA'

def draw_polygon():
    longitudes = []
    latitudes = []
    area = pd.read_csv('C:\\Users\\akush\\Desktop\\Medelin\\ST0245\\code\\final-delivery\\src\\data\\poligono_de_medellin.csv', sep=';')
    polygon = str(area['geometry'].to_list()[0])[9:-2].split(',')
    for coordinates in polygon:
        long, lat = list(map(float, coordinates[1:].split(' ')))
        longitudes.append(long)
        latitudes.append(lat)
    return latitudes, longitudes

def assign_coordinates(path):
    lat = []
    long = []
    for coord in path:
        lat, long = zip(*path)
    return lat, long

def draw_map(path1):
    limit_latitude, limit_longitude = draw_polygon()
    lat1, long1 = assign_coordinates(path1)

    gmp_draw = gmplot.GoogleMapPlotter(6.267203842477565, -75.579710387, 10, apikey=apikey)
    gmp_draw.polygon(limit_latitude, limit_longitude, face_color='white', face_alpha=0.4, edge_color='grey',
                     edge_width=5)
    gmp_draw.scatter(lat1, long1, 'green', size=3, marker=False)
    gmp_draw.plot(lat1, long1, 'green', edge_width=4)
    gmp_draw.marker(lat1[0], long1[0], label='A', color='blue')
    gmp_draw.marker(lat1[-1], long1[-1], label='B', color='red')

    gmp_draw.draw('map.html')
    webbrowser.open_new_tab('map.html')


def draw_map(path1, path2):
    limit_latitude, limit_longitude = draw_polygon()
    lat1, long1 = assign_coordinates(path1)
    lat2, long2 = assign_coordinates(path2)

    gmp_draw = gmplot.GoogleMapPlotter(28.6128946, 77.229446, 10, apikey=apikey)
    gmp_draw.polygon(limit_latitude, limit_longitude, face_color='white', face_alpha=0.4, edge_color='grey',
                     edge_width=5)
    gmp_draw.scatter(lat1, long1, 'green', size=3, marker=False)
    gmp_draw.plot(lat1, long1, 'green', edge_width=4)
    gmp_draw.scatter(lat2, long2, 'blue', size=3, marker=False)
    gmp_draw.plot(lat2, long2, 'blue', edge_width=4)
    gmp_draw.marker(lat1[0], long1[0], label='A', color='blue')
    gmp_draw.marker(lat1[-1], long1[-1], label='B', color='red')

    gmp_draw.draw('map.html')
    webbrowser.open_new_tab('map.html')

def draw_map(path1, path2, path3):
    limit_latitude, limit_longitude = draw_polygon()
    lat1, long1 = assign_coordinates(path1)
    lat2, long2 = assign_coordinates(path2)
    lat3, long3 = assign_coordinates(path3)

    gmp_draw = gmplot.GoogleMapPlotter(28.6128946, 77.229446, 10, apikey=apikey)
    gmp_draw.polygon(limit_latitude, limit_longitude, face_color='white', face_alpha=0.4, edge_color='grey',
                     edge_width=5)
    gmp_draw.scatter(lat1, long1, 'green', size=3, marker=False)
    gmp_draw.plot(lat1, long1, 'green', edge_width=4)
    gmp_draw.scatter(lat2, long2, 'blue', size=3, marker=False)
    gmp_draw.plot(lat2, long2, 'blue', edge_width=4)
    gmp_draw.scatter(lat3, long3, 'red', size=3, marker=False)
    gmp_draw.plot(lat3, long3, 'red', edge_width=4)
    gmp_draw.marker(lat1[0], long1[0], label='A', color='blue')
    gmp_draw.marker(lat1[-1], long1[-1], label='B', color='red')

    gmp_draw.draw('map.html')
    webbrowser.open_new_tab('map.html')