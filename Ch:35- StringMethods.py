#1. capitalize 
text: str = 'python'
print(text.capitalize()) #OUTPUT: Python 

#2. casefold
text: str = "PyThON"
text2: str = "PyTHON"
print(text.casefold()) #OUTPUT: python 
print(text2.casefold())  #OUTPUT: python

#3. center
text: str = 'LOUIS'
print(text.center(20, '.')) #OUTPUT: .......LOUIS......

#4. count
text: str = "jjabcjjabcjjxyz"
print(text.count('jj')) #OUTPUT:3

#5. encode
text: str = 'TIM BERNERS-LEE'
print(text.encode(encoding='UTF-8', errors='strict')) #OUTPUT: b'TIM BERNERS-LEE'
