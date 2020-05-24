import datetime
import time
from skyfield.api import load, EarthSatellite, Topos
import matplotlib.pyplot as plt
from solve import calc_duty_cycle

# name = "MAROC-TUBSAT"            
# line1  = "1 27004U 01056D   20101.12713578 -.00000040  00000-0  47473-5 0  9998"
# line2 = "2 27004  99.5043 235.4641 0019726 190.1813 347.4559 13.70139743916818"

latitude = 51.43
longitude = 5.5
# Satellite: GLOBALSTAR M094
# Start time GMT: 1586418067.298839

# latitude = 19.8957
# longitude = 75.3203

name = "GLOBALSTAR M094"
line1 = "1 39074U 13005C   20101.25324282 -.00000078  00000-0  14274-3 0  9991"
line2 = "2 39074  51.9950 188.5999 0000549  95.3724 264.7205 12.62264397333198"

ts = load.timescale()

maroc = EarthSatellite(line1, line2, name=name)
station = Topos(latitude_degrees=latitude, longitude_degrees=longitude)

difference = maroc - station

entries = list(map(lambda x: x.replace(",", "").split(" "), open('./examples/solution2.txt').read().split("\n")))

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

result = list(map(lambda abc: calc_duty_cycle(*abc), zip(azList, elList)))

expected = [(int(serv1), int(serv2)) for serv1, serv2 in zip(serv1List, serv2List)]

# statusList = []

# for indx, val in enumerate(result):
#     if val == expected[indx]:
#         statusList.append("matched")
#     else:
#         statusList.append("failed")

# time az ele

with open('result.txt', 'w+') as f:
    for i, val in enumerate(timez):
        toWrite = f'{val}, {serv1List[i]}, {serv2List[i]}\n'
        f.write(toWrite)
    f.write("\n")


