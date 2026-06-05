nums =  [3, 1, 4, 2, 3, 5,5]
freq = {}
dup = None
for i in nums:
    if i in freq:
        freq[i] +=1
        
    else:
        freq[i] = 1
print(freq)
for key,value in freq.items():
    if value > 1:
        dup = key
        
print("the  duplicate element is ",dup)
        
        