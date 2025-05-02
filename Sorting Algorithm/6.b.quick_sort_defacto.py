def quicksort(arr, low, high):
    if low < high:
        # Find pivot position
        pivot_index = partition(arr, low, high)
        
        # Recursively sort the subarrays
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    # Use median-of-three pivot selection
    mid = (low + high) // 2
    
    # Sort low, mid, high values
    if arr[mid] < arr[low]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[high] < arr[low]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[high] < arr[mid]:
        arr[mid], arr[high] = arr[high], arr[mid]
    
    # Place pivot (median value) at high-1
    pivot = arr[mid]
    arr[mid], arr[high-1] = arr[high-1], arr[mid]
    
    # Partition around the pivot
    i = low
    j = high - 1
    
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        
        j -= 1
        while arr[j] > pivot:
            j -= 1
            
        if i >= j:
            break
            
        arr[i], arr[j] = arr[j], arr[i]
    
    # Restore pivot
    arr[i], arr[high-1] = arr[high-1], arr[i]
    return i

# Initialize the sort
def sort(arr):
    if len(arr) <= 1:
        return arr
    quicksort(arr, 0, len(arr) - 1)
    return arr

arr = [22, 26, 48, 54, 58, 59, 62, 72, 75, 76, 83, 85, 123, 143, 148, 150, 170, 184, 185, 193]
print(sort(arr))