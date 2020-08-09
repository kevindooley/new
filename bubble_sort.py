# Demonstration bubble sort
# Adopted from source https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheBubbleSort.html
# Supportive source https://www.youtube.com/watch?v=Vca808JTbI8

def bubbleSort(alist): #define function called bubbleSort
    for passnum in range(len(alist)-1,0,-1): # create outer for loop starting from second last index of alist to index 0
        for i in range(passnum): # inner loop now has a new range and goes until passnum. Largest number at the end
            if alist[i]>alist[i+1]: # if first value is greater than the value beside it, swap them
                temp = alist[i] # create temp variable
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)