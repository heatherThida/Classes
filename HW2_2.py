#Thida Aung
# CSCI 169 by Prof Dr. Linnell
#Programming HW 2 due OCT 5

#2 
def report(xs):
    num = []
    strr = "" 
    name = "" 
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

