print("\n******************* Python Calculator *******************")

print('''Selecione o número da operação desejada \n
1 - Soma 
2 - Subtração 
3 - Multiplicação 
4 - Divisão \n''')

numOper = str(input('Digite sua opção (1/2/3/4): '))

if numOper == '1':
    n1 = int(input('\nDigite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    soma = n1 + n2
    print('\nO resultado da soma é:', soma)

elif numOper == '2':
    n1 = int(input('\nDigite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    sub = n1 - n2
    print('\nO resultado da subtração é:', sub)

elif numOper == '3':
    n1 = int(input('\nDigite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    mul = n1 * n2
    print('\nO resultado da multiplicação é:', mul)
        
elif numOper == '4':
    n1 = int(input('\nDigite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    div = n1 / n2
    print('\nO resultado da divisão é:', div)
else:
    print('\nEste resultado não é valido, digite um número entre 1 e 4')
