def prime(n):
    if n<=1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def print_prime_numbers (start, end):
    for num in range (start, end+1):
        if prime(num):
            print(num,end=" ")

print_prime_numbers(1,100)