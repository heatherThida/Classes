def add(ls):
    sum=0
    def inner(x):#helper function
        sum=0
        for y in x:
            sum=sum+y
        nonlocal sum# even though the changes happened before this, they'll be reflected in add's sum
        return sum
    for x in ls:
        #sum=inner(x)+sum
        print(sum)
        inner(x)
        print(sum)
    return sum

print(add([[1,5, 2, 7], [3, 6, 2, 4], [2, 6, 1]]))













##
##def foo(ls):
##    sum=0
##    def inner(x):
##        sum=100
##        for y in x:
##            sum=sum+y
##        def inin():
##            nonlocal sum
##            sum=17
##            print(sum, "inin")
##        print(sum, "inner")
##        inin()
##        print(sum, "inner")
##        nonlocal sum #now the sum in inin and the one in inner are tied to the one in foo - so the one in foo was just changed to 17
##        print(sum, "inner")
##        return sum
##    for x in ls:
##        print(sum, "foo")
##        sum=inner(x)+sum
##        print(sum, "foo")
##    return sum
##
##print(foo([[1,5, 2, 7], [3, 6, 2, 4], [2, 6, 1]]))
##
