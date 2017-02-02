a, b, x= (1, 2, 9)

print(a, b)

def test():
    a=5#creates new local a
    global b# if you want to modify global b you have to do this
    b=b+1
    c=10#local to test
    while c==10:
        d=15#local to test
        c=c+1
    print(a)
    print(b)
    print(c)
    print(d)
    print(x)
test()
print(a, b)# can't print c or d here


