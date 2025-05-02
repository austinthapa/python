def best_construct(target, arr, memo = {}):
    if target in memo: return memo[target]
    if target == '': return []
    s_c = None
    
    for word in arr:
        if target.startswith(word):
            new_target = target[len(word):]
            results = best_construct(new_target, arr, memo)
            
            if results is not None:
                c_c = [word] + results
                
                if s_c is None or len(s_c) > len(c_c):
                    s_c = c_c
                    
    memo[target] = s_c
    return s_c


print(best_construct('target', ['t', 'ar', 'ge', 'tar', 'get','targ', 'et', 'arg', 'et']))
print(best_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(best_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(best_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(best_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee', ['e', 'ee', 'eeee', 'eeeeee', 'eeeeeee', 'eeeeeeee']))