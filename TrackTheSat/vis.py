import datetime
import time
from skyfield.api import load, EarthSatellite, Topos
import matplotlib.pyplot as plt

name = "MAROC-TUBSAT"            
line1  = "1 27004U 01056D   20101.12713578 -.00000040  00000-0  47473-5 0  9998"
line2 = "2 27004  99.5043 235.4641 0019726 190.1813 347.4559 13.70139743916818"

latitude = 19.8957
longitude = 75.3203


ts = load.timescale()

maroc = EarthSatellite(line1, line2, name=name)
station = Topos(latitude_degrees=latitude, longitude_degrees=longitude)

difference = maroc - station

entries = list(map(lambda x: x.replace(",", "").split(" "), open('./examples/solution1.txt').read().split("\n")))

# read the solution, remember to kill the commas
# loop over each solution and create a viz obj
# vis: time, ds(arm1, ar2), topo(azimuth, elevation)

def calc_topo(time):
    alt, az, dist = difference.at(time).altaz()
    return alt.degrees, az.degrees
    

def create_vis(entry):
    if len(entry) < 3: return None
    timestamp, serv1, serv2 = entry

    t = ts.utc(datetime.datetime(*time.gmtime(float(timestamp))[:7], tzinfo=datetime.timezone.utc))

    elevation, azimuth = calc_topo(t)

    vis = {
        "time": timestamp,
        "serv1": serv1,
        "serv2": serv2,
        "azimuth": azimuth,
        "elevation": elevation
    }
    # return the vis dict

    # print(vis)
    return vis

# x axis time
#  y = value
# 4 pieces = indiv colors

azList, elList, serv1List, serv2List, timez = [[] for x in range(5)]

for e in list(map(create_vis, entries)):
    if e == None:
        continue
    else:
        timez.append(e["time"])
        azList.append(e["azimuth"])
        elList.append(e["elevation"])
        serv1List.append(e["serv1"])
        serv2List.append(e["serv2"])


