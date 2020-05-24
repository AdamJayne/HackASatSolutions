import datetime
import time
from skyfield.api import load, EarthSatellite, Topos

"""
Latitude: 19.8957
Longitude: 75.3203
Satellite: MAROC-TUBSATmt
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

ts = load.timescale()

def build_ts(time_num):
    return load.timescale()

def build_sat(sat_name):
    tle1, tle2 = sat_dict[sat_name]
    return EarthSatellite(tle1, tle2, sat_name)
http://www.math.com/school/subject1/lessons/S1U2L1DP.htmltude_degrees=lon)

def calc_duty_cycle(degrees):
    return (degrees * (4915/180)) + 2457

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

t = ts.utc(datetime.datetime(*time.gmtime(demo_time)[:7], tzinfo=datetime.timezone.utc))

print(t)

difference = sat - bluffton

topocentric = difference.at(t)

alt, az, distance = topocentric.altaz()

elevation = alt.degrees
azimuth = az.degrees

print(azimuth, elevation)

# elevation = 180.0
# azimuth = 90.0


if azimuth > 180.0:
    azimuth -= 180.0
    elevation = 180.0 - elevation

ds1 = calc_duty_cycle(azimuth)
ds2 = calc_duty_cycle(elevation)

print(demo_time, ds1, ds2)
# test azimuth: >270
# test elevation: < 150
# 1585994946.924365, 7265, 7148