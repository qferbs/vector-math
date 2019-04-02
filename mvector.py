from math import acos, cos, radians, degrees
class Vector:
    def __init__(self, xyz=(0, 0, 0)):
        self.x, self.y, self.z = xyz

    def set_xyz(self, xyz):
        self.x, self.y, self.z = xyz

    def set_by_angle(self, magnitude, alpha=None, beta=None, gamma=None):
        vx, vy, vz = None, None, None
        if(alpha != None):
            vx = magnitude*cos(radians(alpha))
        if(beta != None):
            vy = magnitude*cos(radians(beta))
        if(gamma != None):
            vz = magnitude*cos(radians(gamma))

        if(vx == None):
            vx = (magnitude**2 - vy**2 - vz**2)**0.5
        elif(vy == None):
            vy = (magnitude**2 - vx**2 - vz**2)**0.5
        elif(vz == None):
            vz = (magnitude**2 - vx**2 - vy**2)**0.5
        
        self.x, self.y, self.z = vx, vy, vz

    def xyz(self):
        return (self.x, self.y, self.z)

    def angle(self, angle):
        comp = 0
        if(angle=="alpha"):
            comp = self.x
        elif(angle=="beta"):
            comp = self.y
        elif(angle=="gamma"):
            comp = self.z
        mag = self.magnitude()
        if(mag != 0):
            return degrees(acos(comp/self.magnitude()))
        else:
            return 0
    
    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

def add_vector(v1, *args):
    vx, vy, vz = v1
    for arg in args:
        vx += arg[0]
        vy += arg[1]
        vz += arg[2]
    return (vx, vy, vz)

def scale_vector(v, scalar):
    return (v[0]*scalar, v[1]*scalar, v[2]*scalar)

def dot_product(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

def cross_product(v1, v2):
    vx = v1[1]*v2[2] - v2[1]*v1[2]
    vy = v2[0]*v1[2] - v1[0]*v2[2]
    vz = v1[0]*v2[1] - v2[0]*v1[1]
    return(vx, vy, vz)
