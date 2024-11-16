from random import * # usually better just to say import random, 
                     # but with the from * way you don't have to put the 
                     # reference name at the beginning when using the functions as seen below

for i in range(100):
    print(randint(0,100))