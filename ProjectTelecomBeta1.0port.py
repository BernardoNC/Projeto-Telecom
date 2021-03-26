option = 0
misses = 0
hits = 0
programming_done = False
programming = ''
while option == 0:
    if programming_done:
        programming = '(feito)'
    print('-=' * 80)
    option = str(input(f'[ 1 ] para programação {programming}'
                       f'\n[ sair ] para sair do programa'
                       f'\n acertos: {hits}, erros: {misses}'
                       f'\n -- '))
    if option == '1' and programming_done is False:
        print('-=' * 80, '\nvocê escolheu: programação'
                         '\ndentro deste programa existe um segredo, procure-o (dica: olhe o codigo do programa)')
        r = str(input('Resposta: ')).lower()
        if r == 'binário':
            print('acertou')
            option = 0
            hits += 1
            programming_done = True
        else:
            print('errou')
            option = 0
            misses += 1
    elif option == '1':
        print('desafio ja feito')
        option = 0
    if option == 'sair':
        print('adeus')
        option = 1

# 01000010 01101001 01101110 11100001 01110010 01101001 01101111
