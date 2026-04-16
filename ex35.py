def numeral(n):
    if n % 2 == 0:
        return f"O número {n} é par."
    else:
        return f"O número {n} é ímpar."
x = int(input("Digite um número: "))
print(numeral(x))