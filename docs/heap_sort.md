## Heap Sort

**Description**

Heap Sort using comparisons to sort arrays using a binary heap data structure. Basically, it turns the array into something called a heap and sorts it by extracting the maximum element each time to create a sorted list. 

**How It Works**

  1. Build a max heap from array
  2. Swap the root of the heap with the last element
  3. Heapify the root to maintain the max heap property, repeat the process till full array is sorted

**Python Code**

```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
```

**Time Complexity**

- Best: O(n log n)

- Average: O(n log n)

- Worst: O(n log n)

**Space Complexity**

- O(1)

**Stability** 

- This algorithm is not stable

**Applications**

Heap sorting is mainly used in priority queues: when you need to quickly find and remove the highest or lowest priority item from a collection. But, you can also implement it if you have limited access memory, as it sorts the data in place using comparisons. 
