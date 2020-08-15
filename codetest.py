def GreedyRet(val):             # If units of money are multiple of ohers, you can use Greedy algorithm.
    ans = 0                     # Number of coins you hace to return.
    list = [500,100,50,10]      # Units of coins.
    for i in list:
        ans = ans + val // i
        val = val % i
    return ans

print(GreedyRet(1260))