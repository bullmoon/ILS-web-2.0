# Copper bars calculation 
# for ABB 1.2 without current transfers

# Variables
t = None           # Thickness of copper (mm). Must be 10 or 12 mm.
amperage = None    # Amperage of Circuit Breaker (A)
h = None           # Size from Circuit Breaker to Busbar (mm)
bb = None          # Distance from Circuit Breaker to board back (mm)
corr = None        # Correction parameter of binding on the machine
delta = None       # Correction parameter for binding depends of thickness
l1s1 = None        # Lenght of stripe L1s1
l1s2 = None        # Lenght of stripe L1s2
l2s1 = None        # Lenght of stripe L2s1
l2s2 = None        # Lenght of stripe L2s2
l3s1 = None        # Lenght of stripe L3s1
l3s2 = None        # Lenght of stripe L3s2
ns1 = None         # Lenght of stripe Ns1
ns2 = None         # Lenght of stripe Ns2

# Constants
spacer = 28 # High of spacer (mm)
shs = 61    # Lenght of short shelf (mm)
shb = 71    # Lenght of long shelf (mm)
bs1 = 199   # Distance from board back to stripe S1
corr10 = 8.5    # Binding correction for copper thinkness 10 mm
corr12 = 9.0    # Binding correction for copper thinkness 12 mm

def set_correction():
    if t == 10:
        corr = corr10
    elif t == 12:
        corr = corr12
    else:
        return "Incorrect thinkness"
    return corr

def calc_stripe_lenght():
    #l3s1 = S1L + S1H1 + shs - (2 * 17) + 1
    pass
    #return 200