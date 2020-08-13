from skyfield.api import load, EarthSatellite

# Time when spotted (2020, 3, 18, 4, 13, 54.0)
# Sat coords ? [-6219.329207248555, -2170.734173251079, 1330.291494856528]
# Time next view (2020, 3, 18, 18, 51, 28.0)


ts = load.timescale()

sat_dict = {}

startTime = ts.utc(2020, 3, 18, 4, 13, 54.0)

with open('stations.txt','r') as f:
    data = f.readlines()
    data = [l.replace('\n', "").rstrip() for l in data]

for index, line in enumerate(data[::3]):
  # print(index, line)
  sat_dict[line] = data[index*3+1],data[index*3+2]

for k, v in sat_dict.items():
  # print(k, v)
  sat = EarthSatellite(*v, name=k)
  x, y, z = sat.at(startTime).position.km
  tocheck =  [-6219, -2170, 1330]
  if int(x) == tocheck[0] and int(y) == tocheck[1] and int(z) == tocheck[2]:
    print("found", k)
    again = sat.at(ts.utc(2020, 3, 18, 23, 9, 51.0))
    print(again.position.km)
  
