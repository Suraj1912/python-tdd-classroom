def reverse_list(input_list):
    """
    Reverses order of elements in list input_list.
    """
    return input_list[::-1]

def count_digits(number):
    """
    Return count of digits
    """
    number = abs(number)
    count = 0
    while number > 0:
        count += 1
        number = number // 10
    
    return count