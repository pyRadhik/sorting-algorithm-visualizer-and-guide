## Radix Sort

**Description**

Radix sort works by processing each digit individually, starting from least to most significant digit. 

**How It Works**

  1. Sort each digit using a **stable** algorithm *(Counting Sort is often used here)*
  2. Process from the least significant digit to most significant digit

**Python Code**

```python
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr
```

**Time Complexity**

- Best: O(n * k) *refer to coutning sort*

- Average: O(n * k)

- Worst: O(n * k)

**Space Complexity**

- O(n + k)

**Stability** 

- This algorithm is stable

**Applications**

Radix sort is often used to sort arrays with fixed integers or strings.
