name="this is vikash gajraj yadav.they are very lazy boy"
frequency={}
for char in name:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1
print(frequency)        
           