def swap_case(s):
    x = ""
    for i in s:
        if i.isupper() == True:
            x += (i.lower())
            
        else:
            x += (i.upper())
        
    return x
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
