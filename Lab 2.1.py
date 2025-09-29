def prime(n):
    primes = []
    num = 2

    while len(primes) < n:
        is_prime = True
        for p in primes:
            if p*p > num:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num+=1

    return primes[-1]
valid = False
while valid == False:
    n = int(input("Введите номер простого числа: "))
    if n >= 1:
        valid = True
    else:
        print("Введите целое число большее нуля!")
print("Простое число:", prime(n))