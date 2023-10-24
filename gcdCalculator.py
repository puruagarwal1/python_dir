def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    try:
        num1 = int(input("Enter the first positive integer: "))
        num2 = int(input("Enter the second positive integer: "))
        if num1 <= 0 or num2 <= 0:
            print("Please enter positive integers.")
        else:
            result = gcd(num1, num2)
            print(f"The greatest common divisor of {num1} and {num2} is {result}.")
    except ValueError:
        print("Invalid input. Please enter positive integers.")

if __name__ == "__main__":
    main()