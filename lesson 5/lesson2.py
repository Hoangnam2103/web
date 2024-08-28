A = [1,2,5,6,4,8,9]
for i in range(len(A)):
    if i % 3 ==0:
        sum +=A[i]
print(sum)

A = [1,2,3]
B = [2,4]
for i in A:
    for k in B:
        if i == k:
            print(i)