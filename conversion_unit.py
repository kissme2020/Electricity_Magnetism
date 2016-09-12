#conversion_unit.py
##Function for converion Physics unit.

import math 

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

def GetDistance(p1, p2):
    """Assume p1 and p2 is a list [x, y]. 
    Return distance between two point. """
    x = max([p1[0], p2[0]]) - min([p1[0], p2[0]])
    y = max([p1[1], p2[1]]) - min([p1[1], p2[1]])
    #print str(x) + " and " + str(y)
    return math.sqrt(x**2.0 + y**2.0)

#Coulomb's constant : Ke, 9e9 N*m^2 / C^2 , 1/(4*pi*epsilon_0)
def GetMagOfCharge(q1, q2):
    """Assume q1 and q2 are a list [charge, x, y]. """
    Ke = 9e9
    #Fe = Ke*(q1*q2/r^2)
    return (Ke*abs(q1[0])*abs(q2[0])) / GetDistance(q1[1:], q2[1:])**2.0 
    
    
#Test code. 
# a =  GetChargeFormMass(70) * 0.01 
# print GetMagOfCharge([a, 0, 0], [-a, 1.5, 0])


flag = True
x = -10.0
q1P = 0.0
q2P = 4.0
deltaX = 0.001
epsilon = 0.01
while flag:
    F1 = 9e9 * (4*2)/ (x - q1P)**2.0
    F2 = 9e9 * (9*2)/ (x - q2P)**2.0
    print "X = " + str(x)
    print max(F1, F2) - min(F1,F2)  
    if abs(max(F1, F2) - min(F1,F2)) <= epsilon:
        print "F1 : " + str(F1) + ", F2 " + str(F2) 
        flag = False
    if x >=  10.0 :
        print "X is out of limit. "
        flag = False
    x += deltaX
          
        
    
    
    
    
    
    