def binary_search(arr, left, right, x):
    if left <= right:
        middle = left + (right - left) // 2
        #if x is on the middle
        if arr[middle] == x:
            return middle
        #if x is in right subarray
        elif x > arr[middle]:
            return binary_search(arr, middle+1, right, x)
        #if x is in left subarray
        else:
            return binary_search(arr, left, middle-1, x) 
    else:
        return "NO"      

if __name__ == "__main__":
    arr = [1,4,5,7,23,34,45,56,67,78,79]
    x = 23
    result = binary_search(arr, 0, len(arr)-1, x)
    print(f"{x} is on the {result} place")

            