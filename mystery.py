import math

def fun(a, first, last, key):
    if first > last:
        return -1
    else:
        mid = math.floor((first+last)/2)  
        if key == a[mid]:
            return mid
        elif key < a[mid]:
            return fun(a, first, mid-1, key)
        else:
            return fun(a, mid+1, last, key)
    

ls = [2, 5, 7, 10, 12, "apple"] 


size = 6
print(fun(ls, 0, size-1, 10))
# can't do this kind of type
#print("apple"< 7)
# can't do this kind of type either
#size = "Hello!"
print(size)

print("Python doesn't need any type infront of parameters of the functions")
print("\nso cool") 
