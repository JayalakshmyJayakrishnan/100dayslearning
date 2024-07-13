import sys
Tuple1 = ("J" ,10,  "A", 19, "Z" , 11)
Tuple2 = (1, 2 ,3 ,4)
Tuple3 = ((1,"Clutch") , (2,"Brake"), (3,"Accelerator"))

print("Size of Tuple1: " + str(sys.getsizeof(Tuple1)) + "bytes")
print("Size of Tuple2: " + str(sys.getsizeof(Tuple2)) + "bytes")
print("Size of Tuple3: " + str(sys.getsizeof(Tuple3)) + "bytes")




# OUTPUT:  Size of Tuple1: 88bytes
           Size of Tuple2: 72bytes
           Size of Tuple3: 64bytes
