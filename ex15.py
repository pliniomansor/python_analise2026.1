name=input("Digite seu nome: ")
an=int(input("Digite o ano do seu nascimento: "))
idade=2026-an
gen=input("Digite M (maiúsculo) ser for homem ou F (maiúsculo) se for mulher: ")
if idade >=18 and gen == "M":
    print(f"Busque o melhor endereço para seu alistamento em: https://www.exercitobrasileiro.gov.br.")
else:
    print(f"Você não está apto ao alistamento.")