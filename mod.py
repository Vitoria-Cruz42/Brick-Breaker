import pygame

# A função A cria blocos que serão quebrados pela bolinha
def criar_blocos(qtde_blocos_linha, qtde_linhas_blocos,TAMANHO_TELA):
    # Configurações para o tamanho do display
    ALTURA_TELA = TAMANHO_TELA[1]
    LARGURA_TELA = TAMANHO_TELA[0]
    # Configurações para o tamanho dos blocos
    DISTANCIA_ENTRE_BLOCOS = 5
    LARGURA_BLOCO = LARGURA_TELA / 8 - DISTANCIA_ENTRE_BLOCOS
    ALTURA_BLOCO = 15
    DISTANCIA_ENTRE_LINHAS = ALTURA_BLOCO + 10

    #Criação da lista de blocos
    blocos = []

    for j in range(qtde_linhas_blocos): # Geração de um loop para criar os blocos
        for i in range(qtde_blocos_linha):
            bloco = pygame.Rect(i * (LARGURA_BLOCO + DISTANCIA_ENTRE_BLOCOS), j * DISTANCIA_ENTRE_LINHAS, LARGURA_BLOCO, ALTURA_BLOCO)
            blocos.append(bloco)
    return blocos

# A função B adiciona cores ao jogo
def desenhar_inicio_jogo(tela,cores,jogador,bola):
    tela.fill(cores["rose"]) # Cor do fundo 
    pygame.draw.rect(tela, cores["dark"], jogador) # Cor da plataforma que o jogador controla
    pygame.draw.rect(tela, cores["purple"], bola) # Cor da bola

# A função C adiciona cores aos blocos
def desenhar_blocos(blocos,tela,cores):
    for bloco in blocos:
        pygame.draw.rect(tela, cores["violet"], bloco)

# A função D é responsável pela movimentação da plataforma para a direita e esquerda 
def movimentar_jogador(evento,jogador,tamanho_jogador,TAMANHO_TELA):
    if evento.type == pygame.KEYDOWN: # O evento ocorre quando uma tecla é pressionada, nesse caso o KEYDOWN(setinha para baixo)
        if evento.key == pygame.K_RIGHT:
            if (jogador.x + tamanho_jogador) < TAMANHO_TELA[0]: # Verifica se a bolinha ainda vai estar nos limites da tela 
                jogador.x = jogador.x + 10 # Caso eles ainda estejam dentro dos limites da tela, a bolinha pode avançar mais dez pixels 
        if evento.key == pygame.K_LEFT: # A mesma coisa ocorre para o lado esquerdo
            if jogador.x > 0:
                jogador.x = jogador.x - 10

# A função E é responsável pela movimentação da bola 
def movimentar_bola(bola,movimento_bola,tamanho_bola,TAMANHO_TELA,jogador,blocos):
    movimento = movimento_bola
    # Atualiza o movimento da bola como em um "plano cartesiano", aumentando ou diminuindo o valor do x e do y
    bola.x = bola.x + movimento[0] 
    bola.y = bola.y + movimento[1]

# Quando a bola bate na borda da tela, ela vai para o lado oposto
    if bola.x <= 0: 
        movimento[0] = - movimento[0]
    if bola.y <= 0:
        movimento[1] = - movimento[1]
    if bola.x + tamanho_bola >= TAMANHO_TELA[0]:
        movimento[0] = - movimento[0]
# Caso a bola caia, você perde (None)
    if bola.y + tamanho_bola >= TAMANHO_TELA[1]:
        movimento = None

    if jogador.collidepoint(bola.x, bola.y): # Se a bola encostar na plataforma que o jogador controla, a bola vai para cima
        movimento[1] = - movimento[1]
    for bloco in blocos: # O bloco irá sumir se a bola encostar nele
        if bloco.collidepoint(bola.x, bola.y):
            blocos.remove(bloco)
            movimento[1] = - movimento[1]
    return movimento

# Atualiza a pontuação quando o bloco é quebrado
def atualizar_pontuacao(pontuacao,cores,tela,qtde_total_blocos):
    fonte = pygame.font.Font(None, 30) # Cria o texto que será a pontuação
    texto = fonte.render(f"Pontuação: {pontuacao}", 1, cores["coffee"]) # Nomeia o texto de "pontuação"
    tela.blit(texto, (0, 780)) # Posição onde o texto irá aparecer
    if pontuacao >= qtde_total_blocos:
        return True # O jogador ganha quando acertar todos os blocos
    else:
        return False
