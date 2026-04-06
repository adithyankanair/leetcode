def finalPrices(prices):
    n = len(prices)
    result = [0]*n
    for i in range(n):
        result[i] = prices[i]
        for j in range(i+1,n):
            if prices[i] > prices[j]:
                result[i] = prices[i] - prices[j]
                break
    return result
print(finalPrices([8,4,6,2,3]))

# 2 loops o(n)^2
def finalPricesStacK(prices):
    stack  = []
    for i in range(len(prices)):
        while stack and prices[stack[-1]] >= prices[i]:
            index = stack.pop()
            prices[index] -= prices[i]
        stack.append(i)
    return prices

print(finalPricesStacK([8,4,6,2,3]))