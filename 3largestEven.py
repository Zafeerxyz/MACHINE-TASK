nums =  [5, 3, 7,4,6]
largest_even = 0
for num in nums:
    if num % 2 ==0 and num > largest_even:
        largest_even = num
        
if largest_even == 0:
    print("No even")
else:
    print("Largest even",largest_even)