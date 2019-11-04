def isprime(x):
    if x > 2:
        for i in range(2, int(x/2 +1)):
            if (x % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

for i in range(100):
    print(i, isprime(i))
