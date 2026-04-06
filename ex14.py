name=input("Insira seu nome: ")
ano=float(input("Insira o ano do seu nascimento: "))
idade=2026-ano
if idade <18:
    print(f"Deculpe! Você é menor de idade, por isso impossibilitamos o seu acesso.")
else:
    print(f"Seja bem-vindo! Nosso sistema está totalmente disponível. Boa navegação!")
