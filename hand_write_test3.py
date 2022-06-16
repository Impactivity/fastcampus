import sys

read = sys.stdin.readline

stock_prices = list(map(int, read().split()))


def max_profit(stock_prices):
    start_idx = 0
    max_price = 0
    answer = []

    for i in range(1,len(stock_prices)):
        if stock_prices[i] >= stock_prices[i-1]:
            end_idx = i
        else:
            max_price = max(max_price, stock_prices[end_idx] - stock_prices[start_idx])
            answer.append([max_price,start_idx,end_idx])

    if len(answer) == 0:
        answer.append([stock_prices[end_idx] - stock_prices[start_idx], start_idx,end_idx])

    return answer[-1]

mx_price, st_idx , ed_idx = max_profit(stock_prices)

print(mx_price,st_idx,ed_idx)


