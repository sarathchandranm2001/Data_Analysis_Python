def factorial_with_storage(n):
    if n < 0:
        return None  
    
    factorial_dict = {}
    
    def factorial(num):
        if num in factorial_dict:
            return factorial_dict[num]
        elif num == 0 or num == 1:
            factorial_dict[num] = 1
            return 1
        else:
            result = num * factorial(num - 1)
            factorial_dict[num] = result
            return result
    
    result = factorial(n)
    
    print(f"The factorial of {n} is: {result}")
    
    print("Factorials stored in dictionary:")
    for num, fact in factorial_dict.items():
        print(f"{num}! = {fact}")
    
    return result

number = int(input("Enter a number to calculate its factorial: "))
factorial_result = factorial_with_storage(number)
