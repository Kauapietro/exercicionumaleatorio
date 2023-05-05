import random

num = int(input("Digite um número entre 1 e 10: "))
soma = 0

while True:
    aleatorio = random.randint(1, 10)
    soma += aleatorio
    print(f"Número gerado: {aleatorio}")
    
    if aleatorio == num:
        break

print(f"A soma dos números gerados é {soma}.")
