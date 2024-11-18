def cribaDeEratostenes(n):
    # Crear una lista de booleanos, inicializada como True
    primos = [True] * (n + 1)
    p = 2  # El primer número primo
    
    while p * p <= n:
        # Si primos[p] es True, entonces es un primo
        if primos[p]:
            # Marcar todos los múltiplos de p como no primos
            for i in range(p * p, n + 1, p):
                primos[i] = False
        p += 1
    
    # Recopilar los números primos en una lista
    numeros_primos = [p for p in range(2, n + 1) if primos[p]]
    
    return numeros_primos

# Ejemplo de uso
n = 30
print("Números primos hasta", n, ":", cribaDeEratostenes(n))



