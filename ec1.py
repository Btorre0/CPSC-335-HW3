# EC1 (12): Design a sorting algorithm whose time complexity is as follows:

# when the input happens to be already non-decreasing, the algorithm takes only O(n) time;
# when the input happens to be already non-increasing (i.e. reverse-sorted), the algorithm takes only O(n) time;
# but in any other situation, the algorithm may take O(n^2) time.

# Justify that your algorithm meets these efficiency goals.

def insertion_sort(arr):
    n = len(arr)
    is_sorted = True
    is_reverse_sorted = True
   
   # O(n)
    for i in range(n -1):
        if arr[i] > arr[i + 1]:
            is_sorted = False
        if arr[i] < arr[i + 1]:
            is_reverse_sorted = False
    # O(1)
    if is_sorted:
        return arr
    
    # O(n)
    if is_reverse_sorted:
        # If the array is reverse sorted, we can reverse it in O(n) time
        reversed_arr = []
        for i in range(n - 1, -1, -1):
            # Append elements in reverse order
            reversed_arr.append(arr[i])
        return reversed_arr
    else:
        # O(n^2)
        for i in range(1, n):
            # Insertion sort algorithm
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                # Move elements of arr[0..i-1], that are greater than key,
                j -= 1
            arr[j + 1] = key
        return arr
    
    
# Test the function
print(insertion_sort([1, 2, 3]))
print(insertion_sort([8, 5, 3]))