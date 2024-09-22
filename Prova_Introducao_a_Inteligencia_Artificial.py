# Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas.

# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0. Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.

# Ao final, exiba a média geral da turma.

numero_alunos =  int(input("Digite o número de alunos: "))

soma_turma = 0

for i in range(numero_alunos):
        nome = input(f"\nDigite o nome do aluno {i +1}: ")

        nota1 = float (input(f"Digite a primeira nota do aluno(a) {nome}: "))

        nota2 = float (input(f"Digite a segunda nota do aluno(a) {nome}: "))

        nota3 = float (input(f"Digite a terceira nota do aluno(a) {nome}: "))


        media_aluno = (nota1 + nota2 + nota3)/3

        soma_turma += media_aluno

        if media_aluno >= 7.0:
                status = "Aprovado"
        else:
                status = "Reprovado"
    
        print(f"\nAluno: {nome}")
        print(f"Notas: {nota1}, {nota2}, {nota3}")
        print(f"Média: {media_aluno:.2f}")
        print(f"Status: {status}")


        media_turma = soma_turma / numero_alunos
        print(f"\nMédia geral da turma: {media_turma:.2f}")


