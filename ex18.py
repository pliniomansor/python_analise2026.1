vl=float(input("Digite o valor da compra que te digo o desconto: "))
cl1 = vl - (vl * (20/100))
cl2 = vl - (vl * (15/100))
cl3 = vl - (vl * (5/100))
if vl > 500 :
    print(cl1)
elif vl > 100 and vl < 499 :
    print(cl2)
else:
    print(cl3)