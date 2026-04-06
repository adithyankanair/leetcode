def betterTemperature(temperatures):
    n = len(temperatures)
    result = [0]*n
    for i in range(n):
        for j in range(i+1,n):
            if temperatures[j] > temperatures[i]:
                result[i] = j-i
                break
    return result

print(betterTemperature([73,74,75,71,69,72,76,73]))

# monotonic stack
def betterTemperatureStack(temperatures):
    stack = []
    result = [0]*len(temperatures)
    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            index = stack.pop()
            result[index] = i - index
        stack.append(i)
    return result

print(betterTemperatureStack([73,74,75,71,69,72,76,73]))