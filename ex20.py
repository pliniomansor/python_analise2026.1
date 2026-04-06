sal = float(input("Digite o salário do contribuinte= "))
if sal <= 5000 :
    imposto = 0
elif sal <= 8000 :
    imposto = sal * 0.075
else:
    imposto = sal * 0.27
salfinal = sal - imposto    
print(f"Salário {sal}, imposto - {imposto} , Salário Bruto {salfinal}")