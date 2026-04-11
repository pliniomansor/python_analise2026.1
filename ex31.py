for i in range(0,5):
    id = float(input("Digite a idade= "))
    if id > 65:
        print(f"Idoso")
    elif id < 18:
        print(f"Menor de idade")
    else:
        print(f"Maior de idade")