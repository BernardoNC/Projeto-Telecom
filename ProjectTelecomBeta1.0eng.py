option = 0
misses = 0
hits = 0
programming_done = False
programming = ''
while option == 0:
    if programming_done:
        programming = '(done)'
    print('-=' * 80)
    option = str(input(f'[ 1 ] for programming {programming}'
                       f'\n[ exit ] to exit the program'
                       f'\n hits: {hits}, misses: {misses}'
                       f'\n -- '))
    if option == '1' and programming_done is False:
        print('-=' * 80, '\nyou chose programming'
                         '\nthere is a secret inside this program, find it (hint: look at the code of the program)')
        answer = str(input('Answer: ')).lower()
        if answer == 'binary':
            print('congratulations, you hit it')
            option = 0
            hits += 1
            programming_done = True
        else:
            print('you missed it, try again')
            option = 0
            misses += 1
    elif option == '1':
        print('challenge already done')
        option = 0
    if option == 'exit':
        print('goodbye')
        option = 1

# 01100010 01101001 01101110 01100001 01110010 01111001
