def ex3(a, b, c):
    print(a, b, c)
    return not (a and b) or ((a and c) and not (b or not c))

print(ex3(0,0,0))
print(ex3(0,0,1))
print(ex3(0,1,0)) 
print(ex3(0,1,1)) 
print(ex3(1,0,0)) 
print(ex3(1,0,1)) 
print(ex3(1,1,0)) 
print(ex3(1,1,1)) 