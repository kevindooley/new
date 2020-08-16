# Count Sort Demonstration
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php

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

print(counting_sort( [1, 2, 7, 3, 99, 1, 4, 2, 3, 2, 1], 100 ))