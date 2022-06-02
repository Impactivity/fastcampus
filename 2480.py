import sys

read = sys.stdin.readline
lst = sorted(list(map(int,read().split())))
print(lst)
if len(set(lst)) == 1:
    print(10000 + lst[0] * 1000)
elif len(set(lst)) == 2:
    print(1000 + lst[1] * 100)
else:
    print(lst[2] * 100)


# solution 2
# import sys
# from collections import Counter
# read = sys.stdin.readline
# dice = map(int,read().split())
# price = 0
# arr = sorted(Counter(dice).items(), key =lambda k : k[0] , reverse = True)
# arr = sorted( arr ,key =lambda k:k[1] , reverse=True)
#
# if len(arr) == 1:
#     price = 10000 + arr[0][0] * 1000
# elif len(arr) == 2:
#     price = 1000 + arr[0][0] * 100
# else:
#     price = arr[0][0] * 100
# print(price)
#
