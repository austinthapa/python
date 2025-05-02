def all_construct(target, arr, memo = {}):
    if target in memo: return memo[target]
    if target == '': return [[]]
    all_ways = []
    
    for word in arr:
        if target.startswith(word):
            new_target = target[len(word):]
            results = all_construct(new_target, arr, memo)
            combinations = [[word] + w for w in results]
            all_ways.extend(combinations)
    memo[target] = all_ways
    return all_ways
                

print(all_construct('target', ['t', 'ar', 'ge', 'tar', 'get','targ', 'et', 'arg', 'et']))
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(all_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(all_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eeee', 'eeeeee', 'eeeeeee', 'eeeeeeee']))