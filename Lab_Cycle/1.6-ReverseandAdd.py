def reverse_digits(number):
    str_number = str(number)
    reversed_number = int(str_number[::-1])
    return reversed_number

def is_palindrome(number):
    str_number = str(number)
    return str_number == str_number[::-1]

def reverse_and_add_until_palindrome(number):
    original_number = number
    while True:
        reversed_number = reverse_digits(original_number)
        sum_result = original_number + reversed_number
        
        if is_palindrome(sum_result):
            return sum_result, reversed_number
        
        original_number = sum_result

number = int(input("Enter a number: "))
palindrome_sum, reversed_number = reverse_and_add_until_palindrome(number)

print(f"The palindrome sum is: {palindrome_sum}")
print(f"The reversed number added is: {reversed_number}")
