def binary_search_with_upper_bound(arr, x):    
    low = 0    
    high = len(arr) - 1    
    iterations = 0
    upper_bound = None    
    while low <= high:        
        iterations += 1        
        mid = (high + low) // 2        
        if arr[mid] < x:        
            low = mid + 1        
        elif arr[mid] > x:        
            upper_bound = arr[mid]        
            high = mid - 1        
        else:        
            upper_bound = arr[mid]        
            return (iterations, upper_bound)
    return (iterations, upper_bound)

# Тестування функції
arr = [1.1, 1.3, 2.5, 3.8, 4.6]
print(binary_search_with_upper_bound(arr, 3.5))  # (2, 3.8)
print(binary_search_with_upper_bound(arr, 4))  # (3, 4.6)
print(binary_search_with_upper_bound(arr, 6.0))  # (3, None)
print(binary_search_with_upper_bound(arr, 2.5))  # (1, 2.5)
print(binary_search_with_upper_bound(arr, 0))  # (2, 1.1)