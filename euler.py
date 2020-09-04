
def e_cuadratica(n):
    e_aprox = 0 
    for i in range (n):
        e_aprox = e_aprox + (1 / factorial_iterativo(i))
    return e_aprox

def factorial_iterativo(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial

def factorial_recursivo(n):
    factorial = 1
    return factorial_recursivo_aux(factorial, n)

def factorial_recursivo_aux(factorial, n):
    if n == 0:
        return factorial
        
    else:

        factorial = factorial * n

        return factorial_recursivo_aux(factorial, n - 1)

def e_lineal(n):
    e_aprox = 0 

    factorial = 1

    e_aprox = e_aprox + (1 / 1)

    for i in range (1, n + 1):

        factorial = factorial * i
    
        e_aprox = e_aprox + (1 / (factorial))

    return e_aprox

print(e_cuadratica(50))

print(e_lineal(50))
