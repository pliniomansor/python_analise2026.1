temp=float(input("Digite aqui a temperatura de hoje: "))
if temp >=1 and temp <=18 :
    print(f"Estando {temp} consideramos que hoje está frio")
elif temp >=19 and temp <=24 :
    print(f"Estando {temp} consideramos que hoje está normal")
else:
    print(f"Estando {temp} consideramos que hoje está calor")