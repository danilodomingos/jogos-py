import random

def jogar():

    imprime_msg_abertura()
    
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = informa_chute()
        

        if(chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1

        enforcou = (erros == len(palavra_secreta))
        acertou = ("_" not in letras_acertadas)
        print(letras_acertadas)
    
    imprime_msg_status(acertou)



def imprime_msg_status(acertou):
    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")

def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra

        index += 1

def informa_chute():
    chute = input("Qual a letra: ")
    return chute.strip().upper()

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def imprime_msg_abertura():
    print("**********************************")
    print("Bem vindo ao jogo da Forca!")
    print("**********************************")

def carrega_palavra_secreta():
    palavras = []
    arquivo = open("palavras.txt", "r")
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    
    return palavra_secreta


if (__name__ == "__main__"):
    jogar()