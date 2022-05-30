import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))

print(max(arr)-min(arr))