# Best Time to Buy and Sell Stock - Leetcode 121


def maxProfit(prices):
    l, r = 0, 1 # we need two pointers and the time complexity will stay O(N)
    # r is going to also initialized at the for loop. I keep both for illustration purposes
    maxProfit = 0
    
    for r in range(1, len(prices)):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(profit, maxProfit)
        else:
            l = r
    return(maxProfit)

print(maxProfit([7,1,5,3,6,4]))