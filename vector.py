#vector.py
## Vector class 
import math

# Help function 
def GetLength(v1, v2):
    """Assume v1 and v2 are a list of vector [i, j, k].
    Return length between v1 and v2."""
    result = []
    for index in range(len(v1)):
        temp = float(max(v1[index], v2[index]) - min(v1[index], v2[index]))
        result.append(abs(temp))
    # print "Length is " + str(result) 
    return result

def GetDirection(From, To):
    """Assume From and To are a list of vector [i, j].
    Return direction from From to To as a list like as [-1, 1]."""
    result = [] 
    for index in range(len(From)):
        if From[index] == To[index]:
            result.append(0)
        elif From[index] < To[index]:
            result.append(1)
        else:
            result.append(-1)
    # print "Direction is " + str(result) 
    return result

def GetVectorFromTo(p1, p2):
    """Assume p1 and p2 are a list of [x, y].
    Return a Vector object of position from p1 to p2."""
    mag = GetLength(p1, p2)
    unit = GetDirection(p1, p2)
    result = [] 
    for index in range(len(mag)):
        result.append(mag[index] * unit[index])
    # print "GetvectorFromTo result is " + str(result) 
    if len(p1) == 2:
        return Vector(result[0], result[1])
    elif len(p1) == 3:
        return Vector3D(result[0], result[1], result[2])

#3D vector class 
class Vector3D(object):
    """ An object for 3D vector """
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.mag = math.sqrt(self.x**2.0 + self.y**2.0 + self.z**2.0)
        #Get unit vector component 
        self.i = self.x / self.mag
        self.j = self.y / self.mag
        self.k = self.z / self.mag

    def getX(self):
        """ Return x component of vector. """
        return self.x

    def getY(self):
        """ Return x component of vector. """
        return self.y

    def getZ(self):
        """ Return x component of vector. """
        return self.z
    
    def getManitude(self):
        """ Return magnitude of vector. """
        return self.mag 

    def getUnitVector(self):
        """Return unit vector as Vector object. """
        return Vector3D(self.i, self.j, self.k)

    def scaleProduct(self, scale):
        """ Assumes a scale is a float,
        and return scaled vector as vecotr object. """
        scale = float(scale)
        # print "Scale is " + str(scale)
        # print "i j k is " + str(self.i) + ", " + str(self.j) + ", " + str(self.k) 
        mag = self.mag * scale
        x = self.i * mag
        y = self.j * mag
        z = self.k * mag
        return Vector3D(x, y, z)

    def add(self, others):
        """Assumes others is a list of vector object.
        Return vector sum as a Vector object. """
        x = self.getX(); y = self.getY() ; z = self.getZ() 
        for index in range(len(others)):
            x += others[index].getX()
            y += others[index].getY()
            z += others[index].getZ()
        return Vector3D(x, y, z)            
    
    def __str__(self):
        s = '{}i + {}j + {}k, Magnitude : {}'\
            .format(str(self.x), str(self.y), str(self.z), str(self.mag))
        return s 

#2D vector class
class Vector(object):
    """ An object of vector. """
    def __init__(self, x, y):
        """ Assume x and y is coordinate position of x and y. """
        self.x = float(x)
        self.y = float(y)
        self.mag =  math.sqrt(self.x**2.0 + self.y**2.0)
        # math.atan2(j, i) resulted  between -pi and pi
        self.angle =  math.atan2(self.y, self.x)
        #self.i and self.j is a unit vector 
        if self.x != 0.0:
            self.i = math.cos(self.angle)
        else:
            self.i = 0.0 
        if self.y != 0.0:
            self.j = math.sin(self.angle)
        else:
            self.j = 0.0
        
    def getManitude(self):
        """ Return magnitude of vector. """
        return self.mag 

    def getAngle(self):
        """Return angle as Radian from origin. """
        return self.angle        

    def getUnitVector(self):
        """Return unit vector as Vector object. """
        return Vector(self.i, self.j)

    def getPolar(self):
        """ Return polar form as a list [magnitude, angle] . """
        return [self.mag, self.angle]
        
    def scaleProduct(self, scale):
        """ Assumes a scale is a float,
        and return scaled vector as vecotr object. """
        scale = float(scale)
        mag = self.mag * scale
        x = self.i * mag
        y = self.j * mag
        return Vector(x, y)

    def rotateVector(self, theta):
        """ Assumes theta is  float an angle in radian to rotate in counterclockwise.
        Return a vector object rotated. """
        ang = self.angle + theta
        #If component is zero, keep it to zero 
        if self.x != 0.0:
            x = self.mag * math.cos(ang)
        else:
            x = 0.0 
        if self.y != 0.0:
            y = self.mag * math.sin(ang)
        else:
            y = 0.0
        return Vector(x, y)

    def add(self, other):
        """ Assumes other is an object of Vector.
        Return sum of vector as vector object. """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def subteract(self, other):
        """ Assumes other is an object of Vector.
        Return subtraction from self to other vector as vector object. """
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def getMult(self, other):
        """ Assumes other is an object of Vector.
        Return a vector object of multified other. """
        mag = self.mag * other.mag
        ang = self.angle + other.angle
        x = mag * math.cos(ang)
        y = mag * math.sin(ang)
        return Vector(x, y) 

    def getDiv(self, other):
        """ Assumes other is an object of Vector.
        Return a vector object of multified other. """
        mag = self.mag / other.mag
        ang = self.angle -  other.angle
        x = mag * math.cos(ang)
        y = mag * math.sin(ang)
        return Vector(x, y) 
        
    def __str__(self):
        s = '{}i + {}j, Magnitude : {} Angle : {}'\
            .format(str(self.x), str(self.y), str(self.mag), str(math.degrees(self.angle)))
        return s 



###Test code ###
        
# test = Vector(0, 1)
# print test.getUnitVector()
# To = [math.cos(math.pi*(7/4.0)), math.sin(math.pi*(7/4.0))]
# From = []
# for i in range(0, 7):
#     x = math.cos(math.pi*(i/4.0))
#     y = math.sin(math.pi*(i/4.0))
#     From.append([x, y])

# DiffVec = []
# for index in range(len(From)):
#     DiffVec.append(GetVectorFromTwoPoint(From[index], To))
    
# for val in DiffVec:
#     print val 
