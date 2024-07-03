import random

_#Define the set of characters to choose from for the password_
x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?><:{}[]\\|+_=-.,;~`'"

_#Specify the desired length of the password_

passlen = 14

_# random.sample() creates a list of 'passlen' unique characters from 's_

p = "".join(random.sample(x, passlen))

print(p)
