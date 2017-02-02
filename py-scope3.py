"""
def add(ls):
    sum=0
    def inner(x):#helper function
        sum=0
        for y in x:
            sum=sum+y
        return sum
    for x in ls:
        sum=sum+inner(x)
    return sum

print(add([[1,5, 2, 7], [3, 6, 2, 4], [2, 6, 1]]))










def add(ls):
    sum=0
    def inner(x):#helper function
        nonlocal sum #what chaos will this cause??
        sum=0
        for y in x:
            sum=sum+y
        return sum
    for x in ls:
        sum= inner(x)+ sum  # what happens if we switch the order back to the original?  Why?
    return sum

print(add([[1,5, 2, 7], [3, 6, 2, 4], [2, 6, 1]]))

"""



def add(ls):
    sum=0
    def inner(x):#helper function
        
        sum=0
        for y in x:
            sum=sum+y
        nonlocal sum #moving local lower changes? No, it still apply to outer variable above sum=0 changed to sum= 15
        return sum
    for x in ls:
        #sum= inner(x)+ sum  # what happens if we switch the order back to the original?  Why?
        print(sum)
        inner(x)
        print(sum)
    return sum

print(add([[1,5, 2, 7], [3, 6, 2, 4], [2, 6, 1]]))
"""
output :
0
15
15
15
15
9
9
"""












