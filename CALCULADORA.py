#calculadora de Aprovação Escolar

nome = input("Digite o nome do estudante: ")

soma_notas =  0
quantidade_trimestres = 3
meta_Aprovacao = 180

#coleta as notas dos três periodos 
for i in range(1, quantidade_trimestres + 1):
    nota = float(input("Informe a nota{i}º periodo: "))
    soma_notas +=nota

print("-" * 30)
print(f"Escudante: {nome}")
print(f"Pontuação Total: {soma_notas}")

#Verificar o Status de aprovação
if soma_notas >= meta_Aprovacao:
    print("Status: APROVADO!!!")
else:
    pontos_faltantes = meta_Aprovacao = soma_notas
    print("Status: VAI ESTUDAR SAFADO")
    print(f"faltam : {pontos_faltantes}, para atingir o mínimo de {meta_Aprovacao}." )




