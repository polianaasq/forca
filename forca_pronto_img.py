#!/usr/bin/env python3
import os
from random import randrange

class Exibidor():
    
    forca = None
    
    mensagem = ''
    pergunta = ''
    lin = 0
    col = 0
   

    def atualizar(self):
                
        self.escrever_na_posicao("====================== Jogo da forca ======================")
        self.exibir_forca(self.forca.numero_tentativas)
        self.lin += 1
        self.col = 1
        
        self.escrever_na_posicao(' '.join(self.forca.letras_acertadas))
        self.lin += 2
        
        self.escrever_na_posicao(self.mensagem)
        self.lin += 1
        
    def exibir_forca(self, erros):
        for linha in forca_img[erros]:
            self.escrever_na_posicao(linha)
            self.lin += 1
        
    def perguntar(self, pergunta):
        self.pergunta = pergunta
        self.atualizar()
        return self.perguntar_na_posicao(self.pergunta).upper()

    def limpar_tela(self):
        os.system('clear')

    def mensagem_na_posicao(self, msg):
        xx =  msg
        return xx
    
    def escrever_na_posicao(self, msg):
        print(self.mensagem_na_posicao(msg))
    
    def perguntar_na_posicao(self, msg):
        return input(self.mensagem_na_posicao(msg))
        
        
class Forca():
    
    exibidor = Exibidor()
    
    jogar_de_novo = True
    
    numero_tentativas_maximo = 6
    
    numero_tentativas = 0
    acertos = 0
    tamanho = 0
    
    enforcou = False
    acertou = False
    numero_tentativas = 0
    
    palavra_secreta = ''
    letras_acertadas = []
    
    chutes = ''
    
    def carrega_palavra_secreta(self):
        palavras_file = open("palavras.txt", "r")
        palavras_txt = palavras_file.read()
        palavras = palavras_txt.split('\n')
        palavra_idx = randrange(len(palavras))
        self.palavra_secreta = palavras[palavra_idx].upper()
        
    def inicializa_letras_acertadas(self):
        self.letras_acertadas = []
        for letra in self.palavra_secreta:
            self.letras_acertadas.append('_')
        
    def pede_chute(self):
        return self.exibidor.perguntar("Entre com uma letra: ")
    
    def cont_jogar(self):
        resposta = ''
        ja_respondeu = False
        while resposta != 'N' and resposta != 'S':
            if ja_respondeu:
                self.exibidor.mensagem = "Opção inválida"
            
            resposta = self.exibidor.perguntar("Para jogar novamente digite SIM ou para parar NAO: ").upper()[0]
            ja_respondeu = True
        self.jogar_de_novo = resposta == 'S'
    
    def marca_chute_correto(self, chute):
        for posicao in range(0, len(self.letras_acertadas)):
            if chute == self.palavra_secreta[posicao]:
                self.letras_acertadas[posicao] = chute
    
    def jogar(self):
        self.carrega_palavra_secreta()
        self.inicializa_letras_acertadas()
        
        self.enforcou = False
        self.acertou = False
        self.numero_tentativas = 0
        
        self.exibidor.mensagem = "A palavra tem " + str(len(self.palavra_secreta)) + " letras"
        
        chute = ' '
        
        while not self.enforcou and not self.acertou:
            
            chute = self.pede_chute()
            
            if chute in self.chutes:
                self.exibidor.mensagem = "Você já digitou essa letra"
            else:
                self.chutes += chute
                if chute in self.palavra_secreta:
                    self.marca_chute_correto(chute)
                    self.exibidor.mensagem = "Acertou!!!";
                else:
                    self.numero_tentativas += 1
                    self.exibidor.mensagem = "Errou a letra. Tentativas: " + str(self.numero_tentativas)
                
            if self.numero_tentativas == self.numero_tentativas_maximo:
                self.enforcou = True
        
            if "_" not in self.letras_acertadas:
                self.acertou = True
            
        if self.acertou:
            self.exibidor.mensagem = "Você acertou a palavra: " + self.palavra_secreta
        if self.enforcou:
            self.exibidor.mensagem = "Você se enforcou (a palavra era " + self.palavra_secreta + ")."
            
            
    def loop(self):
        try:
            self.exibidor.forca = self
            while self.jogar_de_novo:
                self.jogar()
                self.cont_jogar()
        except KeyboardInterrupt:
            print("\nA execução foi interrompida")

        
def main():
    Forca().loop()

forca_img = [
    [
        '  +---+',
        '  |   |',
        '      |',
        '      |',
        '      |',
        '      |',
        '=========',
    ],[
        '  +---+',
        '  |   |',
        '  O   |',
        '      |',
        '      |',
        '      |',
        '=========',
    ],[
        '  +---+',
        '  |   |',
        '  O   |',
        '  |   |',
        '      |',
        '      |',
        '========='
    ],[
        '  +---+',
        '  |   |',
        '  O   |',
        ' /|   |',
        '      |',
        '      |',
        '=========',
    ],[
        '  +---+',
        '  |   |',
        '  O   |',
        ' /|\  |',
        '      |',
        '      |',
        '=========',
    ],[
        '  +---+',
        '  |   |',
        '  O   |',
        ' /|\  |',
        ' /    |',
        '      |',
        '=========',
    ],[
        '  +---+',
        '  |   |',
        '  O   |',
        ' /|\  |',
        ' / \  |',
        '      |',
        '========='
    ]
]


main()
