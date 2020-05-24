# COSMOS 2481 32.8151 -79.963 1586371870.730892
import datetime
import time
from skyfield.api import load, EarthSatellite, Topos
from solve import calc_duty_cycle


def calc_topo(time, difference):
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


def solve_things(satName, lat, lng, start_time):
    ts = load.timescale()
    
    print(satName)

    return_string = ''

    azList, elList, timez = [[] for x in range(3)]
    with open('./Data/active.txt', "r") as f:
        data = f.readlines()
        for i, d in enumerate(data):
            if satName in d:
                tle1 = data[i+1].replace("\n", "").strip()
                tle2 = data[i+2].replace("\n", "").strip()
                break
        else:
            return "No Sat Found"
        satellite = EarthSatellite(tle1, tle2, name=satName)
        station = Topos(latitude_degrees=lat, longitude_degrees=lng)

        difference = satellite - station

        for i in range(720):
            newTime = start_time + float(i)

            timez.append(newTime)

            t = ts.utc(datetime.datetime(*time.gmtime(float(newTime))[:7], tzinfo=datetime.timezone.utc))

            elevation, azimuth = calc_topo(t, difference)

            ds1, ds2 = calc_duty_cycle(azimuth, elevation)
            azList.append(ds1)
            elList.append(ds2)

        for i, e in enumerate(timez):
            return_string = return_string + f'{e}, {azList[i]}, {elList[i]}\n'
        
        

        return return_string

# demovar = """
# Track-a-sat control system
# Latitude: -20.0013
# Longitude: 148.2087
# Satellite: GLOBALSTAR M089
# Start time GMT: 1586944476.246937
# 720 observations, one every 1 second
# Waiting for your solution followed by a blank line...
# """

# print(solve_things("GLOBALSTAR M089", -20.0013, 148.2087, 1586944476.246937))  
                
