# Demonstration Insertion Sort
# https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html
# https://www.youtube.com/watch?v=CB_NCoxzQnk

#  define function quicksort
def quickSort(alist):
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

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
