#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = [0,1]

    if length <= 0:
        print([])
        return

    while len(fib_sequence) < length:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    print(fib_sequence[:length])
    
print_fibonacci(0)
        