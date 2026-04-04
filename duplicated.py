def findDuplicated(nums):
    n = len(nums)

    total = n*(n+1)//2

    actual_sum = sum(nums)
    unique_sum = sum(set(nums))

    duplicate = actual_sum - unique_sum
    missing = total - unique_sum

    return [duplicate, missing]

print(findDuplicated([1,2,2,4]))


