def collatz_sequence(n):
    sequence = []
    
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    
    sequence.append(1)
    
    return sequence

n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    result = collatz_sequence(n)
    print(f"Starting number: {n}")
    print(f"Collatz sequence: {result}")
