n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

minimum = arr[0]
maximum = arr[0]

for i in range(1, n):
    if arr[i] < minimum:
        minimum = arr[i]
    if arr[i] > maximum:
        maximum = arr[i]

print("Smallest element:", minimum)
print("Largest element:", maximum)
