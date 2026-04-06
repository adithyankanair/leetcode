def calculateFunctionTime(n,logs):
    result = [0]*n
    stack = []
    prev_time = 0
    for log in logs:
        fn, typ, time = log.split(':')
        fn, time = int(fn), int(time)
        if typ == 'start':
            if stack:
                result[stack[-1]] += time - prev_time
            stack.append(fn)
            prev_time = time
        else:
            result[stack.pop()] += time - prev_time +1
            prev_time = time+1
    return result

print(calculateFunctionTime(2,["0:start:0","1:start:2","1:end:5","0:end:6"]))
