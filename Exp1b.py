def binary_search(n, arr, key):
    low = 0
    high = n - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if key == arr[mid]:
            return mid + 1  # Returning 1-based position matching the expected output
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
            
    return -1


if __name__ == "__main__":
    try:
        n = int(input("Enter size of array : "))
    except ValueError:
        n = 5

    arr = []
    print("Enter arr")
    for i in range(n):
        val = int(input("Element :"))
        arr.append(val)

    try:
        key = int(input("Enter key: "))
    except ValueError:
        key = 0

    res = binary_search(n, arr, key)
    
    if res == -1:
        print("Unsuccessful Search")
    else:
        print(f"{key} found at {res}")
