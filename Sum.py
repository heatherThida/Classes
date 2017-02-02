import math

def fun (ls):
    sum = 0
    def iter(ls2):
        sum = 0
        for x in ls2:
            sum = sum+x
            print("x: " , x, " sum: " , sum)
        print("iter's sum " , sum)
        return sum  
    
    
    for x in ls:
        sum = sum + iter(x)
        print("2nd loop x: " , x)
        print("2nd sum: ",  sum)

    return sum
print("\n", fun([[1, 2, 3], [2, 3, 4], [1, 2, 3]]))
