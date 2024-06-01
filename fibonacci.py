def fibonacci_sequence(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

# Example usage
n = int(input())
print(" ".join(map(str, fibonacci_sequence(n))))