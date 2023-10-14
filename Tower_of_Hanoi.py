def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)

def main():
    try:
        num_discs = int(input("Enter the number of discs: "))
        if num_discs < 1:
            print("Number of discs must be a positive integer.")
        else:
            tower_of_hanoi(num_discs, 'A', 'B', 'C')
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
