def is_palindrome(text):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    text = text.replace(" ", "").lower()
    
    # Compare the original text with its reverse
    return text == text[::-1]

def main():
    text = input("Enter a word or phrase to check for palindrome: ")
    
    if is_palindrome(text):
        print(f"'{text}' is a palindrome!")
    else:
        print(f"'{text}' is not a palindrome.")

if __name__ == "__main__":
    main()