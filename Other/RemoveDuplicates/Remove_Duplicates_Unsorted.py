"""
Print distinct array elements according to their first occurrence
"""

def remove_duplicates(arr, n):
    mapp = {i:0 for i in arr}
    for i in range(n):
        if mapp[arr[i]]==0:
            print(arr[i], end=" ")
            mapp[arr[i]] += 1

if __name__ == "__main__":
    arr = [3,4,2,5,6,7,5,8,9,1,2,3,4]
    n = len(arr)
    remove_duplicates(arr, n)
