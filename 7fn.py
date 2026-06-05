

nw_lst = []
def lst(*nums):
    for i in nums:
        if i>20:
            nw_lst.append(i)
    return nw_lst
            
            
result = lst(3,44,33,22)
print(result)


def lstn(*nums):
    max1 = 0
    for i in nums:
        if i > max1:
            max1 = i
    return max1
        
final = lstn(22,22,3,34,45)
print(final)
