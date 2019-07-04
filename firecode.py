def find_missing_number(list_numbers):
    correct_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    correct_sum = sum(correct_list)
    list_sum = sum(list_numbers)
    
    if list_sum != correct_sum:
        missing_val = correct_sum - list_sum
    
    return missing_val

def reverse_string(a_string):
    str = ""
    
    for char in a_string:
        str = char + str
    
    return str

def is_palindrome(input_string):
    first = 0
    last = len(input_string) -1
    
    while last > first:
        if input_string[last] != input_string[first]:
            return False
        first += 1
        last -= 1
        
    return True