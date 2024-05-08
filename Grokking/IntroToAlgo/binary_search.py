def binary_search(list, item):
    #Low and High are used as trackers
    low= 0 #low is an index
    high= len(list)-1 #high is an index
    
    #While I haven't narrowed it down to one element
    while low<=high:
        #Check the middle element
        mid= (low+high)//2 #mid is an index
        guess=list[mid] #this is the only number
    
    #These are all the checks to see if you got guess right
    #For conceptual thinking, reflect on the book's example of 
    #guessing a number between 1 to 99    
        if guess==item:
            return mid
        
        if guess > item:
            #all the numbers after current high becomes irrelevant
            #confusion spot: your mid is actually your 'guess index'
            high= mid-1 
        else:
            low= mid+1
    return None
    
my_list=[1,3,5,6,7,8,10]
print(binary_search(my_list, 8)) #will return the position where your the correct guess exists
print(binary_search(my_list, -1))
