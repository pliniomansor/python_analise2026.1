name=input("Digite o nome do aluno: ")
turma=input("Digite a turma do aluno: ")
b1=float(input("Primeiro bimestre -> "))
b2=float(input("Segundo bimestre -> "))
b3=float(input("Terceiro bimestre -> "))
med = (b1 + b2 + b3) / 3
print(f"O aluno {name} do {turma} tirou no primeiro bismestre {b1}, no segundo {b2} e no terceiro {b3}. O aluno está: ")
if med >= 6:
    print("APROVADO")
else:
    print("RECUPERAÇÃO")