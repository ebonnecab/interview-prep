'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.'''


def twoSum(nums, target):
    i = 0
    j = len(nums)-1
        
    while i < j:
        if nums[i] + nums[j] == target:
            return(i, j)
        elif nums[i] + nums[j] < target:
            i+=1
        else:
            j-=1
    return None

if __name__ == "__main__":
    test = twoSum([2,5,7,10], 12)
    print(test)
