# GFG Problem: https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
# Title: Reverse an Array
# Difficulty: Easy
# Tags: Array, Two Pointers

def reverse_array(arr):
    """
    Reverse the given array in-place
    """
    start = 0
    end = len(arr) - 1
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)
    
    reverse_array(arr)
    print("Reversed array:", arr)
    
    # Test case 2
    arr2 = [10, 20, 30, 40]
    print("\nOriginal array:", arr2)
    reverse_array(arr2)
    print("Reversed array:", arr2)
