# 🧮 Calculadora Simples em Python

## 🎯 Objetivo
Criar uma calculadora interativa utilizando estruturas de repetição, condicionais e operações matemáticas.

## 💻 Código

```python
while True:
    print('\n--- Calculadora ---')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('0 - Sair')
    print('=' * 25)

    opcao = input('Escolha uma opção: ')

    if opcao == '0':
        print('Até logo!')
        break

    if opcao not in ('1', '2', '3', '4'):
        print('Opção inválida!')
        continue

    num1 = float(input('Digite o 1º número: '))
    num2 = float(input('Digite o 2º número: '))

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
                print('Erro: não é possível dividir por zero.')
```

## 📚 Conceitos praticados

- 🔁 `while True`: mantém a calculadora em execução.
- ⌨️ `input()`: recebe informações do usuário.
- 🔢 `float()`: converte valores para números decimais.
- 🔀 `if` e `else`: verificam condições.
- 🎯 `match-case`: seleciona a operação matemática.
- 🛑 `break`: encerra o laço de repetição.
- ⏭️ `continue`: retorna ao início do laço.
- 🔍 `not in`: verifica se uma opção não pertence às opções válidas.

## ✅ Funcionalidades

- ➕ Adição
- ➖ Subtração
- ✖️ Multiplicação
- ➗ Divisão
- 🚫 Proteção contra divisão por zero
- 🔄 Repetição até o usuário escolher sair

## 📝 Observação
Este exercício reúne diferentes fundamentos da linguagem Python em um único programa interativo.
