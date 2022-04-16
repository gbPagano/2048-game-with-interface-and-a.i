import numpy as np
import pygame, os, sys, datetime
from core import*
from montecarlo import*
from process import*

PRETO = (0,0,0)
BRANCO = (255,255,255)
VERDE = (0,255,0)
VERMELHO = (255,0,0)

FUNDO = (205,193,180)

TAMANHO = (499, 499)
                
class Game():
    def __init__(self):
        self.tela = pygame.display.set_mode(TAMANHO)
        self.fundo = pygame.image.load(os.path.join(os.getcwd(),"images", "fundo.png")).convert_alpha()
        self.relogio = pygame.time.Clock()
        self.velocidade = 35
        self.carregar_arquivos()

    def carregar_arquivos(self):
        self.num2 = pygame.image.load(os.path.join(os.getcwd(),"images", "num2.png")).convert_alpha()
        self.num4 = pygame.image.load(os.path.join(os.getcwd(),"images", "num4.png")).convert_alpha()
        self.num8 = pygame.image.load(os.path.join(os.getcwd(),"images", "num8.png")).convert_alpha()
        self.num16 = pygame.image.load(os.path.join(os.getcwd(),"images", "num16.png")).convert_alpha()
        self.num32 = pygame.image.load(os.path.join(os.getcwd(),"images", "num32.png")).convert_alpha()
        self.num64 = pygame.image.load(os.path.join(os.getcwd(),"images", "num64.png")).convert_alpha()
        self.num128 = pygame.image.load(os.path.join(os.getcwd(),"images", "num128.png")).convert_alpha()
        self.num256 = pygame.image.load(os.path.join(os.getcwd(),"images", "num256.png")).convert_alpha()
        self.num512 = pygame.image.load(os.path.join(os.getcwd(),"images", "num512.png")).convert_alpha()
        self.num1024 = pygame.image.load(os.path.join(os.getcwd(),"images", "num1024.png")).convert_alpha()
        self.num2048 = pygame.image.load(os.path.join(os.getcwd(),"images", "num2048.png")).convert_alpha()
        self.num4096 = pygame.image.load(os.path.join(os.getcwd(),"images", "num4096.png")).convert_alpha()
        self.num8192 = pygame.image.load(os.path.join(os.getcwd(),"images", "num8192.png")).convert_alpha()



    def update_tela(self):
        self.relogio.tick(60)
        self.tela.blit(self.fundo,(0,0))
        self.print_tabuleiro_atual()
        pygame.display.update()

    def eventos(self):
        if ia_jogando:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        return
        else:
            while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                            return
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_DOWN or event.key == pygame.K_s:                            
                                return 's'
                            elif event.key == pygame.K_UP or event.key == pygame.K_w: 
                                return 'w'
                            elif event.key == pygame.K_LEFT or event.key == pygame.K_a: 
                                return 'a'
                            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                                return 'd'

    def print_tabuleiro_atual(self):
        for i in range(4):
            for j in range(4):
                if self.tabuleiro[i][j] != 0:
                    num_atual = self.tabuleiro[i][j]

                    if i == 0: y = 15
                    elif i == 1: y = 136
                    elif i == 2: y = 257
                    else: y = 378
                    if j == 0: x = 15
                    elif j == 1: x = 136
                    elif j == 2: x = 257
                    else: x = 378

                    self.blit_pecas(num_atual,x,y)

    def criar_novo_jogo(self):
        self.tabuleiro = novo_jogo()


    def mover(self,jogada,copia):
        if jogada == 'a':
            pos = np.copy(copia)
            final = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            anterior = False
            for k in range(1,11):
                self.tela.blit(self.fundo,(0,0))
                for i in range(4):
                    for j in range(4):
                        if copia[i][j] != 0:
                            num_atual = copia[i][j]                           

                            if i == 0: y = 15
                            elif i == 1: y = 136
                            elif i == 2: y = 257
                            else: y = 378
                            if j == 0: x = 15
                            elif j == 1: x = 136
                            elif j == 2: x = 257
                            else: x = 378
                            
                            if final[i][j] == 0:
                        
                                final_pos = x
                                somado = False
                                voltou = 0
                                if j > 0: 
                                    if pos[i][j-1] == 0: 
                                        final_pos -= 121
                                        voltou += 1
                                        pos[i][j-1],pos[i][j] = copia[i][j], 0
                                    elif pos[i][j-1] == copia[i][j] and not somado:
                                        final_pos -= 121
                                        somado = True
                                        voltou += 1
                                        pos[i][j-1],pos[i][j] = copia[i][j], 0
                                    
                                    if j > 1 and voltou > 0:
                                        if pos[i][j-2] == 0: 
                                            final_pos -= 121
                                            voltou += 1
                                            pos[i][j-2],pos[i][j-1] = copia[i][j], 0
                                        elif pos[i][j-2] == copia[i][j] and not somado and not anterior:
                                            final_pos -= 121
                                            somado = True
                                            voltou += 1
                                            pos[i][j-2],pos[i][j-1] = copia[i][j], 0
                                        
                                        if  j > 2 and voltou > 1:
                                            if pos[i][j-3] == 0: 
                                                final_pos -= 121
                                                voltou += 1
                                                pos[i][j-3],pos[i][j-2] = copia[i][j], 0
                                            elif pos[i][j-3] == copia[i][j] and not somado and not anterior:
                                                final_pos -= 121
                                                somado = True
                                                voltou += 1
                                                pos[i][j-3],pos[i][j-2] = copia[i][j], 0
                                anterior = somado                              
                                final[i][j] = final_pos
                            
                            else:
                                final_pos = final[i][j]

                            if x > final_pos:
                                x -= self.velocidade*k
                                if x < final_pos: x = final_pos
                            else: x = final_pos

                            self.blit_pecas(num_atual,x,y)
                
                self.relogio.tick(60)
                pygame.display.update()
        
        if jogada == 'd':
            pos = np.copy(copia)

            final = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            anterior = False
            for k in range(1,11):
                self.tela.blit(self.fundo,(0,0))
                for i in range(4):
                    for j in range(3,-1,-1):
                        if copia[i][j] != 0:
                            num_atual = copia[i][j]                           

                            if i == 0: y = 15
                            elif i == 1: y = 136
                            elif i == 2: y = 257
                            else: y = 378
                            if j == 0: x = 15
                            elif j == 1: x = 136
                            elif j == 2: x = 257
                            else: x = 378

                            if final[i][j] == 0:
                        
                                final_pos = x
                                somado = False
                                voltou = 0
                                if j < 3: 
                                    if pos[i][j+1] == 0: 
                                        final_pos += 121
                                        voltou += 1
                                        pos[i][j+1],pos[i][j] = copia[i][j], 0
                                    elif pos[i][j+1] == copia[i][j] and not somado:
                                        final_pos += 121
                                        somado = True
                                        voltou += 1
                                        pos[i][j+1],pos[i][j] = copia[i][j], 0
                                    
                                    if j < 2 and voltou > 0:
                                        if pos[i][j+2] == 0: 
                                            final_pos += 121
                                            voltou += 1
                                            pos[i][j+2],pos[i][j+1] = copia[i][j], 0
                                        elif pos[i][j+2] == copia[i][j] and not somado and not anterior:
                                            final_pos += 121
                                            somado = True
                                            voltou += 1
                                            pos[i][j+2],pos[i][j+1] = copia[i][j], 0
                                        
                                        if  j < 1 and voltou > 1:
                                            if pos[i][j+3] == 0: 
                                                final_pos += 121
                                                voltou += 1
                                                pos[i][j+3],pos[i][j+2] = copia[i][j], 0
                                            elif pos[i][j+3] == copia[i][j] and not somado and not anterior:
                                                final_pos += 121
                                                somado = True
                                                voltou += 1
                                                pos[i][j+3],pos[i][j+2] = copia[i][j], 0
                                anterior = somado
                                final[i][j] = final_pos

                            else:
                                final_pos = final[i][j]

                            if x < final_pos:
                                x += self.velocidade*k
                                if x > final_pos: x = final_pos
                            else: x = final_pos

                            self.blit_pecas(num_atual,x,y)
                
                self.relogio.tick(60)
                pygame.display.update()
         
        if jogada == 'w':
            transposta = np.transpose(copia)
            pos = np.copy(transposta)
            final = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            anterior = False
            for k in range(1,11):
                self.tela.blit(self.fundo,(0,0))
                for i in range(4):
                    for j in range(4):
                        if transposta[i][j] != 0:
                            num_atual = copia[j][i]                           
                            
                            if j == 0: y = 15
                            elif j == 1: y = 136
                            elif j == 2: y = 257
                            else: y = 378
                            if i == 0: x = 15
                            elif i == 1: x = 136
                            elif i == 2: x = 257
                            else: x = 378
                            
                            if final[i][j] == 0:
                        
                                final_pos = y
                                somado = False
                                voltou = 0
                                if j > 0: 
                                    if pos[i][j-1] == 0: 
                                        final_pos -= 121
                                        voltou += 1
                                        pos[i][j-1],pos[i][j] = transposta[i][j], 0
                                    elif pos[i][j-1] == transposta[i][j] and not somado:
                                        final_pos -= 121
                                        somado = True
                                        voltou += 1
                                        pos[i][j-1],pos[i][j] = transposta[i][j], 0
                                    
                                    if j > 1 and voltou > 0:
                                        if pos[i][j-2] == 0: 
                                            final_pos -= 121
                                            voltou += 1
                                            pos[i][j-2],pos[i][j-1] = transposta[i][j], 0
                                        elif pos[i][j-2] == transposta[i][j] and not somado and not anterior:
                                            final_pos -= 121
                                            somado = True
                                            voltou += 1
                                            pos[i][j-2],pos[i][j-1] = transposta[i][j], 0
                                        
                                        if  j > 2 and voltou > 1:
                                            if pos[i][j-3] == 0: 
                                                final_pos -= 121
                                                voltou += 1
                                                pos[i][j-3],pos[i][j-2] = transposta[i][j], 0
                                            elif pos[i][j-3] == transposta[i][j] and not somado and not anterior:
                                                final_pos -= 121
                                                somado = True
                                                voltou += 1
                                                pos[i][j-3],pos[i][j-2] = transposta[i][j], 0
                                anterior = somado
                                final[i][j] = final_pos
                            
                            else:
                                final_pos = final[i][j]

                            if y > final_pos:
                                y -= self.velocidade*k
                                if y < final_pos: y = final_pos
                            else: y = final_pos

                            self.blit_pecas(num_atual,x,y)
                
                self.relogio.tick(60)
                pygame.display.update()
        
        if jogada == 's':
            transposta = np.transpose(copia)
            pos = np.copy(transposta)

            final = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            anterior = False
            for k in range(1,11):
                self.tela.blit(self.fundo,(0,0))
                for i in range(4):
                    for j in range(3,-1,-1):
                        if transposta[i][j] != 0:
                            num_atual = copia[j][i]                          

                            if j == 0: y = 15
                            elif j == 1: y = 136
                            elif j == 2: y = 257
                            else: y = 378
                            if i == 0: x = 15
                            elif i == 1: x = 136
                            elif i == 2: x = 257
                            else: x = 378

                            if final[i][j] == 0:
                        
                                final_pos = y
                                somado = False
                                voltou = 0
                                if j < 3: 
                                    if pos[i][j+1] == 0: 
                                        final_pos += 121
                                        voltou += 1
                                        pos[i][j+1],pos[i][j] = transposta[i][j], 0
                                    elif pos[i][j+1] == transposta[i][j] and not somado:
                                        final_pos += 121
                                        somado = True
                                        voltou += 1
                                        pos[i][j+1],pos[i][j] = transposta[i][j], 0
                                    
                                    if j < 2 and voltou > 0:
                                        if pos[i][j+2] == 0: 
                                            final_pos += 121
                                            voltou += 1
                                            pos[i][j+2],pos[i][j+1] = transposta[i][j], 0
                                        elif pos[i][j+2] == transposta[i][j] and not somado and not anterior:
                                            final_pos += 121
                                            somado = True
                                            voltou += 1
                                            pos[i][j+2],pos[i][j+1] = transposta[i][j], 0
                                        
                                        if  j < 1 and voltou > 1:
                                            if pos[i][j+3] == 0: 
                                                final_pos += 121
                                                voltou += 1
                                                pos[i][j+3],pos[i][j+2] = transposta[i][j], 0
                                            elif pos[i][j+3] == transposta[i][j] and not somado and not anterior:
                                                final_pos += 121
                                                somado = True
                                                voltou += 1
                                                pos[i][j+3],pos[i][j+2] = transposta[i][j], 0
                                anterior = somado
                                final[i][j] = final_pos

                            else:
                                final_pos = final[i][j]

                            if y < final_pos:
                                y += self.velocidade*k
                                if y > final_pos: y = final_pos
                            else: y = final_pos

                            self.blit_pecas(num_atual,x,y)
                
                self.relogio.tick(60)
                pygame.display.update() 
       
        self.print_tabuleiro_atual()
            
    def blit_pecas(self,num_atual,x,y):

        if num_atual == 2:
            self.tela.blit(self.num2,(x,y))
        elif num_atual == 4:
            self.tela.blit(self.num4,(x,y))
        elif num_atual == 8:
            self.tela.blit(self.num8,(x,y))
        elif num_atual == 16:
            self.tela.blit(self.num16,(x,y))
        elif num_atual == 32:
            self.tela.blit(self.num32,(x,y))
        elif num_atual == 64:
            self.tela.blit(self.num64,(x,y))
        elif num_atual == 128:
            self.tela.blit(self.num128,(x,y))
        elif num_atual == 256:
            self.tela.blit(self.num256,(x,y))
        elif num_atual == 512:
            self.tela.blit(self.num512,(x,y))
        elif num_atual == 1024:
            self.tela.blit(self.num1024,(x,y))
        elif num_atual == 2048:
            self.tela.blit(self.num2048,(x,y))
        elif num_atual == 4096:
            self.tela.blit(self.num4096,(x,y))
        elif num_atual == 8192:
            self.tela.blit(self.num8192,(x,y))

    def acabou(self):
        while True:
            self.eventos()

ia_jogando = False

if __name__ == '__main__':
    if ia_jogando:
        real_inicio = datetime.datetime.now()
        pool = fazer()
    pygame.init()
    jogo = Game()
    jogo.criar_novo_jogo()
    jogadas = 0
    game_over = False
    pontos = [0]
    while not game_over:
        if ia_jogando:
            inicio = datetime.datetime.now()
            x = 10+jogadas
            y = 5
            if jogadas > 1300: y = 10

        jogo.update_tela()      
        
        if jogadas == 0:
            os.system('cls')
            print(f'jogadas: {jogadas}')
            print(f'pontos: {pontos[0]}')
            print_tabuleiro(jogo.tabuleiro)
            copia = np.copy(jogo.tabuleiro)
            if ia_jogando:
                jogada = monte_carlo(jogo.tabuleiro,x,pontos,y,True,pool)
            else:
                jogada = jogo.eventos()
            
            if jogada_player(jogo.tabuleiro,jogada,pontos):

                if not ia_jogando:
                    jogo.mover(jogada,copia)

                jogadas +=1
                aparecer_peca(jogo.tabuleiro)
        else:
            os.system('cls')        
            print(f'jogadas: {jogadas}')
            print(f'pontos: {pontos[0]}')
            print_tabuleiro(jogo.tabuleiro)
            if ia_jogando: print(final)            
            copia = np.copy(jogo.tabuleiro)

            if not verificar_final(jogo.tabuleiro,pontos):
                print('fim')
                print(f'pontuação final: {pontos[0]} em {jogadas} jogadas')
                game_over = True
                if ia_jogando: print(datetime.datetime.now()-real_inicio)
                jogo.acabou()
                pygame.quit()
                sys.exit()
                break
            if ia_jogando: jogada = monte_carlo(jogo.tabuleiro,x,pontos,y,True,pool)
            else: jogada = jogo.eventos()
            if jogada_player(jogo.tabuleiro,jogada,pontos):

                if not ia_jogando: jogo.mover(jogada,copia)

                jogadas +=1
                aparecer_peca(jogo.tabuleiro)
            
        if ia_jogando:
            final = (datetime.datetime.now()-inicio)