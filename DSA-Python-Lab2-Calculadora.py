# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
operacao = input('Descreva a operação desejada: soma, subtração, multiplicação ou divisão.')

if operacao == 'soma':
    resultado = valor1 + valor2
    print('O resultado da soma é de ',resultado)
elif operacao == 'subtração':
    resultado = valor1 - valor2
    print('O resultado da subtração é de ',resultado)
elif operacao == 'multiplicação':
    resultado = valor1 * valor2
    print('O resultado da multiplicação é de ',resultado)
elif operacao == 'divisão':
    if valor2 != 0:
        resultado = valor1 / valor2
        print('O resultado da divisão é de ',resultado)
    else: 
        print('Divisão por 0 não é permitido.')
else:
    print('Operação inválida')
