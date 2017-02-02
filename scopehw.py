# Thida Aung
# HW3 for CSCI 169 
# 10/12/16

#spam = "global spam"

def scope_test():
    def do_local():
         spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam1"
        print("After global assignment:", spam)
        
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    """output: test spam because do_local "spam" die once you get out of that scope"""

    do_nonlocal()
    print("After nonlocal assignment:", spam)
    """output: nonlocal spam because nonlocal 
        spam will go find one scope up"""
    do_global()
    print("After global assignment:", spam)
    """output: nonlocal spam" because even it overwrite to "global spam" which we never declared one it dies as it gets out of scope"""

scope_test()
print("In global scope:", spam)

"""output: global spam because there wasn't any "global spam" declared outside of scope_test"""
