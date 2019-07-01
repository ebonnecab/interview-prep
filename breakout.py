'''
Breakout Problem:
Given a list of n numbers, determine if it contains any duplicate numbers.
'''
test = [5, 6, 8, 9, 4, 4]
test2 = [5,3,4]

def find_pairs(lst):
    lst = lst.sort()
    for i in range(len(lst)-1):
        if lst[i] == list[i+1]:
            return True
    return False

if __name__ == "__main__":
    find_pairs()