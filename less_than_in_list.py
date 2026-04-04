def countLessInList(nums):
    new = []
    for i in nums:
        count = 0
        for j in nums:
            if i != j and j<i:
                count+=1
        new.append(count)
    return new

print(countLessInList([8,1,2,2,3]))
# 2 loops not optimal

def optimalCLIL(nums):
    sorted_nums = sorted(nums)
    rank = {}
    for i, num in enumerate(sorted_nums):
        if num not in rank:
            rank[num] = i
    return [rank[num] for num in nums]

print(optimalCLIL([4,1,2,2,3]))