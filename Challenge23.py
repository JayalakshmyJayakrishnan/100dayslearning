#to print out the frequency of all the unique elements present in a given tuple.

def unique_count(tup):
    ''' 
    input: tup - indicates the tuple
    output: Prints the unique elements and their frequency
    '''
    freq = {}
    
    for i in tup:
        # Convert lists to strings to make them hashable
        if isinstance(i, list):
            i = str(i)
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    
    for key, value in freq.items():
        print(f"{key} : {value}")
