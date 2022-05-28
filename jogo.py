p1='1'
p2='2'
p3='3'
p4='4'
p5='5'
p6='6'
p7='7'
p8='8'
p9='9'

def atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8, p9):

        tabuleiro = f'''

                        |     |     
                     {p1}  |  {p2}  |  {p3}  
                   _____|_____|_____
                        |     |     
                     {p4}  |  {p5}  |  {p6}  
                   _____|_____|_____
                        |     |     
                     {p7}  |  {p8}  |  {p9}  
                        |     | 

        '''

        print(tabuleiro)

def verificaGanhador():
    if p1 == 'X' and p2 == 'X' and p3 == 'X':
        print('X é o vencedor!')
        return  True
    elif p4 == 'X' and p5 == 'X' and p6 == 'X':
        print('X é o vencedor!')
        return  True
    elif p7 == 'X' and p8 == 'X' and p9 == 'X':
        print('X é o vencedor!')
        return  True
    elif p1 == 'X' and p4 == 'X' and p7 == 'X':
        print('X é o vencedor!')
        return  True
    elif p2 == 'X' and p5 == 'X' and p8 == 'X':
        print('X é o vencedor!')
        return  True
    elif p3 == 'X' and p6 == 'X' and p9 == 'X':
        print('X é o vencedor!')
        return  True
    elif p1 == 'X' and p5 == 'X' and p9 == 'X':
        print('X é o vencedor!')
        return  True
    elif p3 == 'X' and p5 == 'X' and p7 == 'X':
        print('X é o vencedor!')
        return  True

    elif p1 == 'O' and p2 == 'O' and p3 == 'O':
        print('O é o vencedor!')
        return  True
    elif p4 == 'O' and p5 == 'O' and p6 == 'O':
        print('O é o vencedor!')
        return  True
    elif p7 == 'O' and p8 == 'O' and p9 == 'O':
        print('O é o vencedor!')
        return  True
    elif p1 == 'O' and p4 == 'O' and p7 == 'O':
        print('O é o vencedor!')
        return  True
    elif p2 == 'O' and p5 == 'O' and p8 == 'O':
        print('O é o vencedor!')
        return  True
    elif p3 == 'O' and p6 == 'O' and p9 == 'O':
        print('O é o vencedor!')
        return  True
    elif p1 == 'O' and p5 == 'O' and p9 == 'O':
        print('O é o vencedor!')
        return  True
    elif p3 == 'O' and p5 == 'O' and p7 == 'O':
        print('X é o vencedor!')
        return  True

def verificaEmpate():
    if p1 != '1'and p2 != '2' and p3 != '3' and p4 != '4' and p5 != '5' and p6 != 6 and p7 != '7' and p8 != '8' and p9 != '9':
        print('Deu empate!')
        return True

tabuleiro_inicial = f'''

                        |     |     
                     1  |  2  |  3  
                   _____|_____|_____
                        |     |     
                     4  |  5  |  6  
                   _____|_____|_____
                        |     |     
                     7  |  8  |  9  
                        |     | 

        '''

print(tabuleiro_inicial)

lista_equacoes = ['2x = 4', '4x = 16', '6x = 36', '7x = 49', '4 = b - 5', 'y - 2 = -12', 'x + 1 = 15', 'z - 3 = -9', '3 + 2x = 6 - x', '7 + 2y = 10 - y', 'x - 2 = 4 - x']
lista_equacoes_respostas = [2, 4, 6, 7, 9, -10, 14, -6, 1, 1, 3]

vez_x_jogar = True
cont = 0

while True:

    if verificaGanhador():
        break

    if verificaEmpate():
        break

    if vez_x_jogar == True:
        posicao_escolhida = int(input('Jogador X, onde você deseja jogar: '))

        if posicao_escolhida < 1 or posicao_escolhida > 9:
            print('Digite uma opção válida!')
            print('')
        else:
            resposta = int(input(f'Qual o resultado de {lista_equacoes[cont]}: '))

            if lista_equacoes_respostas[cont] == resposta:
                if posicao_escolhida == 1 and p1 == '1':
                    p1 = 'X'
                    atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8,p9)
                elif posicao_escolhida == 2 and p2 == '2':
                    p2 = 'X'
                    atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8,p9)
                elif posicao_escolhida == 3 and p3 == '3':
                    p3 = 'X'
                    atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8,p9)
                elif posicao_escolhida == 4 and p4 == '4':
                    p4 = 'X'
                    atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8,p9)
                elif posicao_escolhida == 5 and p5 == '5':
                    p5 = 'X'
                    atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8,p9)
                elif posicao_escolhida == 6 and p6 == '6':
                    p6 = 'X'
                    atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8,p9)
                elif posicao_escolhida == 7 and p7 == '7':
                    p7 = 'X'
                    atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8,p9)
                elif posicao_escolhida == 8 and p8 == '8':
                    p8 = 'X'
                    atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8,p9)
                elif posicao_escolhida == 9 and p9 == '9':
                    p9 = 'X'
                    atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8,p9)
                else :
                    print('Esta posição já foi escolhida, escolha outra!')

                vez_x_jogar = False
                cont += 1
            else:
                print('Resposta errada, O é a sua vez!')
                vez_x_jogar = False
    else:
        posicao_escolhida = int(input('Jogador O, onde você deseja jogar: '))

        if posicao_escolhida < 1 or posicao_escolhida > 9:
            print('Digite uma opção válida!')
            print('')
        else:
            resposta = int(input(f'Qual o resultado de {lista_equacoes[cont]}: '))

            if lista_equacoes_respostas[cont] == resposta:
                if posicao_escolhida == 1 and p1 == '1':
                    p1 = 'O'
                    atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8,p9)
                elif posicao_escolhida == 2 and p2 == '2':
                    p2 = 'O'
                    atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8,p9)
                elif posicao_escolhida == 3 and p3 == '3':
                    p3 = 'O'
                    atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8,p9)
                elif posicao_escolhida == 4 and p4 == '4':
                    p4 = 'O'
                    atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8,p9)
                elif posicao_escolhida == 5 and p5 == '5':
                    p5 = 'O'
                    atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8,p9)
                elif posicao_escolhida == 6 and p6 == '6':
                    p6 = 'O'
                    atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8,p9)
                elif posicao_escolhida == 7 and p7 == '7':
                    p7 = 'O'
                    atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8,p9)
                elif posicao_escolhida == 8 and p8 == '8':
                    p8 = 'O'
                    atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8,p9)
                elif posicao_escolhida == 9 and p9 == '9':
                    p9 = 'O'
                    atualizaTAbuleiro(p1, p2, p3, p4, p5, p6, p7, p8,p9)
                else :
                    print('Esta posição já foi escolhida, escolha outra!')

                vez_x_jogar = True
                cont += 1
            else:
                print('Resposta errada, X é a sua chance!')
                vez_x_jogar = True