def report(xs):
    sum = 0 #to get total for average
    count = 0 #to get number of scores for average
    names_array = [] #initializing to insert first names and middle names into names_array array
    string_per_person = 0 #used to separate names for each score
    for element in xs:
         
        if(type(element)) == (type(1)):
            sum += element
            if (string_per_person == 2):
            	#Add only first name
            	num = xs.index(element) - 2 #getting position to get first name only
            	names_array.append(xs[num]) #adding to array
            elif (string_per_person == 3):
            	#Add first and middle name
            	num = xs.index(element) - 3 #getting position to get first name 
            	num1 = xs.index(element) - 2 #getting position to get middle name 
            	names = xs[num] + " " + xs[num1]
            	names_array.append(names) #adding to array

            count += 1
            string_per_person = 0 #reset number of names for each person

        if(type(element)) == (type("s")):
        	string_per_person += 1 # counting number of names for each person


    for name1 in names_array:
    	print(name1, end=", ")

    print ("averaged", sum/count, ".") #getting average
    
report(["Jill", "Johnson", 87, "Billy", "Ray", "Cyrus", 78, "Rita", "Yeats", 94, "Bobbie", "Sue", "Palmer", 72])
   
        
        


    
