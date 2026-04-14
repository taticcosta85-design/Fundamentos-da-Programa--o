#Variáveis do Sistema de Matrícula

idade = int(input("Informe a idade: "))
nota = float(input("Informe a nota: "))
frequencia = int(input("Informe a frequência: "))

# A matrícula será aprovada se a idade for >= 18, a nota for >= 6 e a frequencia for > 75%.

print(f"Idade: {idade}, Nota: {nota}, Frequência: {frequencia}%")

#Estruturas condicionais: 

if idade <18: 
    print("Matrícula não aprovada: Idade inferior a 18 anos.")

elif nota >=9:
    print(" Matricula aprovada automaticamente!")

elif idade >=18 and nota >=6 and frequencia >=75:
    print(" Matrícula aprovada!")
else:
    print(" Matrícula não aprovada.")       