
# ====================== Avaliação de Programação 1 2024.2 =========================

# Jogo: Adivinhe o Número Secreto

import random
from time import sleep
import threading

# Função para gerar o número secreto
def gerar_numero_secreto():
    digito_um = [str(i) for i in range (1, 10) if i != 6] #garente que o primeiro número não será 0 ou 6
    digitos = [str(i) for i in range(0, 10) if i != 6] #restante do número podendo ter 0, excluindo o 6
    while True:
        primeiro = random.choice(digito_um) #escolhe o primeiro numero
        restantes = random.sample(digitos, 2) #escolhe os 2 ultimos numeros
        numero_secreto = primeiro + ''.join(restantes) #junta para o numero secreto
        if len(set(numero_secreto)) == 3:
            return numero_secreto

# Função para verificar o palpite do jogador
def verificar_palpite(palpite, numero_secreto):
    resultado = []
    for i in range(3):
        if palpite[i] == numero_secreto[i]:
            resultado.append('🟢')  # Algarismo correto e na posição correta
        elif palpite[i] in numero_secreto:
            resultado.append('🟡')  # Algarismo correto, mas na posição errada
    return resultado

# Função principal do jogo
def jogar():
    numero_secreto = gerar_numero_secreto()
    tentativas = 5
    print("Bem-vindo ao jogo! Tente adivinhar o número secreto que está entre 100 e 999 (sem o dígito 6)."); sleep(1)
    print("Você tem 5 tentativas. Após cada palpite, serão exibidas bolinhas verdes ou amarelas como dicas."); sleep(1)
    print("🟢 = número certo na posição certa | 🟡 = número certo na posição errada"); sleep(1)
    print("Mas Atenção! A ordem das bolinhas não corresponde à posição exata do número."); sleep(1)
    
    for tentativa in range(1, tentativas + 1):
        palpite = input(f"Tentativa {tentativa}: ")
        if len(palpite) != 3 or not palpite.isdigit() or '6' in palpite or len(set(palpite)) != 3 or palpite[0] == '0':
            print("Analisando..."); sleep(1)
            if palpite[0] == '0':
                print("Palpite inválido! O número não pode começar com 0.")
            else:
                print("Palpite inválido! Insira um número de 3 dígitos, sem repetição de algarismos e sem o número 6.")
            continue
        
        if palpite == numero_secreto:
            print("Analisando..."); sleep(1)
            print(f"Parabéns! Você adivinhou o número secreto {numero_secreto} na tentativa {tentativa}.")
            break
        
        resultado = verificar_palpite(palpite, numero_secreto)
        if resultado:
            print("Analisando..."); sleep(1)
            print("Não é bem esse número ainda... 🫢")
            print("Dica:", ' '.join(resultado))
        else:
            print("Analisando..."); sleep(1)
            print("Algo de errado não está certo... 🤔"); sleep(1)
            print("Nenhum número está correto.")
    
    else:
        print(f"Você perdeu! O número secreto era {numero_secreto}.")

#Função para reiniciar o jogo
def reiniciar_jogo():
    print("\nTempo esgostado! Reiniciando o jogo...\n")
    iniciar_jogo()

def iniciar_jogo():
    while True:
        jogar()
        timeout_thread = threading.Timer(10.0, reiniciar_jogo)
        timeout_thread.start()

        continuar = input("Deseja jogar novamente? (s/n): ")

        if continuar.lower() != 'S'.lower():
            print("Obrigado por jogar! Até a próxima.")
            break

# Rodar o jogo
iniciar_jogo()