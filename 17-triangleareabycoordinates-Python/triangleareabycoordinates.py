# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.

import math
from math import sqrt
def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
    l1 = math.sqrt((x1 - x2)*2 + (y1 - y2)*2)
    l2 = math.sqrt((x2 - x3)*2 + (y2 - y3)*2)
    l3 = math.sqrt((x3 - x1)*2 + (y3 - y1)*2)
    p = (l1 + l2 + l3)/2
    area = sqrt(p * (p - l1) * (p - l2) * (p - l3))
    return area
    
	