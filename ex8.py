pre=float(input("Digite aqui o valor total: "))
desc=float(input("Digite qual porcentagem lhe atende: "))
res = pre - (pre * desc / 100)
print(f"Seu desconto é de: {res}")