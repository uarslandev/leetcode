def PrintPrimeNumbers():
    for i in range(2, 101):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime=False
                break
        print(i)
PrintPrimeNumbers()
