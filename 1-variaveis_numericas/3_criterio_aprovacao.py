# Um aluno de computação fez as avaliações do semestre. 
# O regulamento da faculdade diz que a Prova Teórica tem relevância de valor 3, enquanto o Projeto Prático de Código tem relevância de valor 7. 
# Descubra a nota final do aluno com base nas regras da instituição.

# Dados do sistema
nota_prova_teorica = 6.0
importancia_prova = 3

nota_projeto_pratico = 9.0
importancia_projeto = 7

# Seu código abaixo:
nota_peso_1 = (nota_prova_teorica * importancia_prova)
nota_peso_2 = (nota_projeto_pratico * importancia_projeto)
nota_maxima = (importancia_projeto + importancia_prova)
nota_final = (nota_peso_1 + nota_peso_2) / nota_maxima
print(nota_final)