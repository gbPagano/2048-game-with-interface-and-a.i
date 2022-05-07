# Jogo 2048 em Pygame com algoritmo de Monte-Carlo
## Introdução
Nesse projeto, desenvolvi uma réplica do jogo
2048 com interface e implementei um algoritmo de
busca em árvore Monte-Carlo em Python,
utilizando somente as bibliotecas Pygame e
Numpy.

A busca em árvore Monte-Carlo foi utilizada com
o objetivo de vencer o jogo, esse objetivo foi
concluído e foi possível alcançar até a peça de 4096.
## Requisitos
* Ter o Python instalado na versão 3.10.4 (durante o desenvolvimento, utilizei a versão 3.10.4, então não garanto que versões anteriores funcionem);
    * Ter as seguintes bibliotecas no Python:
        * numpy==1.21.6
        * pygame==2.1.2
## Como utilizar
### Instalando as bibliotecas necessárias
```bash
$ git clone https://github.com/gbPagano/2048-game-with-interface-and-a.i
$ cd 2048-game-with-interface-and-a.i
$ pip install -r requirements.txt
```
### Executando o jogo
Abra o arquivo ./2048-game-with-interface-and-a.i/2048.py e verifique a variável ```ia_jogando``` na **linha 7**.

Caso queira jogar, deixe a variável com valor False:
```py
ia_jogando = False
```
Caso queira que a i.a jogue, deixe a variável com valor True:
```py
ia_jogando = True
```
Depois execute o script:
```bash
$ python 2048.py
```
---
![exemplo](./images/readme/exemplo4096.png)
