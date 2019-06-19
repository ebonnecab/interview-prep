'''Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length. '''

def remove_duplicate(nums):
    i = 0

    if len(nums) == 0:
        return 0
        
    while i < len(nums)-1:
        if nums[i] != nums[i+1]:
            i+=1
        elif nums[i] == nums[i+1]:
            del nums[i]
    return len(nums)

if __name__ == "__main__":
    numbers = [1,2,2,4,5]
    test = remove_duplicate(numbers)

    print(test)