import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    n = len(arr)
    times = []
    steps = []

    for i in range(1, n):
        start_time = time.time()

        j = i - 1
        v = arr[i]
        while j >= 0 and arr[j] > v:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = v

        end_time = time.time()
        elapsed = end_time - start_time

        times.append(elapsed)
        steps.append(i)

        print(f"Time taken for element {v}: {elapsed:.6f} seconds")

    print("Sorted array:", arr)

    plt.plot(steps, times, marker='o')
    plt.xlabel("Iteration")
    plt.ylabel("Time (seconds)")
    plt.title("Insertion Sort Time per Iteration")
    plt.grid(True)
    plt.show()

arr = list(map(int, input("Enter the elements: ").split()))
insertion_sort(arr)

