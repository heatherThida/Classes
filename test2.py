def partition(int_list,p,r):
    pivot = int_list[r]
    while p<r : #left < right
        while int_list[p] < pivot:
            p +=1
        while int_list[r] > pivot:
            r -=1
        if int_list[p] == int_list[r]:
            p +=1
        elif p<r:
            tmp = int_list[p]
            int_list[p] = int_list[r]
            int_list[r] = tmp
    return r 
    
def quicksort(int_list,p,r):
        if p < r:
            j = partition(int_list,p,r)
            quicksort(int_list,p,j-1)
            quicksort(int_list,j+1,r)
            
size = 10
int_list = [500, 700, 800, 100, 300, 200, 900, 400, 1000, 600]
print("Input: ", int_list)
quicksort(int_list,0,9)
print("Output: ", int_list)
print(int_list)
