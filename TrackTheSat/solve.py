import datetime
from skyfield.api import load, EarthSatellite, Topos

"""
Latitude: 19.8957
Longitude: 75.3203
Satellite: MAROC-TUBSAT
Start time GMT: 1585994946.924365
"""

"""
duty cycles between 2457 and 7372, from 0 to 180 degrees
"""

""" az , elev
N - 2457, 2457
E - 

"""

"""
ds = az * ((7372-2157)/180) + 2457
"""

def build_ts(time_num):
    return load.timescale()

def build_sat(sat_name):
    tle1, tle2 = sat_dict[sat_name]
    return EarthSatellite(tle1, tle2, sat_name)

def build_topos(lat, lon):
    return Topos(latitude_degrees=lat, longitude_degrees=lon)

sat_dict = {}

with open('Data/active.txt','r') as f:
    data = f.readlines()
    data = [l.replace('\n', "").rstrip() for l in data]

for index, line in enumerate(data[::3]):
    sat_dict[line] = data[index-1],data[index]

# Setup
lat = 19.8957
lon = 75.3203
demo_time = 1585994946.924365
sat_name = "MAROC-TUBSAT"

# Building sat / topos object
bluffton = build_topos(lat, lon)
sat = build_sat(sat_name)

ts = load.timescale().utc(datetime.date.fromtimestamp(demo_time))

print(ts)

difference = sat - bluffton

topocentric = difference.at(ts)

alt, az, distance = topocentric.altaz()

print(alt.degrees, az.degrees, distance.m)