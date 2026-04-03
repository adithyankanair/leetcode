def shuffle_array(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i+n])
    return result

# list comprehension

def shuffle_array(nums, n):
    return [ val for i in range(n) for val in (nums[i], nums[i+n])]