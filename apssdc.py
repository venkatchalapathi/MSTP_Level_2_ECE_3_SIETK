def isPrime(n):
    count = 1
    for i in range(1,n):
        if n%i == 0:
            count = count+1
    if count == 2:
        return True
    else:
        return False
    