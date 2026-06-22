import time

# Interpolation Search
def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and key >= arr[low] and key <= arr[high]:
        comparisons += 1

        pos = low + ((key - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == key:
            return pos, comparisons

        elif arr[pos] < key:
            low = pos + 1

        else:
            high = pos - 1

    return -1, comparisons


# Input
n = int(input("Enter number of elements: "))

# Uniformly distributed sorted array
arr = [i * 10 for i in range(n)]

print("Array:", arr)

key = int(input("Enter search key: "))

# Measure time
start = time.time()
position, comparisons = interpolation_search(arr, key)
end = time.time()

# Output
if position != -1:
    print("Element found at position:", position)
else:
    print("Element not found")

print("Comparisons:", comparisons)
print("Execution Time:", end - start, "seconds")

print("Time Complexity: O(log log n) (Average)")
print("Space Complexity: O(1)")