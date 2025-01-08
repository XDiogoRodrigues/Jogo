import random

def choice_difficulty() -> int:
    choice: int = int(input('Informe a dificuldade:\n1- Fácil\n2- Normal\n3- Díficil:\nEscolha: '))

    if choice == 1:
        return 1
    elif choice == 2:
        return 2
    elif choice == 3:
        return 3
   

def gerator_expression(option: int) -> tuple:
    operation: list = ['+', '-']
    signal_choice: int = random.randint(0, len(operation) - 1)
    print(signal_choice)
    operation_choice: str = operation[signal_choice]
    match option:
        case 1:
            number_1: int = random.randint(0, 100)
            number_2: int = random.randint(0, 100)
            result: int = number_1 + number_2
            return f'Qual e a soma entre {number_1} + {number_2}?', result
        case 2:
            number_1: int = random.randint(0, 500)
            number_2: int = random.randint(0, 500)
            number_3: int = random.randint(0, 500)
      
            if operation_choice == '+':
                result: int = number_1 + number_2 + number_3
                return f'Qual é a soma da seguinte adição: {number_1} {operation_choice} {number_2} {operation_choice} {number_3} ?', result
            elif operation_choice == '-':
                number_2 = random.randint(0,450)
                result: int = number_1 - number_2 
                return f'Qual é o valor da seguinte subtração: {number_1} {operation_choice} {number_2} ?', result
           
        case 3:
            number_1: int = random.randint(500, 1000)
            number_2: int = random.randint(500, 1000)
            number_3: int = random.randint(500, 1000)

            operation: list = ['+', '-', 'x']
            signal_choice: int = random.randint(0, len(operation) - 1)
            operation_choice: str = operation[signal_choice]
            
            if operation_choice == '+':
                result: int = number_1 + number_2 + number_3
                return f'Qual é a soma da seguinte adição: {number_1} {operation_choice} {number_2} {operation_choice} {number_3} ?', result, option
            elif operation_choice == '-':
                number_2 = random.randint(1, 499)
                result: int = number_1 - number_2 
                return f'Qual é o valor da seguinte subtração: {number_1} {operation_choice} {number_2} ?', result, option
            elif operation_choice == 'x':
                number_1: int = random.randint(1,150)
                number_2: int = random.randint(1,150)
                result: int = number_1 * number_2
                return f'Qual é o valor da seguinte multiplicação: {number_1} {operation_choice} {number_2} ?', result, option


def generating_score(choice: int) -> str:
   quantity: int = 1
   score: int = 0
   acertou: bool = True
   while acertou == True and score < 10:
        result: list = gerator_expression(choice)
        print(f'Pergunta {quantity}/10')
        print(result[0])
        value: int = int(input('Valor: '))
        print('\n')
        if value == result[1]:
            score += 1
            quantity += 1
            acertou = True
        else:
            acertou = False
   print(f'Você acertou {score} perguntas.')