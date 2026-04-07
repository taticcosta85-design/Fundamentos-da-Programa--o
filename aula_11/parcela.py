#Variáveis

valor_empréstimo = float(input("Informe o quanto deseja solicitar ao banco."))
valor_da_parcela = float(input("Informe o valor da parcela."))
salario = float(input("Informe o valor do salário."))

#Se o valor do salário for menor que 30% do valor da parcela, o empréstimo é negado. Caso contrário, o empréstimo é aprovado.
if valor_da_parcela  > salario * 0.3:
    print ("Empréstimo negado")

else:
    print ("Empréstimo aprovado")





