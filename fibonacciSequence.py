def main():
    number = int(input("Enter the length of the Fibonacci Sequence: "))
    sequence = fibonacci_sequence(number)
    return sequence


def fibonacci_sequence(number):
    sequence = [0,1]
    for i in range(number-2):
        sequence.append(sequence[i] + sequence[i + 1])
    return sequence

if __name__ == "__main__":
    print(main())