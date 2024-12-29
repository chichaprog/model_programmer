from math import tan, pi,sin,cos,atan2,sqrt

from math import sin, cos

print(tan(pi/4))


#sin and cos.
def length(v):
    return sqrt(v[0]**2 + v[1]**2)

def to_polar(vector):
    x,y = vector[0], vector[1]
    angle = atan2(y,x)

    return (length(vector), angle)


def deg_to_rad(x):
    return x / 180 * pi

atan2(3,-2)
#2.158798930342464

print(atan2(3,-2))
print(to_polar((1,0)))
to_polar((1,0))
print(to_polar((-2,3)))


length((-1.34,2.68))
print(length((-1.34,2.68)))
a = (sin(180 / 180 * pi))
b = (cos(90 / 180 * pi))
r = 8.5

print(r * a)
print(r * b)
print(deg_to_rad(180))



#deg to rad.

#def deg_to_rad(x):
    #return x / 180 * pi
