# Exponential‑Time

**Explanation of Exponential Time Complexity (O(2ⁿ))**

This repository provides examples and explanations related to **exponential time complexity** — a class of algorithmic running times where the number of operations grows **exponentially** with the size of the input.

---

## 📊 What Is Exponential Time (O(2ⁿ))?

In algorithm and complexity analysis, **exponential time complexity** refers to algorithms whose running time **increases exponentially** as the input size `n` increases. A common form of this is:


This means that **each additional element in the input roughly doubles** the amount of work the algorithm must perform. As a result, the running time grows **very quickly** and becomes impractical even for moderate input sizes.




---

## 📌 Common Examples of O(2ⁿ) Algorithms

Typical algorithms that exhibit exponential time complexity include:

- **Naive recursive Fibonacci calculation:** Each call to calculate `fib(n)` calls two further recursive calls, roughly doubling the number of operations. 
- **Generating all subsets of a set:** With `n` elements, there are 2ⁿ possible subsets, and a brute‑force algorithm will explore them all.
- **Brute‑force combinatorial search:** Algorithms that try every possible combination or arrangement often grow exponentially. 

---

## 🧪 Source Code
```python
import time
import matplotlib.pyplot as plt

def fibonacci_recursive(n):
    """
    This is a classic example of O(2^n) - Exponential Time Complexity.
    
    Why is it exponential?
    For every call to this function (where n > 1), it branches into TWO more calls:
    fibonacci_recursive(n-1) and fibonacci_recursive(n-2).
    
    The number of calls effectively doubles with each increase in 'n', 
    leading to a growth rate proportional to 2^n.
    """

    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)



def demomstrate_complexity():
    # We will track the time taken for different input sizes (n)
    input_sizes = list(range(10,31,2)) # Testing n form 10 to 30
    execution_times = []

    print(f"{"n":<10} | {"Result":<15} | {"Time (seconds)":<20}")
    print("-"*50)


    for n in input_sizes:
        start_time = time.time()

        # Calculate the Fibonacci number
        result = fibonacci_recursive(n)

        end_time = time.time()
        duration = end_time - start_time
        execution_times.append(duration)


        print(f"{n:<10} | {result:<15} | {duration:<20.6f}")


    # Visualizing the growth
    # Notice how the curve starts flat but then shoots up vertically
    # This explosion is the hallmark of exponential growth

    plt.figure(figsize=(10,6))
    plt.plot(input_sizes,execution_times,marker="o",linestyle="--",color="red")
    plt.title("Visualization of O(2^n) - Exponential Time Complexity")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.grid(True)

    print("\n[INFO] The chart shows how time increases exponentially.")
    print("[INFO] Try increasing the range to 40, and you'll see a massive slowdown!")
    plt.show()

if __name__ == "__main__":
    """
    Exponential time complexity O(2^n) is often considered 'uncomputable' for large n.
    In real-world scenarios, algorithms with this complexity (like Brute Force 
    Password Cracking or the Traveling Salesman Problem via simple recursion) 
    become impractical very quickly.
    """
    print("Running O(2^n) Exponential Complexity Demo...\n")
    demomstrate_complexity()
```




---

## 🧠 Why It Matters

Exponential‑time algorithms are usually **very slow**, especially for larger inputs, because their running time increases much faster than linear, polynomial, or logarithmic algorithms. While exponential algorithms **might work for small inputs** or in educational examples, they are generally **not practical at scale**.
