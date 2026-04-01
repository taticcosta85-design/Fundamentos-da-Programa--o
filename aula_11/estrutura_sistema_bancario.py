# Variáveis do Sistema Bancário

idade = int(input("Informe a idade"))
salario = float(input("Informe o salário"))
tempo_de_trabalho = float(input("Informe o tempo de trabalho"))

#print(f" A idade do cliente é {idade}, o salário do cliente é {salario} e o tempo de trabalho é {tempo_de_trabalho}.")

if idade <18:
    print ("Você é menor de idade")

elif salario >=5000:
    print ("Empréstimo aprovado")

elif idade >=18 and salario >=2000 and tempo_de_trabalho >=2:
    print ("Empréstimo aprovado")

else: 
    print ("Empréstimo negado.")
