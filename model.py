import random

##
class Startup:
    def __init__(self, nome, slogan, ano_fundacao):
        self.nome = nome
        self.slogan = slogan
        self.ano_fundacao = ano_fundacao
        self._pontuacao = 70
        self.eventos_rodada = set()
        self.estatisticas = {"Pitch convincente": 0,
                            "Produto com bugs": 0,
                            "Boa tração de usuários": 0,
                            "Investidor irritado": 0,
                            "Fake news no pitch": 0}


    def get_pontuacao(self):
        return self._pontuacao


    def set_pontuacao(self, valor): 
        if valor < 0:
            raise ValueError("Pontuação não pode ser negativa") #validação pontuacao
        self._pontuacao = valor
####
class Torneio:

    def __init__(self):
        self.startups = []
        self.startups_originais = []
        self.batalhas = []
        self.batalhas_concluidas = []
        self.historico_batalhas = []
        self.rodada_atual = 1
        self.batalha_id = 1

    def adicionar_startup(self, nome, slogan, ano):
        if len(self.startups) >= 8:  
            raise ValueError("Máximo de 8 startups atingido!") #validacao tamanho e preench
        
        if not nome or not slogan or not ano:
            raise ValueError("Preencha todos os campos!")
        
        try:
            ano = int(ano)
            if ano > 2025 or ano < 2000:
                raise ValueError("Ano inválido!")
            
        except ValueError:
            raise ValueError("Ano inválido!")
        
        startup = Startup(nome, slogan, ano)
        self.startups.append(startup)
        self.startups_originais.append(startup)
        return startup

    def sortear_batalhas(self):

        if len(self.startups) % 2 != 0:
            raise ValueError("Número de startups deve ser par!") #validacao par
        
        random.shuffle(self.startups)
        self.batalhas = [(self.startups[i], self.startups[i+1]) for i in range(0, len(self.startups), 2)]
        return self.batalhas

    def finalizar_batalha(self, startup1, startup2):
        if startup1.get_pontuacao() == startup2.get_pontuacao():
            vencedor = self.shark_fight(startup1, startup2)
        else:
            vencedor = startup1 if startup1.get_pontuacao() > startup2.get_pontuacao() else startup2
        
        vencedor.set_pontuacao(vencedor.get_pontuacao() + 30)
        perdedor = startup2 if vencedor == startup1 else startup1
        
        self.historico_batalhas.append((self.batalha_id, startup1.nome, startup2.nome, vencedor.nome))
        self.batalha_id += 1
        self.startups.remove(perdedor)
        startup1.eventos_rodada.clear()
        startup2.eventos_rodada.clear()
        self.batalhas_concluidas.append((startup1, startup2))
        
        return vencedor

    def shark_fight(self, startup1, startup2):
        vencedor = random.choice([startup1, startup2])
        vencedor.set_pontuacao(vencedor.get_pontuacao() + 2)
        return vencedor

    def avancar_rodada(self):
        self.batalhas_concluidas.clear()
        self.batalhas = []
        
        if len(self.startups) >= 2:
            self.rodada_atual += 1
            self.sortear_batalhas()
        elif len(self.startups) != 1:
            raise ValueError("Não há startups suficientes para continuar!")

    def reiniciar(self):
        self.startups = []
        self.startups_originais = []
        self.batalhas = []
        self.batalhas_concluidas = []
        self.historico_batalhas = []
        self.rodada_atual = 1
        self.batalha_id = 1