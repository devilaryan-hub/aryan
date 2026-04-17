def check_prime(number):
    if number <= 1:
        print(f"{number} is not a prime number.")
        return

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            return

    print(f"{number} is a prime number.")

check_prime(29)
check_prime(8)

for num in range(1, 101):
    check_prime(num)
