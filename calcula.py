while True:
    print('\n--- Calculadora ---')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print("4 - Dividir")
    print('0 Sair')
    print('=' *25)

    opcao = input('Escolha uma opção: ')
    num1 = float(input('Digite o 1° número: '))
    num2 = float(input('Digite o 2° número: '))

    if opcao == '0':
         print('Até logo')
    match opcao:
        case '1':
            print(f'Resultado: {num1 + num2}')
        case '2':
                print(f'Resultado: {num1 - num2}')
        case '3':
                  print(f'Resultado: {num1 * num2}')
        case '4':
            if num2 != 0: 
                print(f'Resultado: {num1 / num2}')
            else:
                print("Erro por não pode existir divisão por zero")
        case '0':
            print('Ate, logo!')
            break
        case _:
              print('Opção inválida')