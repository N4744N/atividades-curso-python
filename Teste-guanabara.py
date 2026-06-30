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

# exercicio 22
'''Crie um programa que leia o nome completo de uma pessoa e
mostre:
O nome com todas as letras maiúsculas e minusculas.
Quantas letras ao todo o nome tem (sem considerar espaços).
Quantas letras tem o primeiro nome.'''

'''nome = str(input('Digite o seu nome completo: ')).strip()
print(f'Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minuscúlas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras')'''

# exercicio 23
'''Faça um rpograma que leia um número de 0 a 9999 e mostre na tela
cada um dos seus digitos serparados.
ex.:
Digite um número: 1234
unidade: 4  dezena: 3  centena: 2  milhar: 1'''

'''n = int(input('Digite um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Analisando o número {n}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')'''

# exercicio 24
'''Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com o nome 'SANTO' '''

'''c = str(input('Em que cidade você nasceu? ')).strip()
print(c[:5].upper() == 'SANTO')'''

# exercicio 25
'''Crie um programa que leia o nome de uma pessoa e diga se ela tem
"SILVA" no nome.'''

'''nome = str(input('Qual é o seu nome completo? ')).strip()
print(f'Seu nome tem Silva? {'SILVA' in nome.upper()}')'''

# exercicio 26
'''Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "a".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez.'''

'''frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra A aparece {frase.count('A')} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.find('A')+1}')
print(f'A ultima letra A apareceu na posição {frase.rfind('A')+1}')'''

# exercicio 27
'''Faça um programa que leia o nome completo de uma pessoa,
mostrando um seguida o primeiro e o último nome separadamente.
Ex.: Ana Maria de Souza
Primeiro: Ana
Último: Souza'''

'''nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print(f'Satisfação em te conhecer {nome}!')
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[-1]}')'''

#AULA 10 EXEMPLOS:
'''nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'Nathan':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal...')
print(f'Bom dia, {nome}!')'''

'''n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m}')
if m >= 6.0:
    print('A sua média foi boa, você passou de ano PARABÉNS!!!')
else:
    print('A sua média foi ruim, infelizmente você reprovou, ESTUDE MAIS ANO QUE VEM!!!')'''

# exercicio 28
'''Escreva um programa que faça o computador ''pensar'' em um número
inteiro entre 0 e 5 e peça para o usuário descobrir qual foi o número
escolhido pelo computador. O programa deverá escrever na tela se o 
usuário venceu ou perdeu.'''

'''from random import randint
num = randint(0, 5)
print('_' * 20)
print('Pensei em um número de 0 a 5, tente adivinhar...')
print('_' * 20)
p = int(input('Em que número eu pensei? '))
if p == num:
    print('Como você fez isso??? ACERTOU!')
    print('Ninguem nunca conseguiu, estranho...')
else:
    print('HAHAHAHA, VOCÊ É MAIS UM QUE ERROU!!!')'''

# exercicio 29
'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem
dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

'''velocidade = int(input('Qual a velocidade do carro? '))
multa = (velocidade-80) * 7
if velocidade > 80:
    print(f'Você estava acima de 80Km/h por isso vai receber uma multa de R${multa:.2f}!')
else:
    print('Você esta dentro do limite de velocidade, continue assim!')'''

# exercicio 30
'''Crie um programa que leia um número inteiro
e mostre na tela se ele é PAR ou ÍMPAR.'''

'''num = int(input('Digite um número inteiro: '))
r = num % 2
if r == 0:
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é impar.')'''

# exercicio 31
'''Desenvolva um programa que pergunte a distância de uma viagem
em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
viagens de até 200Km e R$0,45 para viagens mais longas.'''

'''km = float(input('Quantos Km serão percorridos? '))
preço1 = 0.50 * km
preço2 = 0.45 * km
if km <= 200:
    print(f'Para {km}km, sera cobrado R${preço1:.2f} sem a promoção.')
else:
    print(f'Para {km}km, sera cobrado R${preço2:.2f} com o valor promocional. ')'''

# exercicio 32
'''Faça um programa que leia um ano qualquer
e mostre se ele é bissexto.'''

'''from datetime import date
ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')'''

# exercicio 33
'''Faça um programa que leia 3 números e
mostre qual é o maior e o menor.'''

'''n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O maior é {maior}')
print(f'O menor é {menor}')'''

# exercicio 34
'''Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%'''

s = float(input('Quanto o funcionario ganha? '))
if s <= 1250:
    print(f'O funcionario que ganha R${s:.2f} ira ganhar R${(s / 100) * 15 + s:.2f}')
else:
    print(f'O funcionario que ganha R${s:.2f} ira ganhar R${(s / 100) * 10 + s:.2f}')