# Demonstration Insertion Sort
# Adopted from https://stackabuse.com/sorting-algorithms-in-python/#insertionsort

def insertion(alist):
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

alist = [54,26,93,17,77,31,44,55,20]
insertion(alist)
print(alist)

# Move all items of the sorted segment forward if they are larger than
        # the item to insert