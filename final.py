# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 10:10:02 2016

@author: Bruno
"""


import pickle
import tkinter as tk


## TELA INICIAL

class AplicativoCarona:
    def __init__(self):        
        self.cadastro = {}
        
        self.window = tk.Tk()
        self.window.geometry("300x300")
        self.window.rowconfigure(0, minsize=300)
        self.window.columnconfigure(0, minsize=300)
        
        self.tela_login = Tela_Login(self)
        self.tela_entrar = Tela_Entrar(self)
        self.tela_cadastro = Tela_Cadastro(self)
        self.tela_DarCarona_PedirCarona = Tela_DarCarona_PedirCarona(self)
        self.tela_procura_carona = Tela_Procura_Carona(self)
        with open('database.pickle', 'rb') as u:
            self.cadastro = pickle.load(u)
        self.mostra_tela_login()

    def iniciar(self):
        self.window.mainloop()
        
    def mostra_tela_login(self):
        print(self.cadastro)
        self.tela_login.mostra()

    def mostra_tela_entrar(self):
        self.tela_entrar.mostra()

    def mostra_tela_cadastro(self):
        self.tela_cadastro.mostra()
        
    def mostra_tela_DarCarona_PedirCarona(self):
        self.tela_DarCarona_PedirCarona.mostra()
    
    def mostra_tela_Procura_Carona(self):
        self.tela_procura_carona.mostra()


class Tela_Login:
    def __init__(self, app):
        self.app = app

        
        self.tela_login = tk.Frame(self.app.window)
        self.tela_login.rowconfigure(0, minsize=75)
        self.tela_login.rowconfigure(1, minsize=50)
        self.tela_login.rowconfigure(2, minsize=50)
        self.tela_login.rowconfigure(3, minsize=50)
        self.tela_login.rowconfigure(4, minsize=75)
        self.tela_login.columnconfigure(0, minsize=300)
        self.tela_login.grid(row=0, column=0, sticky="nsew")
        
        label_carona = tk.Label(self.tela_login)
        label_carona.configure(text="Carona", fg='darkorange', font=('Arial','16', 'bold'))
        label_carona.grid(row=1, column=0, sticky="nsew")
        
        botao_entrar = tk.Button(self.tela_login)
        botao_entrar.configure(text="Entrar")
        botao_entrar.configure(command=self.botao_entrar_clicado)
        botao_entrar.grid(row=2, column=0, sticky="nsew")
        
        botao_cadastrar = tk.Button(self.tela_login)
        botao_cadastrar.configure(text='Cadastrar')
        botao_cadastrar.configure(command=self.botao_cadastrar_clicado)
        botao_cadastrar.grid(row=3, column=0, sticky="nsew")
        
    def botao_entrar_clicado(self):
        self.app.mostra_tela_entrar()
        
    def botao_cadastrar_clicado(self):
        self.app.mostra_tela_cadastro()
        
    def mostra(self):
        self.tela_login.tkraise()
        


## TELA ENTRAR


class Tela_Entrar:
    def __init__(self, app):
        self.app = app
        
        with open('database.pickle', 'rb') as u:
            self.cadastro = pickle.load(u)
        
        self.tela_entrar = tk.Frame(self.app.window)
        self.tela_entrar.rowconfigure(0, minsize=50)
        self.tela_entrar.rowconfigure(1, minsize=75)
        self.tela_entrar.rowconfigure(2, minsize=75)
        self.tela_entrar.rowconfigure(3, minsize=50)
        self.tela_entrar.rowconfigure(4, minsize=50)
        self.tela_entrar.columnconfigure(0, minsize=25)
        self.tela_entrar.columnconfigure(1, minsize=100)
        self.tela_entrar.columnconfigure(2, minsize=175)
        self.tela_entrar.grid(row=0, column=0, sticky="nsew")
        
        label_nome1 = tk.Label(self.tela_entrar)
        label_nome1.configure(text="Nome :", fg='darkblue', font=('Arial','9'))
        label_nome1.grid(row=1, column=1, sticky="nsew")
        
        self.nome1 = tk.Entry(self.tela_entrar)
        self.nome1.grid(row=1, column=2, padx=20, sticky="ew")
    
        label_senha1 = tk.Label(self.tela_entrar)
        label_senha1.configure(text='Senha :', fg='darkblue', font=('Arial','9'))
        label_senha1.grid(row=2, column=1, sticky="nsew")
        
        self.senha1 = tk.Entry(self.tela_entrar)
        self.senha1.grid(row=2, column=2, padx=20, sticky="ew")                
        
        fonte1=('Arial','10')
        botao_entrada = tk.Button(self.tela_entrar)
        botao_entrada.configure(text="Entrar", width=10, font=fonte1)
        botao_entrada.configure(command=self.botao_entrando_clicado)
        botao_entrada.grid(row=3, column=2, sticky="nsew")
        
    def botao_entrando_clicado(self):
        nome = self.nome1.get()        
        if nome in self.cadastro:
            print("achei o usuario")
            senha = self.senha1.get()            
            if senha == self.cadastro[nome][0] :
                print("achei a senha")
                self.app.mostra_tela_DarCarona_PedirCarona()
        else:
             print("Cadastro inexistente")
             
        
    def mostra(self):
        self.tela_entrar.tkraise()
    

    
## TELA CADASTRO        


class Tela_Cadastro:
    def __init__(self, app):
        self.app = app
        
        self.tela_cadastrar = tk.Frame(self.app.window)
        self.tela_cadastrar.rowconfigure(0, minsize=50)
        self.tela_cadastrar.rowconfigure(1, minsize=50)
        self.tela_cadastrar.rowconfigure(2, minsize=50)
        self.tela_cadastrar.rowconfigure(3, minsize=50)
        self.tela_cadastrar.rowconfigure(4, minsize=50)
        self.tela_cadastrar.rowconfigure(5, minsize=50)
        self.tela_cadastrar.columnconfigure(0, minsize=100)
        self.tela_cadastrar.columnconfigure(1, minsize=200)
        self.tela_cadastrar.grid(row=0, column=0, sticky="nsew")
        
        label_nome = tk.Label(self.tela_cadastrar)
        label_nome.configure(text="Nome :", fg='darkblue', font=('Arial','9'))
        label_nome.grid(row=0, column=0, sticky="nsew")
        
        self.nome = tk.Entry(self.tela_cadastrar)
        self.nome.grid(row=0, column=1, padx=20, sticky="ew")
                
        
        label_Celular = tk.Label(self.tela_cadastrar)
        label_Celular.configure(text="Celular :", fg='darkblue', font=('Arial','9'))
        label_Celular.grid(row=1, column=0, sticky="nsew")

        self.celular = tk.Entry(self.tela_cadastrar)
        self.celular.grid(row=1, column=1, padx=20, sticky="ew")
        
        label_email = tk.Label(self.tela_cadastrar)
        label_email.configure(text="Email :", fg='darkblue', font=('Arial','9'))
        label_email.grid(row=2, column=0, sticky="nsew")

        self.email = tk.Entry(self.tela_cadastrar)
        self.email.grid(row=2, column=1, padx=20, sticky="ew")
        
        label_senha = tk.Label(self.tela_cadastrar)
        label_senha.configure(text="Senha :", fg='darkblue', font=('Arial','9'))
        label_senha.grid(row=3, column=0, sticky="nsew")

        self.senha = tk.Entry(self.tela_cadastrar)
        self.senha.grid(row=3, column=1, padx=20, sticky="ew")
        
        fonte1=('Arial','10')
        botao_cadastro = tk.Button(self.tela_cadastrar)
        botao_cadastro.configure(text="Efetuar cadastro", width=10, font=fonte1)
        botao_cadastro.configure(command=self.botao_cadastro_clicado)
        botao_cadastro.grid(row=4, column=1, sticky="nsew")

    def botao_cadastro_clicado(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        celular = self.celular.get()
        email = self.email.get()
        
        self.app.cadastro[usuario] = (senha, celular, email)
        with open('database.pickle', 'wb') as u:
            pickle.dump(self.app.cadastro, u)
        self.app.mostra_tela_login()
            
    def mostra(self):
        self.tela_cadastrar.tkraise()
       

# TELA DAR CARONA - PEDIR CARONA

class Tela_DarCarona_PedirCarona:
    def __init__(self, app):
        self.app = app
        
        self.Tela_DarCarona_PedirCarona = tk.Frame(self.app.window)
        self.Tela_DarCarona_PedirCarona.rowconfigure(0, minsize=75)
        self.Tela_DarCarona_PedirCarona.rowconfigure(1, minsize=50)
        self.Tela_DarCarona_PedirCarona.rowconfigure(2, minsize=50)
        self.Tela_DarCarona_PedirCarona.rowconfigure(3, minsize=50)
        self.Tela_DarCarona_PedirCarona.rowconfigure(4, minsize=75)
        self.Tela_DarCarona_PedirCarona.columnconfigure(0, minsize=300)
        self.Tela_DarCarona_PedirCarona.grid(row=0, column=0, sticky="nsew")
              
        botao_dar_carona = tk.Button(self.Tela_DarCarona_PedirCarona)
        botao_dar_carona.configure(text="Oferecer Carona")
        botao_dar_carona.configure(command=self.botao_dar_carona_clicado)
        botao_dar_carona.grid(row=2, column=0, sticky="nsew")
        
        botao_pedir_carona = tk.Button(self.Tela_DarCarona_PedirCarona)
        botao_pedir_carona.configure(text='Pedir Carona')
        botao_pedir_carona.configure(command=self.botao_pedir_carona_clicado)
        botao_pedir_carona.grid(row=3, column=0, sticky="nsew")
        
    def botao_dar_carona_clicado(self):
        self.app.mostra_DarCarona_PedirCarona()
        
    def botao_pedir_carona_clicado(self):
        self.app.mostra_Tela_Procura_Carona()
        
    def mostra(self):
        self.Tela_DarCarona_PedirCarona.tkraise()
        
        


app = AplicativoCarona()
app.iniciar()