print(f'--- Bem vindo ao Sistema de Cadastro de alunos ---')

# Lista principal para a turma 
turma = []

# Variável que guarda a quantidade de alunos que serão cadastrados (Coleta de dados):

quantidade = int(input(" Digite a quantidade de alunos que você deseja cadastrar: "))
                                                        
# Estrutura de repetição para repetir o cadastro para cada aluno: 
                                    
for i in range(quantidade):
    print(f"Cadastrar aluno {i+1}")         


   
    nota1 = float(input("Digite a primeira nota: [0 a 10] "))                            
    nota2 = float(input("Digite a segunda nota: [0 a 10] "))
    nota3 = float(input("Digite a terceira nota: [0 a 10] "))   
                                                                                           

                               