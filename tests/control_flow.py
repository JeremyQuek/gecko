import random

x = 0                       # x: int

if random.randint(0, 2) == 0:
    x = "hi"                # branch A -> x: str
    if True:
        g = False
        if not False:
            h = "st"
            g = float('inf')
elif random.randint(0, 2) == 1:
    x = 3.5                 # branch B -> x: float
else: 
    x = None
y = x                       # merge point -> x: str | float, so y: str | float
