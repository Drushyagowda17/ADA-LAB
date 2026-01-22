arr = list(map(int, input("Enter the elements:").split()))
n = len(arr)
for i in range(n):
    index = i
    for j in range(i + 1, n):
        if arr[j] < arr[index]:
            index = j
    arr[i], arr[index] = arr[index], arr[i]

print(arr)
