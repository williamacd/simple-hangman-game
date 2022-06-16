import os


def imprimepalpitepalavra():
    for i in range(len(advinhaletras)):
        print(advinhaletras[i], end=" ")


def validapalpite(letra):
    y = 0
    if len(palpiteletras) == 0:
        palpiteletras.append(letra)
        return True
    else:
        for w in palpiteletras:
            if palpiteletras[y] == letra:
                return False
            y += 1
            if y == len(palpiteletras):
                palpiteletras.append(letra)
                return True



def imprimepalpitesdados():
    for i in range(len(palpiteletras)):
        print(palpiteletras[i], end=" ")


os.system('cls')
print("BEM-VINDO AO JOGO DA FORCA")
print("PRESSIONE: \n1 - JOGAR\n2 - SAIR\nCONFIRME USANDO ENTER\n")

opcao = input()
opcao = int(opcao)

while opcao != 2:
    if opcao == 1:
        os.system("cls")
        print("INFORME A PALAVRA A SER ADVINHADA: ")
        palavra = input()
        listaletras = []
        advinhaletras = []
        palpiteletras = []
        posicao = 0
        tentativas = 6
        acertou = False

        for x in palavra:
            listaletras.append(x)
            advinhaletras.append(" _ ")
        while (tentativas > 0):
            os.system('cls')
            print("ADVINHE A PALAVRA, ELA POSSUI " + str(len(listaletras)) + " LETRAS:")
            posicao = 0
            imprimepalpitepalavra()
            if len(palpiteletras) > 0:
                print("\nSEUS PALPITES UTILIZADOS: ")
                imprimepalpitesdados()
            print("\nVOCE POSSUI " + str(tentativas) + " TENTATIVAS\n")
            print("INFORME UMA LETRA: ")
            palpite = input()
            if validapalpite(palpite):
                for x in listaletras:
                    if palpite == listaletras[posicao]:
                        advinhaletras[posicao] = palpite
                        acertou = True
                    posicao += 1
                if not acertou:
                    tentativas -= 1
                acertou = False
                if listaletras == advinhaletras:
                    break
            else:
                print("\nSEU PALPITE " + palpite + " JA FOI UTILIZADO, PRESSIONE ENTER PARA CONTINUAR")
                input()

        if listaletras == advinhaletras:
            os.system('cls')
            print("VOCE VENCEU, A PALAVRA INFORMADA FOI: " + palavra)
            print("AINDA RESTAVAM " + str(tentativas) + " TENTATIVAS")
        if tentativas <= 0:
            os.system('cls')
            print("VOCE PERDEU, A PALAVRA INFORMADA FOI: " + palavra + "\n")
            print("SEUS ACERTOS FORAM: ")
            imprimepalpitepalavra()
            print("\nSEUS PALPITES UTILIZADOS: ")
            imprimepalpitesdados()

        print("\nPRESSIONE: \n1 - JOGAR\n2 - SAIR\nCONFIRME USANDO ENTER\n")
        opcao = input()
        opcao = int(opcao)

    else:
        print("OPCAO INVALIDA, TENTE NOVAMENTE")
        print("PRESSIONE: \n1 - JOGAR\n2 - SAIR\nCONFIRME USANDO ENTER\n")
        opcao = input()
        opcao = int(opcao)

print("SAINDO...")
exit(0)
