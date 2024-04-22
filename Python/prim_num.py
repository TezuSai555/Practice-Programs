def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

number = int(input("Enter a number: "))
has_prime_digit = False

while number > 0:
    digit = number % 10
    if is_prime(digit):
        has_prime_digit = True
        break
    number //= 10

if has_prime_digit:
    print(digit)
else:
    print("The number does not contain any prime digit.")
