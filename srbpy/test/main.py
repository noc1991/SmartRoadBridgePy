from srbpy.alignment import Align

m1k = Align(path="00-MainLine/M1K-0312")
l = m1k.get_ground_elevation(16000)
l2 = m1k.get_elevation(16000)
x, y = m1k.get_coordinate(16000)

print(x, y)
print(l, l2)
pk = m1k.get_station_by_point(x0=472736.5636194062, y0=9854283.750879934)
print(pk)
# -0.8626576792206331, 0.5057882249337873 1662.41147141861
# -0.862540215993735,  0.505988513499547  1662.4114714186135
