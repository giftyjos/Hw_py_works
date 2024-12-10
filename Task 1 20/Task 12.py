def is_ugly_number(n):
    if n <= 0:
        return False
    
    for prime in [2, 3, 5]:
        while n % prime == 0:
            n //= prime
    
    return n == 1


n = 6
print(f"Is {n} an ugly number", is_ugly_number(n))

