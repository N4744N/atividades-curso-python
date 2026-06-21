# Exercicios do curso de pyhton
# exercicio 1
'''Crie um programa que escreva "Ola, mundo!" na tela.'''

'''print('Ola, mundo!')'''

# exercicio 2
'''Faça um programa que leia o nome de uma pessoa e mostre uma
mensagem de boas vindas.'''

'''nome = input('Qual o seu nome? ')
print(f'Seja bem vindo {nome}!')'''

# exercicio 3
'''Crie um programa que leia dois números e mostre a some entre eles.'''

'''n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))
print(f'A soma de {n1} com {n2} é igual a: {n1 + n2}')'''

# exercicio 4
'''Faça um programa que leia algo pelo teclado e mostre na tela o seu
tipo primitivo e todas informações possiveis sobre ela.'''

'''a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabetico? ', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('Esta em maisculas? ', a.isupper())
print('Esta em minusculas? ', a.islower())
print('Esta capitalizada? ', a.istitle())'''

# exercicio 5
'''Faça um programa que leia um número inteiro e mostre na tela o seu
sucessor e o seu antecessor.'''

'''n = int(input('Digite um número inteiro: '))
print(f'O antecessor de {n} é {n-1} e o sucessor é {n+1}.')'''

# exercicio 6
'''Crie um algoritimo que leia um  número e mostre o seu dobro, triplo e
raiz quadrada.'''

'''n = int(input('Digite um número inteiro: '))
print(f'O dobro de {n} é: {n*2}, o triplo é {n*3} e a raiz quadrada é {n**(1/2):.2f}.')'''

# exercicio 7
'''Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre a sua média.'''

'''n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A média entre {n1:.1f} e {n2:.1f} é igual a: {m:.1f}.')'''

# exercicio 8
'''Escreva um programa que leia um valor em metros e o exiba
convertido em centimetros e milimetros'''

'''m = float(input('Digite uma distancia em metros: '))
cm = m * 100
mm = m * 1000
print(f'A medida de {m}m corresponde a {cm:.0f}cm e {mm:.0f}mm.')'''

# exercicio 9
'''Faça um programa que leia um número inteiro qualquer e mostre na
tela a sua tabuada.'''

'''n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
print(f'{n} X 1 = {n*1}')
print(f'{n} X 2 = {n*2}')
print(f'{n} X 3 = {n*3}')
print(f'{n} X 4 = {n*4}')
print(f'{n} X 5 = {n*5}')
print(f'{n} X 6 = {n*6}')
print(f'{n} X 7 = {n*7}')
print(f'{n} X 8 = {n*8}')
print(f'{n} X 9 = {n*9}')
print(f'{n} X 10 = {n*10}')
print('-' * 12)'''

# exercicio 10
'''Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira e mostre quantos Dolares ela pode comprar.
Considere US$1,00 = R$5,14'''

'''real = float(input('Quanto você tem? R$'))
dolar = real / 5.14
print(f'Com R${real:.2f} voce pode comprar US${dolar:.2f}.')'''

# exercicio 11
'''Faça um programa que leia a largura e a altura de uma parede em
metros, calcule a sua area e a quantidade de tinta necessaria para
pinta-la. Sabendo que cada litro de tinta pinta uma area de 2m²'''

'''larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.1f}l de tinta.')'''

# exercicio 12
'''Faça um algoritimo que leia o preço de um produto e mostre seu
novo preço, com 5% de desconto.'''

'''p = float(input('Quanto custa o produto? '))
desc = p - (p / 100 * 5)
print(f'O seu produto que custa R${p:.2f} com 5% de desconto passara a custar R${desc:.2f}')'''

# exercicio 13
'''Faça um algoritimo que leia o salário de um funcionário e mostre seu
novo salario, com 15% de aumento.'''

'''salario = float(input('Quanto o colaborador recebe? R$'))
aum = salario + (salario / 100 * 15)
print(f'O colaborador que recebe R${salario:.2f} passara a receber R${aum:.2f} após o aumento de 15%.')'''

# exercicio 14
'''Escreva um programa que converta uma temperatura
digitada em °C e converta para °F'''

'''c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5) + 32
print(f'A temperatura de {c}°C corresponde a {f}F°.')'''

# exercicio 15
'''Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
custa R$60,00 por dia e R$0,15 por Km rodado'''

'''dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R${pago:.2f}')'''

# exercicio 16
'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porçao inteira.
Ex.: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.'''

'''from math import trunc
n = float(input('Digite um valor: '))
print(f'O valor digitado foi {n} e sua parte inteira é {trunc(n)}.')'''

# exercicio 17
'''Faça um programa que leia o comprimento do
cateto oposto e do cateto adjacente de um
triângulo retângulo, calcule e mostre o comprimento da hipotenusa.'''

'''from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(co, ca):.2f}')'''

# exercicio 18
'''Faça um programa que leia um ângulo qualquer e
mostre na tela o valor do seno, cosseno e tangente
desse ângulo.'''

'''from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
coss = cos(radians(an))
tang = tan(radians(an))
print(f'O ângulo de {an} tem o SENO de {seno:.2f}')
print(f'O ângulo de {an} tem o COSSENO de {coss:.2f}')
print(f'O ângulo de {an} te a TANGENTE de {tang:.2f}')'''

# exercicio 19
'''Um professor quer sortear um dos seus quatro alunos para apagar
o quadro. Faça um programa que ajude ele, lendo o nome deles e
escrevendo o nome escolhido.'''

'''from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]

print(f'O aluno escolhido foi {choice(lista)}')'''

# exercicio 20
'''O mesmo professor do desafio anterior quer sortear a ordem de
apresentação de trabalhos dos alunos. Faça um programa que leia 
o nome dos quatro alunos e mostre a ordem selecionada.'''

'''from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentação sera {lista}')'''