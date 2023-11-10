'''
Joe Kennedy
March 4, 2023
CIS-2532-NET01
Program: Sorting algorithms

This program creates various sorting algorithms for use with other
external programs
'''
import random
import time

'''
Optimized Bubble sort in Python
'''
def bubbleSort(array):
    
  # loop through each element of array
  for i in range(len(array)):
        
    # keep track of swapping
    swapped = False
    
    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping occurs if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

        swapped = True
          
    # no swapping means the array is already sorted
    # so no need for further comparison
    if not swapped:
      break
'''
Shell sort in python
'''
def shellSort(array, n):
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

'''
Quick sort in Python
'''
def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
 
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


data = []
for i in range(0,10000):
    x = random.randint(0,10000)
    data.append(x)
size = len(data)

'''
#Start the clock
start_time = time.time()
#Run bubble sort
bubbleSort(data)
#stop clock and calculate the time it took
stop_time = time.time() - start_time
print("the bubblesort took %s seconds" % stop_time)
'''

'''
#Start the clock
start_time = time.time()
#run shell sort
shellSort(data, size)
#stop clock and calculate the time it took
stop_time = time.time() - start_time
print('The shellsort took %s seconds' % stop_time)
'''

'''
#Start the clock
start_time = time.time()
#run shell sort
quickSort(data)
#stop clock and calculate the time it took
stop_time = time.time() - start_time
print('The quicksort took %s seconds' % stop_time)
'''
#quickSort(data, 0, size-1)
#print(data)
#print('Sorted Array in Ascending Order:')
#print(data)