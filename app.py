import mod
import pygame
def main():
    pygame.init() # Inicializa os módulos do pygame

    TAMANHO_TELA = (800, 800)
    tela = pygame.display.set_mode(TAMANHO_TELA)
    pygame.display.set_caption("Brick Breaker Youtube") # Nome que irá aparecer na parte superior da tela 

    tamanho_bola = 15
    bola = pygame.Rect(100, 500, tamanho_bola, tamanho_bola) # Criação da bola
    tamanho_jogador = 100
    jogador = pygame.Rect(0, 750, tamanho_jogador, 15) # Criação do jogador
    cores = {
    "purple": (186, 113, 162),
    "rose": (236, 208, 236),
    "coffee": (70, 29, 58),
    "dark": (126, 42, 83),
    "violet": (80, 42, 80)
    }

    fim_jogo = False
    pontuacao = 0
    movimento_bola = [7, -7] # Qtd de pixels que a bola irá movimentar

    qtde_blocos_linha = 8
    qtde_linhas_blocos = 5
    qtde_total_blocos = qtde_blocos_linha * qtde_linhas_blocos
    blocos = mod.criar_blocos(qtde_blocos_linha, qtde_linhas_blocos,TAMANHO_TELA) 
    while not fim_jogo:
        mod.desenhar_inicio_jogo(tela,cores,jogador,bola)
        mod.desenhar_blocos(blocos,tela,cores)
        fim_jogo = mod.atualizar_pontuacao(qtde_total_blocos - len(blocos),cores,tela,qtde_total_blocos)
        for evento in pygame.event.get(): # Verifica se algum botão foi pressionado durante o jogo
            if evento.type == pygame.QUIT: # Caso o jogador feche a janela, o jogo será encerrado
                fim_jogo = True

        # Chama as funções criadas para movimentar o jogador e a bola
        mod.movimentar_jogador(evento,jogador,tamanho_jogador,TAMANHO_TELA)
        movimento_bola = mod.movimentar_bola(bola,movimento_bola,tamanho_bola,TAMANHO_TELA,jogador,blocos)

        if not movimento_bola:
            fim_jogo = True
        pygame.time.wait(20) # Pausa o jogo por 20 milissegundos por loop (para não sobrecarregar o processador)
        pygame.display.flip() # "Atualiza" a tela do jogador para mostrar as alterações, como um bloco destruido

    pygame.quit() # Encerra o pygame

if __name__ =='__main__':
    main()