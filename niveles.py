from random import *


"""
A B C
 D E
F G H
 I J
K L M
"""

B1=["B","C","G","H"]
B2=["B","D","E","G","I","J"]
B3=["D","E","F","G","H","I","J"]
B4=["B","C","G","H","L"]
B5=["B","E","F","H","I","K","L"]
B6=["C","D","E","H","I"]
B7=["B","D","E","G","H","K"]
B8=["B","D","E","F","H","I","J","K","L"]
B9=["B","C","D","E","G","H","I","J"]
I1=["B","D","E","F","H","K","L","M"]
I2=["B","D","E","F","H","I","J","K","M"]
I3=["A","B","D","G","I","L"]
I4=["A","B","C","D","E","G"]
I5=["D","E","F","H","I","J","K","M"]
I6=["B","F","G","H","I","J","K","L","M"]
I7=["B","C","E","F","H","I","K","L"]
I8=["B","C","E","F","G","H","I","K","L"]
I9=["A","B","D","F","G","I","K","L"]
I10=["B","D","E","F","G","H","I","J","L"]
A1=["B","D","E","F","H","I","J","K","L","M"]
A2=["B","D","E","G","I","J","K","L","M"]
A3=["B","D","F","G","H","I","J","K","L"]
A4=["C","D","E","F","G","I","J","K","L"]
A5=["B","C","D","E","F","G","H","I","J","K","L"]
A6=["B","C","D","E","F","H","I","J","K","L","M"]
A7=["C","E","G","H","I","J","K","L","M"]
E1=["B","C","D","E","F","G","H","J","K","L"]
E2=["D","E","F","G","H","I","J","K","L","M"]
E3=["B","D","E","F","G","H","I","J","K","L","M"]
E4=["A","C","D","E","G","H","I","J","K","L","M"]
E5=["A","C","D","E","F","G","H","I","J","K","M"]
E6=["B","C","D","E","F","G","H","I","J","K","M"]
E7=["A","C","D","E","F","G","H","I","J","K","M"]
E8=["B","C","D","E","F","G","I","J","K","M"]
E9=["A","B","D","E","G","H","I","J","K","L","M"]
E10=["A","B","C","D","E","F","H","I","J","K","L","M"]

basico=[B1,B2,B3,B4,B5,B6,B7,B8,B9]
intermedio=[I1,I2,I3,I4,I5,I6,I7,I8,I9,I10]
avanzado=[A1,A2,A3,A4,A5,A6,A7]
experto=[E1,E2,E3,E4,E5,E6,E7,E8,E9,E10]

def niveles(x):
    if x=="basico":
        return basico[int(9*random())]
    elif x=="intermedio":
        return intermedio[int(10*random())]
    elif x=="avanzado":
        return avanzado[int(6*random())]
    elif x=="experto":
        return experto[int(10*random())]
    
    
