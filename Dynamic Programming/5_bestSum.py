def bestSum(target, arr, memo = {}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None
    s_comb = None
    
    for num in arr:
        remainder = target - num
        results = bestSum(remainder, arr, memo)
        if results is not None:
            c_comb = results + [num]
            
            if s_comb is None or len(c_comb) < len(s_comb):
                s_comb = c_comb
    memo[target] = s_comb
    return s_comb

print(bestSum(7, [5, 3, 4, 7]))
print(bestSum(8, [5, 3, 2]))
print(bestSum(8, [1, 4, 5]))
print(bestSum(100, [1, 2, 5, 25]))