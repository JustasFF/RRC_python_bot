def maxProfit(prices: list[int]) -> int:
    maks = 0
    minm = prices[0]
    for i,k in enumerate(prices):
        minm = min(minm,k)
        maks = max(maks,k-minm)
    return maks

assert(maxProfit([7,1,5,3,6,4])) == 5, 'Что то не так...'