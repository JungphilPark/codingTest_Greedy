def GreedyRet(val):             # If units of money are multiple of ohers, you can use Greedy algorithm.
    print("----------GreedyRet----------")
    ans = 0                     # Number of coins you hace to return.
    list = [500,100,50,10]      # Units of coins.
    for i in list:
        ans = ans + val // i
        val = val % i
    return ans

def LawOfBigNum(val1, val2, val3, list):    # return add of maximum of list's vals.
    #(val1 : size of list, val2: num of add, val3: limit of sequence.)
    print("----------LawOfBigNum----------")
    ans = 0
    list.sort()                             # sort list des.
    fst = list[val1-1]                      # max of list
    snd  = list[val1-2]                     # 2nd max of list
    cnt = 1
    while True:
        if val2 <= 0:
            break
        if cnt % val3 != 0:
            ans = ans + fst
        else:
            ans = ans + snd
        val2 = val2 - 1
        cnt = cnt + 1
    return ans

print(GreedyRet(1260))
print(LawOfBigNum(5, 8, 3, [2,4,5,4,6]))