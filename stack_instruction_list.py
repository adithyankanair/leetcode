def buildInstructionList(target, n):
    instruction_list = []
    count = 0
    for i in range(1,n+1):
        instruction_list.append('Push')
        if target[count] == i:
            count +=1
        else:
            instruction_list.append('Pop')
        if count == len(target):
            break
    return instruction_list

print(buildInstructionList([1,3],3))