def Two_Sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        Complement = target - num 
        if Complement in seen:
            return (seen[Complement], i)
        seen[num] = i

print(Two_Sum([2, 7, 11], 9))  

