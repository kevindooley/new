import time
import numpy as np
from random import randint
import pandas as pd
import seaborn as sns


# Demonstration bubble sort
# Adapted from source https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheBubbleSort.html
# Supportive source https://www.youtube.com/watch?v=Vca808JTbI8

def bubble_sort(alist): #define function called bubbleSort
    for passnum in range(len(alist)-1,0,-1): # create outer for loop starting from second last index of alist to index 0
        for i in range(passnum): # inner loop now has a new range and goes until passnum. Largest number at the end
            if alist[i]>alist[i+1]: # if first value is greater than the value beside it, swap them
                temp = alist[i] # create temp variable
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

# Demonstration Selection Sort
# Adapted from https://www.pythoncentral.io/selection-sort-implementation-guide/
# Adapted from https://www.youtube.com/watch?v=4CykZVqBuCw

def selection_sort(alist):
    # for every element in list alist -1 (until second last index, we can assume the last element in the highest value)
    for i in range(len(alist)-1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements to the right of min_index = 1
        for j in range(i+1, len(alist)):
            # Update the min_index if the element at j is lower than min_index
            if alist[j] < alist[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        alist[i], alist[min_index] = alist[min_index], alist[i] 
    return alist


# Demonstration Insertion Sort
# Adapted from https://stackabuse.com/sorting-algorithms-in-python/#insertionsort

def insertion_sort(alist):
    # For every value in alist. There would be no item to the left of the first item so we start at the second element and assume the first element is sorted.
    # Go through 1 by 1 the length of the list so it can be sorted. created variable for the current item in the loop
    for i in range(1, len(alist)):
        currentValue = alist[i] 
        # Let i equal to position to allow manipulation of i
        position = i
        
        
        #while position is greater than 0 and value at current value is less than the one before it
    
        while position > 0 and alist[position - 1] > currentValue:

        #move current value to the position to its left
            alist[position] = alist[position - 1]
        #do for the next value to its left
            position -= 1
        # Insert the item at the appropiate index
        alist[position] = currentValue
    return alist


# Demonstration Insertion Sort
# Adapted from https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html
# Adapted from https://www.youtube.com/watch?v=CB_NCoxzQnk

#  define function quicksort
def quick_sort(alist):
   quickSortHelper(alist,0,len(alist)-1) # call the recursive function with list, starting index & end index

# define function quickSortHelper (this is a recursive function) which takes 3 parameters
def quickSortHelper(alist,first,last):
   if first<last: # if there is more than one element/item to be sorted. If the 1st index is less than the last

       pivot = partition(alist,first,last) # create variable pivot by calling partition function which takes same 3 parameters

        # then call recursive function to sort elements between 1st and left of the pivot using partition function
       quickSortHelper(alist,first,pivot-1)
       # then call recursive function to sort elements between right of the pivot and the last element using partition function
       quickSortHelper(alist,pivot+1,last)

# There are different ways to do a Quick Sort partition
# you can select the first, middle or last elements to be the pivot value. Or even the median of all 3
# in this example, the first element was chosen 

# define function called partition with same 3 parameters as above
def partition(alist,first,last):
   pivotvalue = alist[first] # select first element in array as pivot value

   leftmark = first+1 # create variable left mark which is the first index+1. position after the pivotvalue
   rightmark = last # create variable called right mark which is the last index

   done = False 

   # while sort not complete
   while not done:
       # while left marker less than or equal to right marker(last) and left marker value is less than equal to pivot value
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           #left marker moves right to the next index
           leftmark = leftmark + 1
        # while value of the right marker is greater than or equal to pivot value and right mark ir greater than
        #or equal to left mark
       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           #right marker moves in left direction to the next index
           rightmark = rightmark -1

        # if right mark less than left mark
       if rightmark < leftmark:
           done = True # end the while loop
       else: #else create temp variable which is the value of left mark
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark] # swap the values at the left and right markers
           alist[rightmark] = temp # now variable is equal to the right marker value

   temp = alist[first] # create variable which is value of first index
   alist[first] = alist[rightmark] # value of first index is swapped with value of right mark
   alist[rightmark] = temp # variable is now is equal right marker value. Which is the pivot point. 


   return rightmark

# Count Sort Demonstration
# Adapted from https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php

#define function called counting_Sort. Takes 2 arguments - array to be sorted (array 1)and max value in array 
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


# code sourced from project example
# Creating an array using randint
from random import *

# creating a random array, function takes in n numbers
def random_array(n):
    # create an array variable
    array = []
    # if n = 10, 0,1,2,3,4,,,9
    for i in range(0, n, 1):
        # add to the array random integers between 0 and 100
        array.append(randint(0,100))
    return array

#Benchmarking
# Code Adapted from https://github.com/MarianneLawless/Project-Benchmarking-Sorting-Algorithms/blob/master/BubbleSort.py
# Adapted the benchmark code example for bubble sort algotithm to apply to all other algorithms in this project
# Code Adapted from Lecture notes: Benchmarking in Python
# Code Adapted from https://gethowstuff.com/python-elapsed-time-milliseconds/

global bubble_avg
bubble_avg = []
runs= 10 # 10 iterations at each input n
results = [] 


#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(100) # input n
    bubble_sort(alist) # call bubble sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
bubble_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(250) # input n
    bubble_sort(alist) # call bubble sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3) 
bubble_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(500) # input n
    bubble_sort(alist) # call bubble sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)   
bubble_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(750) # input n
    bubble_sort(alist) # call bubble sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)   
bubble_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(1000) # input n
    bubble_sort(alist) # call bubble sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)   
bubble_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(1250) # input n
    bubble_sort(alist) # call bubble sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)   
bubble_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(2500) # input n
    bubble_sort(alist) # call bubble sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)   
bubble_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(3750) # input n
    bubble_sort(alist) # call bubble sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)   
bubble_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(5000) # input n
    bubble_sort(alist) # call bubble sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)   
bubble_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(6250) # input n
    bubble_sort(alist) # call bubble sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)   
bubble_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(7500) # input n
    bubble_sort(alist) # call bubble sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)   
bubble_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(8500) # input n
    bubble_sort(alist) # call bubble sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)   
bubble_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(10000) # input n
    bubble_sort(alist) # call bubble sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)   
bubble_avg.append(avg_runtime)

print("Bubble", bubble_avg)

global selection_avg
selection_avg = []
runs= 10 # 10 iterations at each input n
results = [] 


#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(100) # input n
    selection_sort(alist) # call selection sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
selection_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(250) # input n
    selection_sort(alist) # call selection sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
selection_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(500) # input n
    selection_sort(alist) # call selection sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
selection_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(750) # input n
    selection_sort(alist) # call selection sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
selection_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(1000) # input n
    selection_sort(alist) # call selection sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
selection_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(1250) # input n
    selection_sort(alist) # call selection sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
selection_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(2500) # input n
    selection_sort(alist) # call selection sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
selection_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(3750) # input n
    selection_sort(alist) # call selection sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
selection_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(5000) # input n
    selection_sort(alist) # call selection sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
selection_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(6250) # input n
    selection_sort(alist) # call selection sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
selection_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(7500) # input n
    selection_sort(alist) # call selection sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
selection_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(8500) # input n
    selection_sort(alist) # call selection sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
selection_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(10000) # input n
    selection_sort(alist) # call selection sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
selection_avg.append(avg_runtime)


print("Selection", selection_avg)

global insertion_avg
insertion_avg = []
runs= 10 # 10 iterations at each input n
results = [] 


#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(100) # input n
    insertion_sort(alist) # call insertion sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
insertion_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(250) # input n
    insertion_sort(alist) # call insertion sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
insertion_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(500) # input n
    insertion_sort(alist) # call insertion sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
insertion_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(750) # input n
    insertion_sort(alist) # call insertion sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
insertion_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(1000) # input n
    insertion_sort(alist) # call insertion sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
insertion_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(1250) # input n
    insertion_sort(alist) # call insertion sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
insertion_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(2500) # input n
    insertion_sort(alist) # call insertion sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
insertion_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(3750) # input n
    insertion_sort(alist) # call insertion sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
insertion_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(5000) # input n
    insertion_sort(alist) # call insertion sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
insertion_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(6250) # input n
    insertion_sort(alist) # call insertion sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
insertion_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(7500) # input n
    insertion_sort(alist) # call insertion sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
insertion_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(8500) # input n
    insertion_sort(alist) # call insertion sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
insertion_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(10000) # input n
    insertion_sort(alist) # call insertion sort
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average (using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
insertion_avg.append(avg_runtime)


print("Insertion", insertion_avg)

global quick_avg
quick_avg = []
runs= 10 # 10 iterations at each input n
results = [] 

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time()
    #although the algorithm takes 3 arguments. They are on the recursive function. quick_sort only takes one argument
    alist = random_array(100) # input n
    quick_sort(alist) # call quick sort
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
    alist = random_array(250) # input n
    quick_sort(alist) # call quick sort
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
    alist = random_array(500) # input n
    quick_sort(alist) # call quick sort
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
    alist = random_array(750) # input n
    quick_sort(alist) # call quick sort
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
    quick_sort(alist) # call quick sort
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
    alist = random_array(1250) # input n
    quick_sort(alist) # call quick sort
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
    alist = random_array(2500) # input n
    quick_sort(alist) # call quick sort
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
    alist = random_array(3750) # input n
    quick_sort(alist) # call quick sort
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
    alist = random_array(5000) # input n
    quick_sort(alist) # call quick sort
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
    alist = random_array(6250) # input n
    quick_sort(alist) # call quick sort
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
    alist = random_array(7500) # input n
    quick_sort(alist) # call quick sort
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
    alist = random_array(8500) # input n
    quick_sort(alist) # call quick sort
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
    alist = random_array(10000) # input n
    quick_sort(alist) # call quick sort
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

global count_avg
count_avg = []
runs= 10 # 10 iterations at each input n
results = [] 


#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(100) # input n
    max_val = max(alist) # get the max value of the array
    counting_sort(alist, max_val) # call counting sort. It takes 2 arguements
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average of all 10 runs(using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
count_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(250) # input n
    max_val = max(alist) # get the max value of the array
    counting_sort(alist, max_val) # call counting sort. It takes 2 arguements
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average of all 10 runs(using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
count_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(500) # input n
    max_val = max(alist) # get the max value of the array
    counting_sort(alist, max_val) # call counting sort. It takes 2 arguements
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average of all 10 runs(using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
count_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(750) # input n
    max_val = max(alist) # get the max value of the array
    counting_sort(alist, max_val) # call counting sort. It takes 2 arguements
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average of all 10 runs(using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
count_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(1000) # input n
    max_val = max(alist) # get the max value of the array
    counting_sort(alist, max_val) # call counting sort. It takes 2 arguements
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average of all 10 runs(using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
count_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(1250) # input n
    max_val = max(alist) # get the max value of the array
    counting_sort(alist, max_val) # call counting sort. It takes 2 arguements
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average of all 10 runs(using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
count_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(2500) # input n
    max_val = max(alist) # get the max value of the array
    counting_sort(alist, max_val) # call counting sort. It takes 2 arguements
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average of all 10 runs(using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
count_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(3750) # input n
    max_val = max(alist) # get the max value of the array
    counting_sort(alist, max_val) # call counting sort. It takes 2 arguements
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average of all 10 runs(using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
count_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(5000) # input n
    max_val = max(alist) # get the max value of the array
    counting_sort(alist, max_val) # call counting sort. It takes 2 arguements
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average of all 10 runs(using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
count_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(6250) # input n
    max_val = max(alist) # get the max value of the array
    counting_sort(alist, max_val) # call counting sort. It takes 2 arguements
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average of all 10 runs(using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
count_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(7500) # input n
    max_val = max(alist) # get the max value of the array
    counting_sort(alist, max_val) # call counting sort. It takes 2 arguements
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average of all 10 runs(using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
count_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(8500) # input n
    max_val = max(alist) # get the max value of the array
    counting_sort(alist, max_val) # call counting sort. It takes 2 arguements
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average of all 10 runs(using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
count_avg.append(avg_runtime)

#for each run in runs
for r in range(runs):
    # Get the Start time (s)
    start_time = time.time() 
    alist = random_array(10000) # input n
    max_val = max(alist) # get the max value of the array
    counting_sort(alist, max_val) # call counting sort. It takes 2 arguements
    # Get the finish time (s)
    end_time = time.time()
    # Calculate difference between finish and start times
    # Change to milliseconds (as per project specification)
    time_taken = (end_time - start_time) * 1000
    # Place run time taken for each run into array 
    results.append(time_taken)

# calculate average of all 10 runs(using numpy). Rounded to 3 decimal places
avg_runtime = round((np.average(results)),3)  
count_avg.append(avg_runtime)

print("Counting", count_avg)

#put outputs into a dataframe under the appropiare headings
df = pd.DataFrame(columns = ['Size','Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Quick Sort', 'Counting Sort'])
#Input size n
df['Size'] = [100, 250, 500, 750, 1000, 1250, 2500, 3570, 5000, 6250, 7500, 8500, 10000]


df['Bubble Sort'] = bubble_avg
df['Selection Sort'] = selection_avg
df['Insertion Sort'] = insertion_avg
df['Quick Sort'] = quick_avg
df['Counting Sort'] = count_avg

print (df) # print dataframe

#use transpose function to put table in format as per project specification
print(df.transpose())

#plot 

#Code adapted from https://github.com/RitRa/Algorithms-project-
#give the plot a Title
title="Benchmarking Sorting Algorithms"
#Set aesthetic parameters
#use of darkgrid and rainbow palettefor contrast
#rc ‘run command’ used with sns.set will override standard
#use figure with the figsize keyword to set dimensions
sns.set(style="darkgrid", palette="gist_rainbow",font_scale = 2, rc={'figure.figsize':(20,10)})
#Load the data from pd Dataframe created from the average lists in previous benchmarking steps
#If bubble sort data is omitted, the results of the other algorithms can be seen more clearly.
#bubble = sns.lineplot( x="Size", y="Bubble Sort", data=df, marker='o', label="Bubble Sort")
bubble = sns.lineplot( x="Size", y="Bubble Sort", data=df, marker='o', label="Bubble Sort")
selection = sns.lineplot( x="Size", y="Selection Sort", data=df, marker=">", label="Selection Sort")
insertion = sns.lineplot( x="Size", y="Insertion Sort", data=df, marker=">",  label="Insertion Sort")
quick = sns.lineplot( x="Size", y="Quick Sort", data=df, marker=">",  label="Quick Sort")
counting = sns.lineplot( x="Size", y="Counting Sort", data=df, marker=">", label="Counting Sort")
#Insert instruction for axes and plot title
plt.xlabel('Random Array size n', fontsize=20)
plt.ylabel('Running Time in milliseconds',fontsize=20)
plt.title(title, fontsize=26)

# Call show to display data visualisation
plt.show()