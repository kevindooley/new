from random import randint
import math
import time
import numpy as np

#define function called counting_Sort. Takes 2 arguments - array to be sorted (array 1)and max value in array (100)
#create counting array 
#goes through array 1 and counts the number of instances of each element
def counting_sort(array1, max_val):
    m = max_val + 1
    count = [0] * m                
    
    for a in array1:
        count[a] += 1  # count occurences of each element in array 1         
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            array1[i] = a
            i += 1
    return array1

# creating a random array, function takes in n numbers
def random_array(n):
    # create an array variable
    array = []
    # if n = 10, 0,1,2,3,4,,,9
    for i in range(0, n, 1):
        # add to the array random integers between 0 and 100
        array.append(randint(0,100))
    return array


global quick_avg
quick_avg = []
runs= 10 # 10 iterations at each input n
results = [] 


#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(100) # input n
    max_val = max(alist)
    counting_sort(alist, max_val) # call quick sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average of all 10 runs(using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
quick_avg.append(avg_runtime)


#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(1000) # input n
    max_val = max(alist)
    counting_sort(alist, max_val) # call quick sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average of all 10 runs(using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
quick_avg.append(avg_runtime)

print("Quick", quick_avg)

print("Quick", quick_avg)