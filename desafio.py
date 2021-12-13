from itertools import permutations
from bs4 import BeautifulSoup
import requests


ICOR = '\033[m'
RED = '\033[31m'
YEL = '\033[33m'


def dicionario_aberto(word):
    """ Usa método de mineração para absorver API do dicionário aberto
     e verificar se a palavra existe no dicionário português! """

    url = 'https://api.dicionario-aberto.net/word/' + word

    headers = {
        'User-Agente': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    if len(soup) > 1:
        return print('A palavra {}{} existe{} no dicionário português e é palíndroma'.format(YEL, word, ICOR))
    else:
        return print('A sequência {}{} não existe{} no dicionário português'.format(YEL, word, ICOR))

    
def teste_palindromo(palavra):
    """Retorna True se a palavra é palíndroma,
        retorna False se a palavra e seu inverso não
         coincidem
         """
    if str(palavra) == str(palavra)[::-1]:
        return True
    else:
        print(f'{str(palavra)} é diferente de {str(palavra)[::-1]}')
        return False

    
def allPermutations(palavra):
    """ Cria todas as permutações de letras e rearranja as sequências e
     verifica se é palíndroma """

    lista_sequencias, lista_palindromos = [], []
    permList = list(permutations(palavra))
    total = len(permList)
    print('{}Pesquisando o total de {} combinações!{}'.format(RED, total, ICOR))
    resp = input(f"Atenção, combinações grandes podem travar seu computador, \ndeseja continuar (s / n)? ")
    if 'S' in str(resp).upper():
        for perm in permList:
            if perm == perm[::-1]:
                seq = ''.join(perm)
                if seq in lista_sequencias:
                    if not seq in lista_palindromos:
                        lista_palindromos.append(seq)
                lista_sequencias.append(seq)
        if len(lista_palindromos) > 0:
            print(f'a palavra {palavra} forma as sequências palíndromas {lista_palindromos}')
            for word in lista_palindromos:
                dicionario_aberto(word)
        else:
            print(f'Não foi possível encontrar nenhum palídromo relacionado a palavra {palavra}.')
    else:
        print('Ok, não vamos continuar!')


if __name__ == "__main__":
    desafio = input('Gostaria de testar o qual desafio da Sling Hub? ({}1{}/{}2{}): '.format(RED, ICOR, YEL, ICOR))
    try:
        if int(desafio) == 1:
            palavra = input('Qual palavra gostaria de verificar se é palíndroma? ')
            print(teste_palindromo(palavra))
        elif int(desafio) == 2:
            palavra = input('Qual palavra gostaria de verificar se é palíndroma? ')
            allPermutations(palavra)
    except:
        print('Ocorreu algum erro, tente novamente!')
