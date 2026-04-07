# Variáveis do Sistema Bancário

idade = int(input("Informe a idade"))
salario = int(input("Informe o salário"))
tempo = int(input("Informe o tempo de trabalho"))

print(f"O cliente tem {idade} anos, salário de R${salario} e {tempo} anos de trabalho.")

# Regra Especial 1: Negação automática para menores de 18 anos.
if idade <18:
    print ("Emprestimo negado.")

#Regra Especial 2: Aprovação automática para salários maiores ou iguais a 5.000.
elif salario >= 5000:
    print ("Empréstimo aprovado.")

#Critério de aprovação do empréstimo: 
elif idade >=18 and salario >= 2000 and tempo >= 2:
    print ("Todas as condições básicas foram antendidas, portanto, o empréstimo é aprovado.")

#Qualquer outro caso que não atenda as regras anteriores, o empréstimo é negado.
else:
    print ("Empréstimo negado.")
    