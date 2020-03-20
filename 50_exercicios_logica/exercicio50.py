prova1= [80,90,91]
prova2= [98,89,53]
alunos= ['maria', 'pedro', 'joao']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip (alunos,prova1,prova2)}
print(final)
