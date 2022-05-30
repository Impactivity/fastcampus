import sys
read = sys.stdin.readline

alp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
N,M = map(int,read().split())
A,B = read().split()
AB = ''

min_len = min(N,M)
for i in range(min_len):
    AB += A[i] + B[i]

AB += A[min_len:] + B[min_len:]

numbers = list(alp[ord(a) - ord('A')] for a in AB )

for j in range(1,len(AB)-1):
    for i in range(0,len(AB)-j):
        numbers[i] = numbers[i] + numbers[i+1]

print("{}%".format(numbers[0] % 10 * 10 + numbers[1] % 10))

# solution 2
# dic = {'A' : 3, 'B' : 2, 'C' : 1, 'D' : 2, 'E' : 4, 'F' : 3 , 'G' : 1, 'H' : 3, 'I':1, 'J':1,'K':3,'L':1,'M':3,'N':2
#        ,'O':1,'P':2,'Q':2,'R':2,'S':1,'T':2,'U':1,'V':1,'W':1,'X':2,'Y':2,'Z':1}
#
# N,M = map(int,read().split())
# A,B = read().split()
# letter = []
# A_len = len(A)
# B_len = len(B)
# tot_len = A_len + B_len
# for i in range(tot_len):
#     if A_len > i:
#         letter.append(A[i])
#     if B_len > i:
#         letter.append(B[i])
#
# numbers = [0] * tot_len
# for i in range(tot_len):
#     numbers[i] = dic[letter[i]]
#
#
# for j in range(1,tot_len-1):
#     for i in range(0,tot_len-j):
#         numbers[i] = (numbers[i] + numbers[i+1]) % 10
#     numbers = numbers[:-1]
#
# if numbers[0] == 0:
#     del numbers[0]
#
# print(''.join(map(str,numbers)) + '%')

