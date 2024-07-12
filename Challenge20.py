import sys
Tuple1 = ("J" ,10,  "A", 19, "Z" , 11)
Tuple2 = (1, 2 ,3 ,4)
Tuple3 = ((1,"Clutch") , (2,"Brake"), (3,"Accelerator"))

print("Size of Tuple1: " + str(Tuple1.__sizeof__()) + "bytes")
print("Size of Tuple2: " + str(Tuple2.__sizeof__()) + "bytes")
print("Size of Tuple3: " + str(Tuple3.__sizeof__()) + "bytes")




#Output: Size of Tuple1: 72bytes
         Size of Tuple2: 56bytes
         Size of Tuple3: 48bytes
