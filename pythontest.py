"""def scope_test():
    x = 5

    def new_scope():
        print(x)
        # error if we do x= 5 here

    new_scope()
scope_test()"""

spam= "test spam"

def scope_test():
    spam = "scope test's spam"
    x = 2
    def do_local():
        spam = "local spam"

        def do_nonlocal():
            x=1
            nonlocal x

        def do_global():
            nonlocal spam
            spam = "global spam"
        do_global()
        print(spam)
    do_local()

scope_test()
print(spam)
print(x)
    
