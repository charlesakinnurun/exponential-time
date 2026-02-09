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