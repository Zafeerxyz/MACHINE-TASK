nums = [3, 1, 2, 1, 4, 1, 3,1,3,3]
freq = {}
count = 0
for num in nums:
    if num in freq:
        freq[num] +=1
    else:
        freq[num] = 1
print(freq)    

max_freq = max(freq.values())
for num in nums:
    if freq[num] == max_freq:
        print(num, ":", max_freq)
        break