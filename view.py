import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class StartupRushView:
    def __init__(self, root):
        self.root = root
        self.root.title("STARTUP RUSH - IT Academy")
        self.root.geometry("800x600")
        
        #estilo
        self.bg_color = "#F8FAFB"
        self.text_color = "#2E3A46"
        self.label_color = "#5F6B78"
        self.btn_primary = "#0052CC"
        self.btn_primary_hover = "#003C99"
        self.btn_secondary = "#00875A"
        self.btn_secondary_hover = "#00663D"
        self.btn_battle = "#2684FF"
        self.btn_battle_hover = "#1070E8"
        self.btn_event = "#FFC400"
        self.btn_event_hover = "#FFAB00"
        self.btn_disabled = "#A5ADB0"
        self.accent_color = "#D92D20"
        #estilo 

        #fonte
        try:
            self.font_title = tkFont.Font(family="Roboto Bold", size=20)
            self.font_subtitle = tkFont.Font(family="Roboto Medium", size=16)
            self.font_body = tkFont.Font(family="Roboto Regular", size=12)
            self.font_small = tkFont.Font(family="Roboto Regular", size=10)
        except:
            self.font_title = tkFont.Font(family="Helvetica", size=20, weight="bold")
            self.font_subtitle = tkFont.Font(family="Helvetica", size=16)
            self.font_body = tkFont.Font(family="Helvetica", size=12)
            self.font_small = tkFont.Font(family="Helvetica", size=10)
        #fonte

        #estilo notebook
        style = ttk.Style()
        style.configure("TNotebook", background=self.bg_color)
        style.configure("TNotebook.Tab", font=self.font_body, padding=[10, 5])
        #estilonotebook
        
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=15, pady=15)
        
        ##
        self.frame_inicio = tk.Frame(self.notebook, bg=self.bg_color)
        self.frame_cadastro = tk.Frame(self.notebook, bg=self.bg_color)
        self.frame_batalhas = tk.Frame(self.notebook, bg=self.bg_color)
        self.frame_batalha_atual = tk.Frame(self.notebook, bg=self.bg_color)
        self.frame_campeao = tk.Frame(self.notebook, bg=self.bg_color)
        self.frame_relatorio = tk.Frame(self.notebook, bg=self.bg_color)
        self.frame_historico = tk.Frame(self.notebook, bg=self.bg_color)
        ##

        ##
        self.notebook.add(self.frame_inicio, text="Início")
        self.notebook.add(self.frame_cadastro, text="Cadastro")
        self.notebook.add(self.frame_batalhas, text="Batalhas")
        self.notebook.add(self.frame_batalha_atual, text="Batalha Atual")
        self.notebook.add(self.frame_campeao, text="Campeão")
        self.notebook.add(self.frame_relatorio, text="Relatório")
        self.notebook.add(self.frame_historico, text="Histórico")
        ##

        ##
        self.criar_tela_inicial()
        self.criar_tela_cadastro()
        self.notebook.tab(2, state="disabled")
        self.notebook.tab(3, state="disabled")
        self.notebook.tab(4, state="disabled")
        self.notebook.tab(5, state="disabled")
        self.notebook.tab(6, state="disabled")
        ##  
#######
    def criar_tela_inicial(self):
        for widget in self.frame_inicio.winfo_children():
            widget.destroy()
        
        tk.Label(self.frame_inicio, text="🚀 STARTUP RUSH", font=self.font_title,
            bg=self.bg_color, fg=self.text_color).pack(pady=30)
        
        btn_frame = tk.Frame(self.frame_inicio, bg=self.bg_color, 
        highlightbackground="#D6D8DB", highlightthickness=2)
        btn_frame.pack(pady=10)
        
        self.btn_cadastrar = tk.Button(btn_frame, text="Cadastrar Startups",
         font=self.font_body, bg=self.btn_secondary,fg="white", relief="flat",
        padx=20, pady=10)
        self.btn_cadastrar.pack()
        self.bind_hover(self.btn_cadastrar, self.btn_secondary, self.btn_secondary_hover)

    def criar_tela_cadastro(self):
        for widget in self.frame_cadastro.winfo_children():
            widget.destroy()
        
        tk.Label(self.frame_cadastro, text="Cadastro de Startups", font=self.font_subtitle,
            bg=self.bg_color, fg=self.text_color).pack(pady=20)
        
        form_frame = tk.Frame(self.frame_cadastro, bg="#F8F9FA", highlightbackground="#DEE2E6", 
        highlightthickness=2)
        form_frame.pack(padx=20, pady=10, fill="x")
        
        self.lbl_contador = tk.Label(form_frame, text="Startups cadastradas: 0/8", 
        font=self.font_small,bg="#F8F9FA", fg=self.label_color)
        self.lbl_contador.pack(pady=5)

        #
        tk.Label(form_frame, text="Nome:", font=self.font_body, bg="#F8F9FA", fg=self.label_color).pack()
        self.entry_nome = tk.Entry(form_frame, font=self.font_body, relief="solid", borderwidth=1)
        self.entry_nome.pack(pady=5, padx=20, fill="x")
        
        tk.Label(form_frame, text="Slogan:", font=self.font_body, bg="#F8F9FA", fg=self.label_color).pack()
        self.entry_slogan = tk.Entry(form_frame, font=self.font_body, relief="solid", borderwidth=1)
        self.entry_slogan.pack(pady=5, padx=20, fill="x")
        
        tk.Label(form_frame, text="Ano de Fundação:", font=self.font_body, bg="#F8F9FA", fg=self.label_color).pack()
        self.entry_ano = tk.Entry(form_frame, font=self.font_body, relief="solid", borderwidth=1)
        self.entry_ano.pack(pady=5, padx=20, fill="x")
        #

        btn_frame = tk.Frame(self.frame_cadastro, bg=self.bg_color)
        btn_frame.pack(pady=20)
        
        #
        self.btn_adicionar = tk.Button(btn_frame, text="Adicionar Startup", 
        font=self.font_body, bg=self.btn_primary,fg="white", relief="flat", 
        padx=20, pady=10)
        self.btn_adicionar.pack(side="left", padx=10)
        self.bind_hover(self.btn_adicionar, self.btn_primary, self.btn_primary_hover)
        #
        
        #
        self.btn_iniciar = tk.Button(btn_frame, text="Iniciar Torneio",
        font=self.font_body, bg=self.btn_primary,fg="white", relief="flat",
        padx=20, pady=10, state=tk.DISABLED)
        self.btn_iniciar.pack(side="left", padx=10)
        self.bind_hover(self.btn_iniciar, self.btn_primary, self.btn_primary_hover)
        #

        #
        self.btn_voltar_cadastro = tk.Button(btn_frame, text="⬅️ Voltar",
        font=self.font_body, bg=self.btn_secondary,fg="white", relief="flat", 
        padx=20, pady=10)
        self.btn_voltar_cadastro.pack(side="left", padx=10)
        self.bind_hover(self.btn_voltar_cadastro, self.btn_secondary, self.btn_secondary_hover)
#######   
    def mostrar_batalhas(self, batalhas, batalhas_concluidas, rodada_atual, 
                        callback_batalha, callback_voltar):
        for widget in self.frame_batalhas.winfo_children():
            widget.destroy()
        
        
        tk.Label(self.frame_batalhas, text=f"Rodada {rodada_atual}", font=self.font_subtitle,
            bg=self.bg_color, fg=self.text_color).pack(pady=20)
        
        battles_frame = tk.Frame(self.frame_batalhas, bg=self.bg_color)
        battles_frame.pack(fill="both", expand=True, padx=20)
        
        #
        for i, (startup1, startup2) in enumerate(batalhas, 1):
            batalha_concluida = (startup1, startup2) in batalhas_concluidas or (startup2, startup1) in batalhas_concluidas
            btn_batalha = tk.Button(battles_frame,text=f"⚔️ Batalha {i}: {startup1.nome} vs {startup2.nome}",
                                    font=self.font_body,bg=self.btn_disabled if batalha_concluida else self.btn_battle,
                                    fg="white" if not batalha_concluida else self.label_color,relief="flat",padx=20, pady=10,
                                    state="disabled" if batalha_concluida else "normal")
            btn_batalha.pack(fill="x", pady=5)
            
            if not batalha_concluida:
                btn_batalha.configure(command=lambda s1=startup1, s2=startup2: callback_batalha(s1, s2))
                self.bind_hover(btn_batalha, self.btn_battle, self.btn_battle_hover)
        #

        #
        btn_voltar_batalhas = tk.Button(self.frame_batalhas, text="⬅️ Voltar", font=self.font_body,
                                        bg=self.btn_secondary, fg="white", relief="flat", padx=20, pady=10,
                                        command=callback_voltar)
        btn_voltar_batalhas.pack(pady=20, anchor="e", padx=20)
        self.bind_hover(btn_voltar_batalhas, self.btn_secondary, self.btn_secondary_hover)
        #

#######       
    def tela_batalha(self, startup1, startup2, callback_evento, callback_finalizar):

        for widget in self.frame_batalha_atual.winfo_children():
            widget.destroy()
        
        container = tk.Frame(self.frame_batalha_atual, bg=self.bg_color)
        container.pack(fill="both", expand=True, padx=20, pady=20)
        
        #
        frame1 = tk.Frame(container, bg="#F8F9FA", highlightbackground="#D6D8DB", highlightthickness=2)
        frame1.pack(side="left", padx=10, pady=10, fill="both", expand=True)
        #

        #
        frame2 = tk.Frame(container, bg="#F8F9FA", highlightbackground="#D6D8DB", highlightthickness=2)
        frame2.pack(side="right", padx=10, pady=10, fill="both", expand=True)
        #
        
        #
        tk.Label(frame1, text=startup1.nome, font=self.font_subtitle, bg="#F8F9FA", fg=self.text_color).pack(pady=5)
        #
        
        #
        tk.Label(frame1, text=f"Slogan: {startup1.slogan}", font=self.font_body, bg="#F8F9FA", fg=self.label_color).pack()
        #

        #
        self.label_pontuacao_s1 = tk.Label(frame1, text=f"Pontuação: {startup1.get_pontuacao()}", font=self.font_body,
                                            bg="#F8F9FA", fg=self.label_color)
        self.label_pontuacao_s1.pack()
        #

        #
        tk.Label(frame2, text=startup2.nome, font=self.font_subtitle, bg="#F8F9FA", fg=self.text_color).pack(pady=5)
        #

        #
        tk.Label(frame2, text=f"Slogan: {startup2.slogan}", font=self.font_body, bg="#F8F9FA", fg=self.label_color).pack()
        #
        
        #
        self.label_pontuacao_s2 = tk.Label(frame2, text=f"Pontuação: {startup2.get_pontuacao()}", font=self.font_body,
                                            bg="#F8F9FA", fg=self.label_color)
        self.label_pontuacao_s2.pack()
        #
        
        #
        eventos = [
            ("Pitch convincente", 6, "✅"),
            ("Produto com bugs", -4, "❌"),
            ("Boa tração de usuários", 3, "✅"),
            ("Investidor irritado", -6, "❌"),
            ("Fake news no pitch", -8, "❌")
        ]
        #
        
        
        for evento, pontos, icon in eventos:
            #
            btn1 = tk.Button(frame1,
                            text=f"{icon} {evento} ({'+' if pontos > 0 else ''}{pontos})",
                            font=self.font_body,
                            bg=self.btn_event,
                            fg=self.text_color,
                            relief="flat",
                            padx=10, pady=5,
                            state=tk.NORMAL if evento not in startup1.eventos_rodada else tk.DISABLED,
                            command=lambda s=startup1, e=evento, p=pontos: callback_evento(s, e, p, startup1, startup2))
            btn1.pack(pady=2, padx=10, fill="x")
            #
            
            if evento not in startup1.eventos_rodada:
                self.bind_hover(btn1, self.btn_event, self.btn_event_hover)
            
            #
            btn2 = tk.Button(frame2,
                            text=f"{icon} {evento} ({'+' if pontos > 0 else ''}{pontos})",
                            font=self.font_body,
                            bg=self.btn_event,
                            fg=self.text_color,
                            relief="flat",
                            padx=10, pady=5,
                            state=tk.NORMAL if evento not in startup2.eventos_rodada else tk.DISABLED,
                            command=lambda s=startup2, e=evento, p=pontos: callback_evento(s, e, p, startup1, startup2))
            btn2.pack(pady=2, padx=10, fill="x")
            #

            if evento not in startup2.eventos_rodada:
                self.bind_hover(btn2, self.btn_event, self.btn_event_hover)
        
        #
        btn_finalizar = tk.Button(self.frame_batalha_atual,
                                 text="Finalizar Batalha",
                                 font=self.font_body,
                                 bg=self.btn_primary,
                                 fg="white",
                                 relief="flat",
                                 padx=20, pady=10,
                                 command=lambda: callback_finalizar(startup1, startup2))
        btn_finalizar.pack(pady=20)
        self.bind_hover(btn_finalizar, self.btn_primary, self.btn_primary_hover)
        #

#######
    def mostrar_campeao(self, campeao, callback_novo_torneio, callback_ver_relatorio, callback_ver_historico):
       
        for widget in self.frame_campeao.winfo_children():
            widget.destroy()
        
        #
        self.frame_campeao.configure(bg=self.bg_color)
        
        container = tk.Frame(self.frame_campeao, bg=self.bg_color, highlightbackground="#D6D8DB", highlightthickness=2)
        
        container.pack(fill="both", expand=True, padx=20, pady=20)
        #
        
        def fade_in(step=0):
            
            alp = step / 10
            if step <= 10:
                container.configure(highlightbackground=f"#{int(214 * (1-alp) + 245 * alp):02x}"
                                    f"{int(216 * (1-alp) + 247 * alp):02x}"
                                    f"{int(219 * (1-alp) + 250 * alp):02x}")
                self.root.after(50, fade_in, step + 1)
        
        self.root.after(0, fade_in)

        #
        tk.Label(container, text="🏆 CAMPEÃO!", font=self.font_title, bg=self.bg_color,fg=self.accent_color).pack(pady=20)
        #

        #
        tk.Label(container, text=f"Nome: {campeao.nome}", font=self.font_subtitle,bg=self.bg_color, fg=self.text_color).pack()
        #

        #
        tk.Label(container, text=f"Slogan: {campeao.slogan}", font=self.font_body,bg=self.bg_color, fg=self.label_color).pack()
        #

        #
        tk.Label(container, text=f"Ano de Fundação: {campeao.ano_fundacao}", font=self.font_body,bg=self.bg_color, 
                 fg=self.label_color).pack()
        #

        #
        tk.Label(container, text=f"Pontuação Final: {campeao.get_pontuacao()}", font=self.font_body,
                bg=self.bg_color, fg=self.label_color).pack()
        #
        
        btn_frame = tk.Frame(container, bg=self.bg_color)
        btn_frame.pack(pady=20)
        
        #
        btn_novo_torneio = tk.Button(btn_frame, text="Novo Torneio", font=self.font_body, bg=self.btn_secondary,
                                    fg="white", relief="flat", padx=20, pady=10, command=callback_novo_torneio)
        btn_novo_torneio.pack(side="left", padx=10)
        self.bind_hover(btn_novo_torneio, self.btn_secondary, self.btn_secondary_hover)
        #

        #
        btn_ver_relatorio = tk.Button(btn_frame, text="Ver Relatório", font=self.font_body, bg=self.btn_secondary,
                                      fg="white", relief="flat", padx=20, pady=10, command=callback_ver_relatorio)
        btn_ver_relatorio.pack(side="left", padx=10)
        self.bind_hover(btn_ver_relatorio, self.btn_secondary, self.btn_secondary_hover)
        #

        #
        btn_ver_historico = tk.Button(btn_frame, text="Ver Histórico", font=self.font_body, bg=self.btn_secondary,
                                      fg="white", relief="flat", padx=20, pady=10, command=callback_ver_historico)
        btn_ver_historico.pack(side="left", padx=10)
        self.bind_hover(btn_ver_historico, self.btn_secondary, self.btn_secondary_hover)
        #
#######      
    def mostrar_relatorio(self, startups_originias, callback_voltar):

        for widget in self.frame_relatorio.winfo_children():
            widget.destroy()
        
        #
        tk.Label(self.frame_relatorio, text="Relatório do Torneio", font=self.font_subtitle,bg=self.bg_color, 
                fg=self.text_color).pack(pady=20)
        #

        #
        text_frame = tk.Frame(self.frame_relatorio, bg="white", highlightbackground="#D6D8DB", highlightthickness=2)
        text_frame.pack(fill="both", expand=True, padx=20, pady=10)
        #

#
        headers = ["Nome", "Pontuação", "Pitches", "Bugs", "Trações", "Investidores Irritados", "Penalidades"]
#

#
        for col, header in enumerate(headers):
#         
            tk.Label(text_frame, text=header, font=self.font_body, bg="white", fg=self.text_color).grid(row=0, column=col, 
                    padx=5, pady=5, sticky="w")
#

        startups_ordenadas = sorted(startups_originias, key=lambda s: s.get_pontuacao(), reverse=True)

        #
        for row, startup in enumerate(startups_ordenadas, start=1):

            tk.Label(text_frame, text=startup.nome, font=self.font_body, bg="white", 
                     fg=self.label_color).grid(row=row, column=0, padx=5, pady=5, sticky="w")
            
            tk.Label(text_frame, text=str(startup.get_pontuacao()), font=self.font_body, bg="white", 
                     fg=self.label_color).grid(row=row, column=1, padx=5, pady=5, sticky="w")
            
            tk.Label(text_frame, text=str(startup.estatisticas.get("Pitch convincente", 0)), font=self.font_body, bg="white", 
                     fg=self.label_color).grid(row=row, column=2, padx=5, pady=5, sticky="w")
            
            tk.Label(text_frame, text=str(startup.estatisticas.get("Produto com bugs", 0)), font=self.font_body, bg="white",
                      fg=self.label_color).grid(row=row, column=3, padx=5, pady=5, sticky="w")
            
            tk.Label(text_frame, text=str(startup.estatisticas.get("Boa tração de usuários", 0)), font=self.font_body, bg="white",
                      fg=self.label_color).grid(row=row, column=4, padx=5, pady=5, sticky="w")
            
            tk.Label(text_frame, text=str(startup.estatisticas.get("Investidor irritado", 0)), font=self.font_body, bg="white",
                      fg=self.label_color).grid(row=row, column=5, padx=5, pady=5, sticky="w")
            
            tk.Label(text_frame, text=str(startup.estatisticas.get("Fake news no pitch", 0)), font=self.font_body, bg="white",
                      fg=self.label_color).grid(row=row, column=6, padx=5, pady=5, sticky="w")
        #

        #
        btn_voltar_relatorio = tk.Button(self.frame_relatorio, text="⬅️ Voltar ao Campeão", font=self.font_body,
                                        bg=self.btn_secondary, fg="white", relief="flat", padx=20, pady=10,command=callback_voltar)
        btn_voltar_relatorio.pack(pady=20)
        self.bind_hover(btn_voltar_relatorio, self.btn_secondary, self.btn_secondary_hover)
        #

#######       
    def mostrar_historico(self, historico_batalhas, callback_voltar_campeao, callback_voltar_batalhas):
       
        for widget in self.frame_historico.winfo_children():
            widget.destroy()
        
        #
        tk.Label(self.frame_historico, text="Histórico de Batalhas", font=self.font_subtitle,
                bg=self.bg_color, fg=self.text_color).pack(pady=20)
        #

        text_frame = tk.Frame(self.frame_historico, bg="white", highlightbackground="#D6D8DB", highlightthickness=2)
        text_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        text_area = tk.Text(text_frame, height=20, width=70, font=self.font_body, relief="flat")
        text_area.pack(pady=10, padx=10)
        
        for batalha_id, s1_nome, s2_nome, ganhador in historico_batalhas:
            entrada = f"🏆 Batalha {batalha_id}: {s1_nome} vs {s2_nome} - Vencedor: {ganhador}\n"
            text_area.insert(tk.END, entrada)
        
        text_area.config(state="disabled")
        
        btn_frame = tk.Frame(self.frame_historico, bg=self.bg_color)
        btn_frame.pack(pady=20)
        
        #
        btn_voltar_historico = tk.Button(btn_frame, text="⬅️ Voltar ao Campeão", font=self.font_body,
                                         bg=self.btn_secondary, fg="white", relief="flat", padx=20, pady=10,
                                         command=callback_voltar_campeao)
        btn_voltar_historico.pack(side="left", padx=10)
        self.bind_hover(btn_voltar_historico, self.btn_secondary, self.btn_secondary_hover)
        #

        #
        btn_voltar_batalhas_historico = tk.Button(btn_frame, text="⬅️ Voltar às Batalhas", font=self.font_body,
                                                 bg=self.btn_secondary, fg="white", relief="flat", padx=20, pady=10,
                                                 command=callback_voltar_batalhas)
        btn_voltar_batalhas_historico.pack(side="left", padx=10)
        self.bind_hover(btn_voltar_batalhas_historico, self.btn_secondary, self.btn_secondary_hover)
        #

######
    def bind_hover(self, widget, original_color, hover_color):
        widget.bind("<Enter>", lambda e: widget.config(bg=hover_color))
        widget.bind("<Leave>", lambda e: widget.config(bg=original_color))