nome = input('Qual é o seu nome? ')
altura = float(input('Qual é a sua altura? '))
peso = float(input('Qual é o seu peso? '))
altura2 = altura * altura 
imc = peso/altura2
print('{} tem {} de altura,\n pesa {} quilos e seu IMC é: \n {}'. format(nome, altura, peso, imc))