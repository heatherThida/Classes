#Thida Aung
# CSCI 169 by Prof Dr. Linnell
#Programming HW 2 due OCT 5


#1
def fun(x,y):
    return (x+y) #end of function
print(fun(1,2))
print(fun("hi", "there"))


#2 
def report(xs):
    num = []
    strr = "" #the whole list of string
    name = "" #ea names so far
    prev = "" 
    for n in xs:
        if type(n) == int: #check to see if number
            num.append(n) #add number in new list
            if strr == "":
                strr = name
            else: 
                strr += ", " + name # formatting , before the next first name
            #resetting the state of prev name to keep track for next name
            prev = ""
            name = ""
        else: #if it's not integer
            if name == "":
                 name = prev #grabbing first name 
            else: #grabbing middle name with space
                name += " " + prev
            prev = n #skip the last name

    average = float(sum(num) / (len(num)))
    return "\"%s, averaged %s. \"" % (strr, average)

print(report([" Jill" ,  "Johnson", 87,  "Billy",  "Ray" ,  "Cyrus" , 78,  "Rita", "Yeats" , 94,  "Bobbie" ,  "Sue" ,  "Palmer" , 72]))


#3
def partition(int_list,p,r):
    pivot = int_list[r]
    while p<r : #true as long as left < right
        while int_list[p] < pivot:
            p +=1 #p++ equivalent
        while int_list[r] > pivot:
            r -=1 #r-- equivalent
        if int_list[p] == int_list[r]: #if both are same value
            p +=1
        elif p<r: #if left<right
            tmp = int_list[p]
            int_list[p] = int_list[r]
            int_list[r] = tmp
    return r 
    
def quicksort(int_list,p,r):
        if p < r:
            j = partition(int_list,p,r)
            quicksort(int_list,p,j-1)
            quicksort(int_list,j+1,r)
            
max_size = 10 #can't really limit size of list in python but if we were to use inside the functionI declare here
int_list = [500, 700, 800, 100, 300, 200, 900, 400, 1000, 600]
print("Input: ", int_list)
quicksort(int_list,0,9)
print("Output: ", int_list)
print(int_list)
