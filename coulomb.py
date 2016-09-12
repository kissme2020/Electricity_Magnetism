#coulomb.py
## calculate Coulomb's law between charges
import sys
import math
from vector import *
#For 3D plot
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


#help function
def GetChargeFormMass(mass):
    """Assume mass is the mass of an object as a float. """
    P_charge = 1.6e-19
    E_charg = -1.6e-19
    P_mass = 1.67e-27
    E_mass = 0.0009e-27

    # Charge per mass : Kg / (Kg/uncleon)
    uncleons = mass / P_mass
    # Protons / (C / Proton) 
    result = (uncleons / 2) * P_charge  # Mass of proton and neutron is same .

    return result #Return value's unit is Coulomb

def GetMagenitude(q1, q2, d):
    """Assume q1 and q1 are charged on a particle in coulomb. 
    d is the magnitude of displacement between q1 and q2. 
    Return magnitude of Force in N."""
    Ke = 9.0e9 #constant of coulomb
    return Ke * ((q1*q2)/ d**2.0)

def IsRepel(x1, x2):
    """Assume x1 and x2 is a numbers.
    Return True if x1 and x2 is same sign otherwise False."""
    if (x1 * x2) < 0:
        return False
    else:
        return True

class Particle(object):
    """An object of electrical charge."""
    def __init__(self, charge, p):
        """Assumes charge is electrical charge on particle,
        and position is a list [x, y]."""
        self.charge = float(charge)
        self.position = p

    def getChagre(self):
        """ Return chage. """
        return self.charge

    def getPosistion(self):
        """ Return position as a list [x, y]."""
        return self.position
        
    def getForceTo(self, other):
        """Assume other is an object of Particle as a list.
        Return Force vector exerts to others."""
        #Calculate position vector from self to other
        posVec = GetVectorFromTo(self.position, other.position)
        # print "Position vector is ",
        # print posVec
        # print "position vector magnitude is " + str(posVec.getManitude())
        #Get magnitude
        mag = GetMagenitude(self.charge, other.charge, posVec.getManitude())
        # print "Coulomb's law magnitude is " + str(mag) 
        return posVec.getUnitVector().scaleProduct(mag)
        
    def __str__(self):
        s = '{} C, angle {}'.format(str(self.chagre), str(math.degrees(self.position.angle)))    
        return s


#Test code
print ""
Q1 = Particle(50e-6, [0, 0, 0])
Q2 = Particle(50e-6, [0, 0, 0.01])
Q3 = Particle(50e-6, [0, 0.01, 0])
Q4 = Particle(50e-6, [0, 0.01, 0.01])
Q5 = Particle(50e-6, [0.01, 0, 0])
Q6 = Particle(50e-6, [0.01, 0, 0.01])
Q7 = Particle(50e-6, [0.01, 0.01, 0])
Q8 = Particle(50e-6, [0.01, 0.01, 0.01])

On = Q1
From = [Q2, Q3, Q4, Q5, Q6, Q7, Q8]
Force = [] 
for val in From:
    Force.append(val.getForceTo(On))

print "Force is " 
for val in Force:
    print val
    
result = Force[0].add(Force[1:])
print "**** Result is *****"     
print result

