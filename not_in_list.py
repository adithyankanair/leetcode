def NotInList(nums):
    set_list = set(nums)
    not_in_list = []
    for i in range(1,len(nums)+1):
        if i not in nums:
            not_in_list.append(i)
    return not_in_list

print(NotInList([1,1]))

# optimal - inplace marking
def optimalNIL(nums):
    for num in nums:
        index = abs(num)-1
        nums[index] =  -abs(nums[index])
    result = []
    for i in range(len(nums)):
        if nums[i] >0:
            result.append(i+1)
    return result
print(optimalNIL([4,3,2,7,8,2,3,1]))
    