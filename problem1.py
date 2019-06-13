'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.'''


def twoSum(nums, target):
        
    dict = {}
        
    for i, j in enumerate(nums):
        num = target -j
            
        if num in dict:
            return [dict[num], i]
        else:
            dict[j] = i
    return None
            

if __name__ == "__main__":
    test = twoSum([2,5,7,10], 12)
    print(test)
