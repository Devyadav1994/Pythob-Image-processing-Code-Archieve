# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 00:13:15 2018

@author: Fakrul-IslamTUSHAR
"""

import numpy as np

primes=[2,3,5,7]
for prime in primes:
    print(prime)


#print  0,1,2,3,4,5
for x in range(6):
    print(x)

#Print a 3,5,7
for i in range(3,8,2):
    print(i)
    

print("While Loop")

count=1
while count<6:
    print(count)
    count +=1

# =============================================================================
# use of break
# =============================================================================

mark=1
while True:
    print(mark)
    mark +=1
    if mark>11:
        break
    

for ix in range(10):
    if ix%2==0:
        continue
    print(ix)



# =============================================================================
# for loop
# =============================================================================
print(".................Babu.................")
for babu in range(1,100):
    if babu==30:
        break
    if babu%2==1:
        continue    
    print(babu)


# =============================================================================
# Boro Babu
# =============================================================================

print(".........Boro Babu........")

for borobabu in range(1,50):
    if borobabu%2==1:
        continue
    if borobabu>29:
        break
    print(borobabu)



