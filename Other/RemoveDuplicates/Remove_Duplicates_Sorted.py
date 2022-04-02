# 1_________________ 
# O(n) extra space!
# def remove_duplicate( A, N):
#     new = []
#     old = A[0]
#     for i in range(N):
#         if A[i] != old:
#             new.append(old)
#             old = A[i]
#     new.append(A[N-1])
#     print(new)

# 2_________________
# O(1) extra space
def remove_duplicate( A, N):
    idx = 0
    for i in range(N):
        if A[idx] != A[i]:
            idx += 1
            A[idx] = A[i]
    return idx + 1  #the number of elements in answer

if __name__ == "__main__":
    A = [1,1,1,2,2,3,4,5,6,6,6]
    N = 11
    remove_duplicate(A, N)