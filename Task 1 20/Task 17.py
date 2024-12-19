def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def smallest_prime_palindrome(n):
    while True:
        if is_palindrome(n) and is_prime(n):
            return n
        n += 1


n = 13
print(f"The smallest prime palindrome greater than or equal to {n} is:", smallest_prime_palindrome(n))

