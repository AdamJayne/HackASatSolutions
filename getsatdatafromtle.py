import datetime

from orbit_predictor.sources import get_predictor_from_tle_lines

TLE_LINES = (
    "1 13337U 98067A   20087.38052801 -.00000452  00000-0  00000+0 0  9995",
    "2 13337  51.6460  33.2488 0005270  61.9928  83.3154 15.48919755219337")

predictor = get_predictor_from_tle_lines(TLE_LINES)

result = predictor.get_position(datetime.datetime(2020, 3, 26, 21, 52))

print(result)
