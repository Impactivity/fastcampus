import sys

read = sys.stdin.readline
inpt = list(map(str,read().rstrip()))

i = 0
while i < len(inpt):
    if inpt[i] == '<':
        while i < len(inpt) and inpt[i] != '>':
            i += 1
    elif inpt[i].isalnum():
        start = i
        while i < len(inpt) and inpt[i].isalnum():
            i += 1
        inpt[start:i] = inpt[start:i][::-1]
        continue
    i += 1
print("".join(inpt))


