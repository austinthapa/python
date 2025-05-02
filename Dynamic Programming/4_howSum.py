def howSum(target, arr, memo = []):
    if target in memo: return memo[target]
    if target < 0: return -1
    if target == 0: return []
    
    for num in arr:
        remainder = target - num
        results = howSum(remainder, arr, memo)
        if results != -1:
            memo.append(num)
            return memo
    return -1
    


print(howSum(100, [7, 9, 17]))