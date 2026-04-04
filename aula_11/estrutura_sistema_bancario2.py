# Variáveis do Sistema Bancário

idade = int(input("Informe a idade"))
salario = float(input("Informe o salário"))
tempo_de_trabalho = float(input("Informe o tempo de trabalho"))

print(f" A idade do cliente é {idade}, o salário do cliente é {salario} e o tempo de trabalho é {tempo_de_trabalho}.")

#⚠️ Prioridade 1: Se a idade for menor que 18 anos, o empréstimo é negado automaticamente.
if idade < 18:
    print("Empréstimo negado. O cliente é menor de idade.")

#⚠️ Prioridade 2: Se o salário for maior ou igual a 5.000, o empréstimo é aprovado automaticamente.
elif salario >= 5000: 
    print("Empréstimo aprovado!")

#⚠️ Prioridade 3: Se o salário for maior ou igual a 2.000 e menor que 5.000 e o tempo de trabalho for maior ou igual 2 anos, o empréstimo é aprovado.
elif 2.000 <= salario < 5.000 and tempo_de_trabalho >= 2:
    print("Empréstimo aprovado!")

# Para todos os outros casos, o empréstimo é negado.
else:
    print("Empréstimo negado.")




