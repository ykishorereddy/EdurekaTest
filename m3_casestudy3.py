import datetime
from math import radians, sin, cos, acos



def find_day_night():
    now = datetime.datetime.now()
    if now.hour > 20:
        print('Night Outside')
    else:
        print('Day Outside')

def distance(slat,slon,dlat,dlon):
    dist = 6371.01  * acos(sin(slat)*sin(dlat) + cos(slat)*cos(dlat)*cos(slon - dlon))
    print("The distance is %.2fkm." % dist)


if __name__ == "__main__":
    #casestudy #3
    find_day_night()
    #casestudy #4
    print("Input coordinates of two points:")
    slat = radians(float(input("Starting latitude: ")))
    slon = radians(float(input("Ending longitude: ")))
    dlat = radians(float(input("Starting latitude: ")))
    dlon = radians(float(input("Ending longitude: ")))
    distance(slat,slon,dlat,dlon)
