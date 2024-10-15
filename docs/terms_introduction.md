# First let's get our terms sorted! (no pun intened)

### Time Complexity (Big O)

Time Complexity, also known as Big O, is the measure of the amount of time it takes for an algorithm to sort data.

Big O notation is usually displayed as **O(n)** with the variable 'n' representing the input size of the data and O(n) representing time to sort. It represents the upperbound (worst-case scenario) of the algorithm's efficiency.

Some examples of time complexities include but are not limited to:

* **O(1)**

  * This is a constant time complexity
  
  * This means that no matter how large the input size is, the execution time remains constant

  * Example: Adding element or removing element from the end of an array

* **O(n)**

  * This is a linear time complexity

  * This means that the execution time has a linear relationship with the input size

  * Example: Examining all elements in an array using a for loop

* **O(n^2)**

  * This is a quadratic time complexity

  * This means that the time grows quadratically as the input size increases

  * Example: Examining all elements in an array using a nested for loop (a loop placed inside another loop)

* **O(n^3)**

  * This is a cubic time complexity

  * This means that the time grows cubically as the input size increases

  * Example: Similar to O(n^2) multiple nested for loops to increase the time at a quicker rate

* **O(n * m)** 

  * This is a non-square time complexity using multiple diminsions

  * It is similar to O(n^2) where depending on two input sizes, the rate at which the time increases varies

  * Example: Similar to O(n^2) and O(n^3) where you can use nested for loops when the loops are different lengths


* **O(log n)**

  * This is a logarithamic time complexity

  * This means that the time grows logarithamically as the input size increases

  * Example: Binary search where sample size is cut in half every iteration

* **O(n log n)**

  * This is a linearithamic time complexity

  * This means that the time grows at a lot lesser rate than O(n^2) and only a tad greater rate than O(n)

  * Example: Most built in sorting algorithms have a O(n log n) time complexity

* **O(2^n)**

  * This is just one example of exponential time complexity using the constant 2

  * This means that the time doubles as the input size increases

  * Example: Found in recursion

* **O(√n)**

  * This is a square root time complexity

  * This means that as *n* increases the time increases at a slower rate

  * Examples: Finding factors of a number

* **(O(n!))**

  * This is a factorial time complexity

  * This means that time grows very quickly as the input size goes up. Specifically, the rate at which it increases depends on the factorial of a number

  * Examples: Generating all permutations of a list of size *n*. For example, generating all possible ways to arrange a group of items.



### Space Complexity

Space Complexity is a measure of the amount of space (memory) that an algorithm or program needs to use in relation to the input size. It expresses the amount of additional memory as the input size grows. Space Complexity is also expressed in Big O Notation, O(n).

Like Time Complexity, Space complexity can have a constant space which means the algorithm doesn't call for an increase or decrease in space. It can also have a variable space meaning that the memory grows based on input size. 

Space complexities are similar to Time Complexities in the way their relationships are denoted via their same notations.

**Examples of Constant Space**

* O(1)

* O(e^2)

* O(log 3)

**Examples of Variable Space**

* O(n)

* O(n^2)

* O(log n)

### Stability

A stable sorting algorithm maintains the relative order of items with equal sort keys. For example, if you sort an array of people by age, a stable sort will keep people with the same age in the same order. An unstable sort might put people with the same age in a different order.

### Summary

Time Complexities and Space Complexities both use input sizes to quantify the amount of time/space needed for the execution of the algorithm. They are both denoted the same using Big-O.

![graph](<../images-assets/complexity graph.png>)

<br>
<br>

**Hopefully you have a good grasp of the fundamental terms that are associated with Sorting Algorithms.**

**Now let's have some fun!**



