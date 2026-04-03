def maxStreak(nums):
    count = max_streak = 0
    for num in nums:
        if num == 1:
            count+=1
            max_streak=  max(count, max_streak)
        else:
            count = 0
    return max_streak