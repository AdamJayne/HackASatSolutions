from skyfield.api import EarthSatellite, load, Topos

ts = load.timescale()
planets = load('de421.bsp')
earth = planets['earth']

monument = Topos("38.889484 N", "77.035278 W")

line1 = '1 13337U 98067A   20087.38052801 -.00000452  00000-0  00000+0 0  9995'
line2 = '2 13337  51.6460  33.2488 0005270  61.9928  83.3154 15.48919755219337'

satellite = EarthSatellite(line1, line2, name="Redacted")
t = ts.utc(2020, 3, 26, 21, 52)

difference = satellite - monument

print(difference)

topocentric = difference.at(t)

print(topocentric.altaz())

alt, az, distance = topocentric.altaz()

print(90.0 - alt.degrees)
print(az.degrees - 180.0)
print(distance.m)