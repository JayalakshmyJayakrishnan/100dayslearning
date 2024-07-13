if __name__ == '__main__':
  #Reads the input
    n = int(input("Enter the number of elements:"))                                         #Read the number of elements
    t = tuple(map(int, input("Enter the elements separated by space:").split()))            #Read the elements and convert them into a tuple of integers
    hash_value = hash(t)                                                                    #Calculate and print the hash value of the tuple
    print(f"Hash value of the tuple {t}: {hash_value}")
  
                                                                                  
  

  


   
