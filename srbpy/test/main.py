from srbpy.alignment import  Align

M1 = Align(path="00-MainLine/M1K-0312")
l = M1.get_ground_elevation(17315)
l2 = M1.get_elevation(17315)
x, y = M1.get_coordinate(17315)


print(l,l2)
# -0.8626576792206331, 0.5057882249337873 1662.41147141861
# -0.862540215993735,  0.505988513499547  1662.4114714186135