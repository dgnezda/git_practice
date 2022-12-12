def fizzbuzz(n):
    return ", ".join('Fizz'*(x % 3 == 0) + 'Buzz'*(x % 5 == 0) or \
            str(x) for x in range(1, n))

print(fizzbuzz(37))

def fizzbuzz2(n):
    return ['Fizz'*(x % 3 == 0) + 'Buzz'*(x % 5 == 0) or \
            str(x) for x in range(1, n)]
    
print(fizzbuzz2(37))
