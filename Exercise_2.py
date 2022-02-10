# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot_idx = high
    pivot = arr[pivot_idx]
    #Initialize the left and right pointers
    i = low
    j = high - 1

    while i <= j:

        #advance the ith pointer to the right if its less than pivot
        if arr[i] < pivot:
            i += 1
            continue
        
        #advance the jth pointer to the left if its more than the pivot
        if arr[j] > pivot:
            j -= 1
            continue
        #swap ith and jth pointer
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    #swap the pivot and the left pointer
    arr[pivot_idx], arr[i] = arr[i], arr[pivot_idx]
    return i
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low >= high:
        return
    
    pivot = partition(arr,low,high)
    quickSort(arr, low, pivot-1) # Quicksort on data to the left to pivot
    quickSort(arr, pivot+1, high) #Quicksort on data to the right of pivot
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
