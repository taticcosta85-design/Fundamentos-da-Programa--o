#Uso do while

while True:


if nome and idade and convite== "sair":
    print("Você está saindo.")    
    break


# Variáveis

nome = input("Digite seu nome:")
idade = int(input("Informe sua idade: "))
convite = input("Possui convite ? [S/N] ")
                

print(f"{nome}, com {idade} anos, {convite}possui entrada para o evento ")

# Regra 1: Entrada negada para menores de 16 anos. 

if idade <16:
    print ("Entrada negada.") 

# Regra 2: Entrada permitida para pessoas com maiores de 16 anos que possuem convite.

elif idade >=16 and convite == "Sim":
    print ("Entrada permitida")


#Regra 3: qualquer outra situação    

else: 
    print ("Entrada negada")



