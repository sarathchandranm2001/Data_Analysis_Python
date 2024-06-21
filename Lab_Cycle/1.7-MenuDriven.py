def check_substring():
    string1 = input("Enter the main string: ")
    string2 = input("Enter the substring to check: ")
    
    if string2 in string1:
        print(f"'{string2}' is a substring of '{string1}'")
    else:
        print(f"'{string2}' is not a substring of '{string1}'")

def count_occurrences():
    string = input("Enter the string: ")
    char = input("Enter the character to count: ")
    
    count = string.count(char)
    print(f"Occurrences of '{char}' in '{string}': {count}")

def replace_substring():
    string = input("Enter the main string: ")
    old_substring = input("Enter the substring to replace: ")
    new_substring = input("Enter the new substring: ")
    
    new_string = string.replace(old_substring, new_substring)
    print(f"Modified string: {new_string}")

def convert_to_capital():
    string = input("Enter the string to convert to capital letters: ")
    capitalized_string = string.upper()
    print(f"String in capital letters: {capitalized_string}")

def main():
    while True:
        print("\nOperations on Strings:")
        print("1. Check if the String is a Substring of Another String")
        print("2. Count Occurrences of Character")
        print("3. Replace a substring with another substring")
        print("4. Convert to Capital Letters")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            check_substring()
        elif choice == '2':
            count_occurrences()
        elif choice == '3':
            replace_substring()
        elif choice == '4':
            convert_to_capital()
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
