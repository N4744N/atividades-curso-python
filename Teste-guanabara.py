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

'''s = float(input('Quanto o funcionario ganha? '))
if s <= 1250:
    print(f'O funcionario que ganha R${s:.2f} ira ganhar R${(s / 100) * 15 + s:.2f}')
else:
    print(f'O funcionario que ganha R${s:.2f} ira ganhar R${(s / 100) * 10 + s:.2f}')'''

# exercicio 35
'''Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem ou
não formar um triângulo.'''

'''r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima formam um triâgulo.')
else:
    print('As retas acima não formam um triângulo.')'''

## Aula 11
'''Como trabalhar com cores no terminal
exemplos:'''

# print('\033[1;31;43mOla, mundo!\033[m')# colocar "\033[m" para abrir e para fechar
'''formatações de estilo: 0 (normal); 1 (negrito); 4 (sublinhado); 7 (inverte texto e fundo).
formatações da cor do texto: 30 (branco); 31 (vermelho); 32 (verde); 33 (amarelo); 34 (azul); 35 (roxo); 36 (ciano) 37 (cinza).
formatações da cor do fundo: 40 (branco); 41 (vermelho); 42 (verde); 33 (amarelo); 44 (azul); 45 (roxo); 46 (ciano) 47 (cinza).'''

## Aula 12
# exemplos:

'''nome = str(input('Qual é o seu nome? ')).strip()
if nome.upper() == 'NATHAN':
    print('Que nome bonito!')
elif nome.upper() == 'PEDRO' or nome.upper() == 'MARIA' or nome.upper() == 'PAULO':
    print('Seu nome não é tão bonito mas é bem popular no Brasil!')
else:
    print('Seu nome é bem normal...')
print(f'Tenha um bom dia, {nome.capitalize()}!')'''

# exercicio 36
'''Escreva um programa para aprovar o empréstimo bancario para a compra
de uma casa. O programa vai perguntar o valor da casa, o salário do comprador
e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do 
salário ou então o empréstimo será negado.'''

'''casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você quer pagar? ')) * 12

prestacao = casa / anos

if prestacao <= ((salario / 100) * 30):
    print(f'Seu emprestimo foi aprovado, parabéns! O valor da parcela ficou em R${prestacao:.2f} por mês.')
else:
    print('Infelizmente o seu empréstimo não foi aprovado.')'''

# exercicio 37

'''Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal'''

'''num = int(input('Digite um número: '))
print('Para converter o número para binaro digite 1.')
print('Para converter para octal, digite 2.')
print('Para converter para hexadecimal, digite 3.')
n = int(input('Digite a opção desejada: '))

binario = bin(num)[2:]
octal = oct(num)[2:]
hexadecimal = hex(num)[2:]

if num < 0:
    print('Um número positivo por favor!')
elif n == 1:
    print(f'{num} em binario é: {binario}')
elif n == 2:
    print(f'{num} em octal é: {octal}')
elif n == 3:
    print(f'{num} em hexadecimal é: {hexadecimal}')'''

# exercicio 38
'''Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

'''n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

if n1 == n2:
    print('Não existe valor maior, os dois são iguais')
elif n1 > n2:
    print('O primeiro valor é maior')
else:
    print('O segundo valor é maior')'''

# exercicio 39
'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora de se alistar ou se ja passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

'''anos = int(input('Quantos anos você tem? '))
if anos < 18:
    print(f'Ainda faltam {18 - anos} anos para você se alistar!')
    exit()
while True:
    alistou = str(input('Você ja se alistou para o exercito? ')).strip().upper()
    if alistou in ['SIM', 'NÃO', 'NAO']:
        break
    else:
        print('Resposta inválida! Por favor, responda apenas com sim ou não. ') 
if anos >= 18 and alistou == 'SIM':
    print('Parabens, você esta em dia com suas obrigações de cidadão!')
elif anos == 18 and alistou == 'NÃO' or 'NAO':
    print('Você precisa se alistar esse ano!')
elif anos > 18 and alistou == 'NÃO' or 'NAO':
    print(f'Você ainda precisa se alistar, você esta atrasado {anos - 18} anos!')'''

# exercicio 40
'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final,  de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

'''while True:
    try:
        n1 = float(input('Digite a primeira nota: '))
        n2 = float(input('Digite a segunda nota: '))
        break
    except ValueError:
        print('Digite apenas números!')

media = (n1 + n2) / 2

if media < 5:
    print('Reprovado.')
elif media < 7:
    print('Recuperação.')
else:
    print('Aprovado.')'''

# exercicio 41
'''A confederação Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER'''

'''from datetime import date
while True:
    try:
        ano = int(input('Qual o ano de nascimento do atleta? '))
        break
    except ValueError:
        print('Digite apenas números!')

idade = date.today().year - ano
print(f'O atleta tem {idade} anos de idade.')
if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print(f'Portanto se encaixa na categoria: {categoria}')'''

# exercicio 42
'''Refaça o exercicio 35 dos triângulos, acrescentando o recurso
de mostrar que tipo de triângulo será formado:
- Equilatero: todos os lados iguais
- Isóceles: dois lados iguais
- Escaleno: todos os lados diferentes'''

'''r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima formam um triâgulo.')

    if r1 == r2 == r3:
        triangulo = 'Equilatero'
    elif r1 == r2 or r1 == r3 or r2 == r3:
        triangulo = 'Isóceles'
    else:
        triangulo = 'Escaleno'

    print(f'As retas formam um Triângulo {triangulo}.')
else:
    print('As retas acima não formam um triângulo.')'''

# exercicio 43
'''Desenvolva uma lógica que leia o peso e a altura
de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida'''

'''while True:
    try:
        peso = float(input('Qual o peso em Kg? '))
        altura = float(input('Qual a altura em metros? '))
        break
    except ValueError:
        print('Digite apenas números!')

imc = peso / (altura ** 2)

if imc < 18.5:
    status = 'Abaixo do Peso'
elif imc < 25:
    status = 'Peso ideal'
elif imc < 30:
    status = 'Sobrepeso'
elif imc < 40:
    status = 'Obesidade'
else:
    status = 'Obesidade mórbida'
print(f'Seu IMC é de: {imc:.2f}')
print(f'Portanto seu status é de: {status}')'''

# exercicio 44
'''Elabore um programa que calcule o valor a ser pago por
um produto, considerando o seu preço normal e condição de pagamento:
- á vista dinheiro/cheque: 10% de desconto.
- á vista no cartão: 5% de desconto.
- em até 2x no cartão: preço normal.
- 3x ou mais no cartão: 20% de juros.'''

'''valor = float(input('Qual o valor a ser pago? R$'))
while True:
    print('\nEscolha a forma de pagamento:')
    print('[ 1 ] À vista dinheiro/cheque (10% de desconto)')
    print('[ 2 ] À vista no cartão (5% de desconto)')
    print('[ 3 ] Em até 2x no cartão (Preço normal)')
    print('[ 4 ] 3x ou mais no cartão (20% de juros)')
    
    opcao = int(input('Sua opção: '))

    if opcao == 1:
        total = valor - (valor * 0.10)
        print(f'Você consegue 10% de desconto. De R${valor:.2f} vai para R${total:.2f}!')
        break
        
    elif opcao == 2:
        total = valor - (valor * 0.05)
        print(f'Você consegue 5% de desconto. De R${valor:.2f} vai para R${total:.2f}!')
        break
        
    elif opcao == 3:
        total = valor
        parcela = total / 2
        print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.')
        print(f'Sua compra vai custar R${total:.2f}.')
        break
        
    elif opcao == 4:
        total = valor + (valor * 0.20)
        totparc = int(input('Quantas parcelas? '))
        parcela = total / totparc
        print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS.')
        print(f'Sua compra de R${valor:.2f} vai custar R${total:.2f} no final.')
        break
        
    else:
        print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')'''

# exercicio 45
'''Crie um programa que faça o computador jogar JOKEMPÔ com você.'''

'''import random
def jogar_jokenpo():
    opcoes = ['pedra', 'papel', 'tesoura']

    while True:
        print('***JOKEMPO***')
        print('Suas opções: Pedra, Papel ou Tesoura.')
        
        escolha_usuario = input('Sua jogada: ').strip().lower()

        if escolha_usuario in opcoes:
            break
 
        print('\nOpção inválida! Escolha entre Pedra, Papel ou Tesoura.')

    escolha_pc = random.choice(opcoes)
    print(f'Computador escolheu: {escolha_pc}')

    if escolha_usuario == escolha_pc:
        print('Empate!')
    elif (escolha_usuario == "pedra" and escolha_pc == "tesoura") or (escolha_usuario == "papel" and escolha_pc == "pedra") or (escolha_usuario == "tesoura" and escolha_pc == "papel"):
        print("\n🎉 VOCÊ VENCEU!")
    else:
        print('Computador venceu!')

jogar_jokenpo()'''

# exercicio 46
'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

'''from time import sleep
for c in range (10, 0, -1):
    print(c)
    sleep (1)
print('BUMMM POWWW CATAPUMMMMMM')'''

# exercicio 47
'''Crie um programa que mostre na tela todos os números pares
que estão no intervalo entre 1 e 50.'''

'''for c in range (1, 51):
    if c %2 == 0:
        print(c)'''

# exercicio 48
'''Faça um programa que calcule a soma entre todos os números 
ímpares que são multiplos de três e que se encontram no intervalo de 1 até 500.'''

'''soma = 0
numero = int(input('Digite um número que o programa irá somar todos os números que são divisiveis por 3: '))
for c in range (1, numero+1):
    if c %3 == 0:
        soma = soma + c
print(f'A soma dos números solicitados é igual a: {soma}')'''

# ecercicio 49
'''Refaça o DESAFIO 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for'''

'''n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
for c in range (1, 11):
    print(f'{n} X {c} = {n*c}')
print('-' * 12)'''

# exercicio 50
'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
que forem PARES. Se o valor digitado for ímpar, desconsidere-o.'''

'''soma = 0
for n in range(1, 7):
    numero = int(input('Digite um número: '))

    if numero %2 == 0:
        soma = soma + numero
print(soma)'''

# exercicio 51
'''Desenvolva um programa que leia o primeiro termo e a razão
de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

'''termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo2 = termo1 + (11 - 1) * razao

for n in range (termo1, termo2, razao):
    print(f'{n}', end=(', '))

print('Fim')'''

# exercicio 52
'''Faça um programa que leia um número inteiro e diga se ele
é ou não um número primo.'''

'''num = int(input('Digite um número: '))
tot = 0
for c in range (1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')

print(f'\n\033[mO número {num}, foi divisivel {tot} vezes.')
if tot == 2:
    print('Portanto é um número primo!')
else:
    print('Portanto não é um número primo!')'''

# exercicio 53
'''Crie um programa que leia uma frase qualquer e diga se ela é um palindromo,
desconsiderando os espaços'''

'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
print(junto, inverso)
if junto == inverso:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')'''

# exercicio 54
'''Crie um programa que leia o ano de cascimento de 7 pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas ja são de maiores.'''

'''from datetime import date
hoje = date.today().year
maior = 0
menor = 0
for n in range(1, 8):
    ano = int(input(f'Em que ano a {n}ª pessoa nasceu? '))
    idade = hoje - ano
    if idade >= 18:
        maior = maior + 1
    else: menor = menor + 1
print(f'Na lista temos {maior} pessoas maior de idade e {menor} pessoas menores de idade!')
'''

# exercicio 55
'''Faça um programa que leia o peso de 5 pessoas.
No final, mostre qual foi o maior e o menor peso lidos.'''

'''maior = 0
menor = 0
for n in range(1, 6):
    peso = float(input(f'Qual o peso da {n}ª pessoa? '))
    if n == 1:
        maior = peso
        menor = peso
    else: 
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi de {maior}Kg!')
print(f'O menor peso foi de {menor}Kg!')'''

# exercicio 56
'''Desenvolva um programa que leia o nome, idade e sexo
de 4 pessoas. No final do programa, mostre:
A média de idade do grupo;
Quantas mulheres tem menos de 20 anos.
Qual é o nome do homem mais velho.'''

'''media = 0
mulheres = 0
maior_idade = 0
nome_velho = ''
for p in range(1, 5):
    print('-' * 25)
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()
    print('-' * 25)
    if sexo == 'F':
        if idade < 20:
            mulheres = mulheres + 1
    media = media + idade

    if sexo == 'M':
        if idade > maior_idade:
            maior_idade = idade
            nome_velho = nome
media = media / 4

print(f'A média de idade do grupo é de {media} anos de idade!')
print(f'Existem {mulheres} mulheres menores de 20 anos na lista!')
print(f'O homem mais velho se chama {nome_velho}!')'''

# exercicio 57
'''Faça um programa que leia o sexo de uma
pessoa, mas só aceite os valores M ou F.
Caso esteja errado, peça a digitação novamente até ter um valor correto'''

'''sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Inválido. Responda com M ou F: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso!')'''

# exercicio 58
'''Melhore o jogo do desafio 28 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.'''

'''from random import randint
num = randint(0, 10)
vezes = 1

print('_' * 20)
print('Pensei em um número de 0 a 10, tente adivinhar...')
print('_' * 20)
p = int(input('Em que número eu pensei? '))
while p != num:
    if p < num:
        print('Errou, tente um número maior!')
    if p > num:
        print('Errou, tente um número menor!')
    p = int(input('tente novamente: '))
    vezes += 1
    
if p == num:
    print('Você acertou, parabens!')
    print(f'você precisou de {vezes} tentativas para acertar')'''

# exercicio 59
'''Crie um programa que leia dois valores
e mostre um menu como o abaixo na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação
solicitada em cada caso.'''

num = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

while True:
    opcao = int(input('''
Digite a opção desejada:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Opção: '''))

    if opcao == 1:
        print(f'A soma de {num} e {num2} é igual a: {num + num2}')

    elif opcao == 2:
        print(f'A multiplicação de {num} e {num2} é igual a: {num * num2}')

    elif opcao == 3:
        if num > num2:
            print(f'{num} é o maior valor')
        elif num2 > num:
            print(f'{num2} é o maior valor')
        else:
            print('Os dois valores são iguais')

    elif opcao == 4:
        print('Informe os novos números:')
        num = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))

    elif opcao == 5:
        print('Finalizando...')
        break

    else:
        print('Opção inválida. Tente novamente.')

    print('-=' * 20)
