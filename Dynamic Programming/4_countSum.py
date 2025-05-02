def countSum(target, arr, memo = {}):
    if target in memo: return memo[target]
    if target < 0: return 0
    if target == 0: return 1
    total = 0
    
    for num in arr:
        remainder = target - num
        total += countSum(remainder, arr, memo)
    memo[target] = total
    return total
        
print(countSum(100, [3, 9, 13]))