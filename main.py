from funcoes import generating_score,choice_difficulty

try:
    choice: int = choice_difficulty()
    
    if choice != None:
        generating_score(choice)
    else:
        print('Não existe essa opção!')
    
except ValueError:
    print('Opção inválida!')