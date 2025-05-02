def solution(nums):
    seen = set()
    for num in nums:
        if 2 * num in seen or (num // 2 in seen and num % 2 == 0):
            return True
        set.add(num)