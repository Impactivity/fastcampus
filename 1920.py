import sys
read = sys.stdin.readline

# solution 1
N,A = int(read()) , {i : 1 for i in map(int,read.split())}
M = int(read())
for num in list(map(int,read().split())):
    print(A.get(num,0))



# solution2
# N = int(read())
# A = list(map(int,read().split()))
# M = int(read())
# M_ARR = list(map(int,read().split()))
#
# A.sort()
#
# for num in M_ARR:
#     l = 0
#     r = len(A)-1
#     YN = False
#     while l <= r:
#         mid = (l + r) // 2
#
#         if A[mid] == num:
#             YN = True
#             break
#         elif A[mid] > num:
#             r = mid - 1
#         elif A[mid] < num:
#             l = mid + 1
#
#     if YN == True:
#         print(1)
#     else:
#         print(0)


