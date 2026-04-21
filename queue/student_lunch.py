def studentLunch(students, sandwiches):
    count = [0,0]

    for s in students:
        count[s] +=1

    for s in sandwiches:
        if count[s]== 0:
            return count[1-s]
        count[s] -= 1
    
    return 0

print(studentLunch([1,1,0,0],[0,1,0,1]))