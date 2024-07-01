def volume_sphere(r):
    '''input: r = radius of the sphere
       output: prints volume of the sphere'''
#Use pi as 22/7

#Calculates the volume
volume = ((4/3) * (22/7) * (r ** 3))

#Prints the result
print('The volume of the sphere with radius', r, 'is:', volume)

#Sample input value

r1 = 1
r2 = 8


# Calculate and print the volume for both radii
volume_sphere(r1)
volume_sphere(r2)

#Output obtained :The volume of the sphere with radius 1 is: 4.19047619047619
                  The volume of the sphere with radius 8 is: 2145.523809523809
