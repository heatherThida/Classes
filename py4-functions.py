def spam(eggs):
    if eggs == "hello":
        return 10
    elif eggs == 10:
        return "hello"
    else:
        return "spam"
print(spam(10))
print(spam("hello"))

#can't print here
#print(z)

z="hello"
z=142 # if I declare this ahead of "hello" it would show z as "hello" not "142"
def spam(eggs):
    if type(eggs) == type("hello"):
        return 10
    elif type(eggs) == type(10):
        return "hello"
    else:
        return "spam"
print(spam(8))
print(spam("hi"))
#can print here
print(z)














x = 10
c=10
def spam ():
    c=14
    bbeans = 15
    def eggs ():
        c="funtimes!  go to the barbecue this afternoon"
        print(c)
        return bbeans
    print(x)
    print(c)
    return eggs()

print(spam())
print(c)
