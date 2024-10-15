## Counting Sort

**Description**

Counting sort is an algorithm that works by counting the number of occurences of each distinct element in an array.

**How It Works**

  1. Count the numvber of occurences of each element
  2. Modify the count array to store cumulative counts
  3. Place elements in correct position based on the cumulative counts

**Python Code**

```python
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    for i in arr:
        count[i] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in arr:
        output[count[i] - 1] = i
        count[i] -= 1

    return output
```

**Time Complexity**

- Best: O(n + k) *(where k  is the range of the input)*

- Average: O(n + k)

- Worst: O(n + k)

**Space Complexity**

- O(n + k)

**Stability** 

- This algorithm is stable

**Applications**

As long as it isn't used for comparisions, Counting Sort is inherently good to sort anything with good efficiency. Some good examples are sorting people by age or alphabet.
