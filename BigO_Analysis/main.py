import random
import time

def randomNumbers(n):
   result = [] #make an empty list to hold random numbers
   
   while len(result) < n: # this loop will run until the length of the empty list is equal to the number that is passed
      num = random.randint(0,n-1) #generates a random number 
      
      found = False #sets found to False
      
      for x in range(len(result)): #looks for a number in the result empty list
         if result[x] == num: #if the random number was found in the result empty list then sets found to True
            found = True
            break
      
      if not found:
         result.append(num) #if the random number was found in the result empty list then keeps addding numbers to the result
   
   return result

def randomIndexes(n):
   result = [-1 for x in range(n)]
   
   for num in range(n):
      index = random.randint(0,n-1)
      
      while result[index] != -1:
         index = random.randint(0,n-1)
      
      result[index] = num
   
   return result

def swap(arr, i, j):
   arr[i], arr[j] = arr[j], arr[i]
   
def randomShuffle(n):
   list= [i for i in range(n)]
   
   for i in range(n-1, 0,-1):
      j=random.randint(0,i)
      swap(list,i,j)
   
   return list
   


# Displays a comparison in RUNTIME between two functions used to create
#  a random list. Tests sizes 10, 100, 1000, and 10000. May take a long
#  time to finish.
def main():
   
   print()
   
   # Print the header for the table of runtimes
   print("{:>25s}{:>12s}{:>12s}\n".format("Numbers", "Indexes", "Shuffle"))
   
   # Testing set
   for size in [10,100,1000,10000]:
      
      # Print the lefthand label of the table
      print(" Size: {:>5d} ".format(size), end="", flush=True)
      
      
      # Test each function
      for function in [randomNumbers, randomIndexes, randomShuffle]:
            
         # When did we start the test      
         startTime = time.time()
         
         function(size)
         
         # When did we end the test
         endTime = time.time()
         
         # Display in nice formatting the difference in seconds between starting
         #  and ending the test.
         print("{:>12.4f}".format(endTime - startTime), end="", flush=True)
         
      
      print()
   
   print()
      

# Use this function instead of main() to see the list created by your function.
#  Change the line at the bottom of this file to use showList instead of main() to
#  use.
#  Example use: showList(10, randomShuffle)
def showList(n, function):
   
   print()
   
   print(function(n))
      
   print()
   

if __name__ == "__main__":
   main()
   showList(10,randomShuffle)

