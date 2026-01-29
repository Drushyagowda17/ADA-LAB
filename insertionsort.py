def insertion_sort(arr):
    for i in range(len(arr)):
        j = i - 1
        v = arr[i]
        while j >= 0 and arr[j] > v:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = v

    print(arr)

if __name__ == "__main__":
    arr = list(map(int,input("Enter the Elements:").split()))
    insertion_sort(arr)
        
            