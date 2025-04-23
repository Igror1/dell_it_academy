from tkinter import messagebox
import tkinter as tk

class StartupRushController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.b_buttons()

    def b_buttons(self):
        self.view.btn_cadastrar.config(command=lambda: self.view.notebook.select(1))
        self.view.btn_adicionar.config(command=self.adicionar_startup)
        self.view.btn_iniciar.config(command=self.iniciar_torneio)
        self.view.btn_voltar_cadastro.config(command=lambda: self.view.notebook.select(0))

    def adicionar_startup(self):
        try:
            nome = self.view.entry_nome.get().strip()
            slogan = self.view.entry_slogan.get().strip()
            ano = self.view.entry_ano.get().strip()
            self.model.adicionar_startup(nome, slogan, ano)
            self.view.lbl_contador.config(text=f"Startups cadastradas: {len(self.model.startups)}/8")
            self.view.entry_nome.delete(0, tk.END)
            self.view.entry_slogan.delete(0, tk.END)
            self.view.entry_ano.delete(0, tk.END)
            self.atualizar_status_botoes()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def atualizar_status_botoes(self):
        if 4 <= len(self.model.startups) <= 8 and len(self.model.startups) % 2 == 0:
            self.view.btn_iniciar.config(state=tk.NORMAL)
        else:
            self.view.btn_iniciar.config(state=tk.DISABLED)

    def iniciar_torneio(self):
        try:
            if len(self.model.startups) < 4 or len(self.model.startups) > 8 or len(self.model.startups) % 2 != 0:
                raise ValueError("O torneio requer entre 4 e 8 startups, em número par!") 
            self.model.sortear_batalhas()
            self.view.notebook.tab(2, state="normal")
            self.view.notebook.select(2)
            self.view.mostrar_batalhas(self.model.batalhas,
                                       self.model.batalhas_concluidas,
                                       self.model.rodada_atual,
                                       self.tela_batalha,
                                       self.voltar_cadastro)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def voltar_cadastro(self):
        self.view.notebook.select(1)

    def tela_batalha(self, startup1, startup2):
        self.view.notebook.tab(3, state="normal")
        self.view.notebook.select(3)
        self.view.tela_batalha(startup1, startup2, self.aplicar_evento, self.finalizar_batalha)

    def aplicar_evento(self, startup, evento, pontos, startup1, startup2):
        try:
            startup.set_pontuacao(startup.get_pontuacao() + pontos)
            startup.eventos_rodada.add(evento)
            startup.estatisticas[evento] += 1
            self.view.label_pontuacao_s1.config(text=f"Pontuação: {startup1.get_pontuacao()}")
            self.view.label_pontuacao_s2.config(text=f"Pontuação: {startup2.get_pontuacao()}")
            self.view.tela_batalha(startup1, startup2, self.aplicar_evento, self.finalizar_batalha)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def finalizar_batalha(self, startup1, startup2):
        try:
            vencedor = self.model.finalizar_batalha(startup1, startup2)
            messagebox.showinfo("Resultado", f"Vencedor: {vencedor.nome}!\nGanhou +30 pontos.")
            self.view.notebook.tab(6, state="normal")
            self.view.mostrar_historico(self.model.historico_batalhas,
                                        lambda: self.view.notebook.select(4),
                                        lambda: self.view.notebook.select(2))
            
            if set(self.model.batalhas_concluidas) == set(self.model.batalhas):
                self.avancar_rodada()
            else:
                self.view.notebook.select(2)
                self.view.mostrar_batalhas(self.model.batalhas,
                                           self.model.batalhas_concluidas,
                                           self.model.rodada_atual,
                                           self.tela_batalha,
                                           self.voltar_cadastro)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def avancar_rodada(self):
        try:
            self.model.avancar_rodada()
            if len(self.model.startups) == 1:
                self.view.notebook.tab(4, state="normal")
                self.view.notebook.tab(5, state="normal")
                self.view.notebook.select(4)
                self.view.mostrar_campeao(self.model.startups[0],
                                          self.reiniciar_torneio,
                                          lambda: self.view.notebook.select(5),
                                          lambda: self.view.notebook.select(6))
                startups_ordenadas = sorted(self.model.startups_originais, key=lambda s: s.get_pontuacao(), reverse=True)
                self.view.mostrar_relatorio(startups_ordenadas,
                                            lambda: self.view.notebook.select(4))
            else:
                self.view.notebook.select(2)
                self.view.mostrar_batalhas(self.model.batalhas,
                                           self.model.batalhas_concluidas,
                                           self.model.rodada_atual,
                                           self.tela_batalha,
                                           self.voltar_cadastro)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            self.reiniciar_torneio()

    def reiniciar_torneio(self):
        self.model.reiniciar()
        self.view.notebook.tab(2, state="disabled")
        self.view.notebook.tab(3, state="disabled")
        self.view.notebook.tab(4, state="disabled")
        self.view.notebook.tab(5, state="disabled")
        self.view.notebook.tab(6, state="disabled")
        self.view.notebook.select(0)
        self.view.criar_tela_inicial()
        self.view.criar_tela_cadastro()
        self.b_buttons()