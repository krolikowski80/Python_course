def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("To jet liczba pierwsza")
    else:
        print("To nie jest liczba pierwsza")


n = int(input("Pofaj jakąś liczbę: "))

prime_checker(n)
