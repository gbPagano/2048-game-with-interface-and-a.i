

import os, time, sys
import numpy as np
from core import*
from process import*

def randomizar():
    return random.choice(['w','s','a','d'])

def monte_carlo(tabuleiro2,x,pontos,y,z,pool):
    inicio = time.time()
    jogadas2 = np.array(['a','s','w','d'])


    pontuacao_a = [0,'a']
    pontuacao_s = [0,'s']
    pontuacao_w = [0,'w']
    pontuacao_d = [0,'d']


    # pesos = np.array( [
    #     [0.150,0.121,0.102,0.0999],
    #     [0.0724,0.076,0.088,0.0997],
    #     [0.0606,0.0562,0.0371,0.0161],
    #     [0.0033,0.0057,0.0099,0.0125],
    # ])
    variaveis = [
        (pontuacao_a,pontuacao_s,pontuacao_w,pontuacao_d,0,jogadas2,tabuleiro2,x,y,pontos),
        (pontuacao_a,pontuacao_s,pontuacao_w,pontuacao_d,1,jogadas2,tabuleiro2,x,y,pontos),
        (pontuacao_a,pontuacao_s,pontuacao_w,pontuacao_d,2,jogadas2,tabuleiro2,x,y,pontos),
        (pontuacao_a,pontuacao_s,pontuacao_w,pontuacao_d,3,jogadas2,tabuleiro2,x,y,pontos),
    ] 

    if z:
    
        # pool = Pool(processes=os.cpu_count())
        
        
            
        results = pool.map(calcular,variaveis)   

        print(results)

        maximo = 0
        variavel = 0
        for i in range(4):
            valor = float(results[i][0])
            if valor > maximo:
                maximo = valor
                variavel = i
        print(results[variavel][1])
        print(time.time()-inicio)
        return results[variavel][1]

    else:
            
        calcular(variaveis[0])
        calcular(variaveis[1])
        calcular(variaveis[2])
        calcular(variaveis[3])

        pontuacoes = np.array([pontuacao_a,pontuacao_s,pontuacao_w,pontuacao_d])

        #print(pontuacoes)
        

        maximo = 0
        variavel = 0
        for i in range(4):
            valor = float(pontuacoes[i][0])
            if valor > maximo:
                maximo = valor
                variavel = i
        print(pontuacoes[variavel][1])
        



        print(time.time()-inicio)
        #print(pontuacao_a,pontuacao_s,pontuacao_w,pontuacao_d)
        # sys.exit()
        
        return pontuacoes[variavel][1]

def calcular(variavel):
    i = variavel[4]
    pontuacao_a = variavel[0]
    pontuacao_s = variavel[1]
    pontuacao_w = variavel[2]
    pontuacao_d = variavel[3]
    
    jogadas2 = variavel[5]
    tabuleiro2 = variavel[6]
    x = variavel[7]
    y = variavel[8]
    pontos = variavel[9]
    jogada2 = jogadas2[i]

    recebivel = True
    
    for j in range(x):
        jogadas = 0
        pontos2 = np.copy(pontos)
        tabuleiro = np.copy(tabuleiro2)
        game_over = False

        while not game_over and jogadas < y:
            
            if jogadas == 0:
                jogada = jogada2
                #print(i)
                
                if jogada_player(tabuleiro,jogada,pontos2):
                    jogadas +=1
                    aparecer_peca(tabuleiro)
                else:
                    game_over = True
                    recebivel = False
                    break
            else: 
                if not verificar_final(tabuleiro,pontos2):                        
                    game_over = True
                    break
                jogada = random.choice(['w','s','a','d'])
                if jogada_player(tabuleiro,jogada,pontos2):
                    jogadas +=1
                    aparecer_peca(tabuleiro)
        if recebivel:            

            if i == 0:
                pontuacao_a[0] +=  pontos2[0]
            elif i == 1:
                pontuacao_s[0] +=  pontos2[0]
            elif i == 2:
                pontuacao_w[0] += pontos2[0]
            elif i == 3:
                pontuacao_d[0] += pontos2[0]

            #print(pontuacao_a,pontuacao_s,pontuacao_w,pontuacao_d,j)
    if i == 0:
        return pontuacao_a
    elif i == 1:
        return pontuacao_s
    elif i == 2:
        return pontuacao_w
    elif i == 3:
        return pontuacao_d  

