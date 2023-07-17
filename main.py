def coin_stair(n):
    i = 1
    while(True):
        sum = (i *(i+ 1) )//2
        if sum == n:
            return i
        elif sum > n:
            if (i-1 * i)//2 < n and n < sum:
                return i-1
        i += 1

print(coin_stair(5))
