# Demonstration Selection Sort
# Adopted from https://www.pythoncentral.io/selection-sort-implementation-guide/
# Adopted from https://www.youtube.com/watch?v=4CykZVqBuCw

def selection(alist):
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


alist = [54,26,93,17,77,31,44,55,20]
selection(alist)
print(alist)