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
        try:
            with open('database.pickle', 'rb') as u:
                self.cadastro = pickle.load(u)
        except:
            self.cadastro = {}
            
        self.window = tk.Tk()
        self.window.geometry("300x300")
        self.window.rowconfigure(0, minsize=300)
        self.window.columnconfigure(0, minsize=300)
        
        self.tela_login = Tela_Login(self)
        self.tela_entrar = Tela_Entrar(self)
        self.tela_cadastro = Tela_Cadastro(self)
        self.tela_DarCarona_PedirCarona = Tela_DarCarona_PedirCarona(self)
        self.tela_oferecer_carona = Tela_OferecerCarona(self)
        self.tela_procura_carona = Tela_Procura_Carona(self)
        self.tela_final = Tela_Final(self)
        self.Tela_Final2 = Tela_Final2(self)
            
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
    
    def mostra_tela_Oferecer_Carona(self):
        self.tela_oferecer_carona.mostra()

    def mostra_tela_Procura_Carona(self):
        self.tela_procura_carona.mostra()
        
    def mostra_tela_Final(self):
        self.tela_final.mostra()
        
    def mostra_Tela_Final2(self):
        self.Tela_Final2.mostra()


class Tela_Login:
    def __init__(self, app):
        self.app = app

        try:
            with open('database.pickle', 'rb') as u:
                self.cadastro = pickle.load(u)
        except:
            self.cadastro = {}
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

        try:        
            with open('database.pickle', 'rb') as u:
                self.cadastro = pickle.load(u)
        except:
            self.cadastro = {}
        
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
                self.app.usuario = nome
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
        self.app.mostra_tela_Oferecer_Carona()
        
    def botao_pedir_carona_clicado(self):
        self.app.mostra_tela_Procura_Carona()
        
    def mostra(self):
        self.Tela_DarCarona_PedirCarona.tkraise()
        
        
## TELA ENDEREÇO DA OPÇÃO DAR CARONA
        

class Tela_OferecerCarona:
    def __init__(self, app):
        self.app=app
        self.Tela_OferecerCarona =tk.Frame(self.app.window)
        self.Tela_OferecerCarona.rowconfigure(0, minsize=50)
        self.Tela_OferecerCarona.rowconfigure(1, minsize=50)
        self.Tela_OferecerCarona.rowconfigure(2, minsize=50)
        self.Tela_OferecerCarona.rowconfigure(3, minsize=50)
        self.Tela_OferecerCarona.rowconfigure(4, minsize=50)
        self.Tela_OferecerCarona.rowconfigure(5, minsize=50)
        self.Tela_OferecerCarona.columnconfigure(0, minsize=100)
        self.Tela_OferecerCarona.columnconfigure(1, minsize=200)
        self.Tela_OferecerCarona.grid(row=0, column=0, sticky="nsew")
        
        label_Bairro1 = tk.Label(self.Tela_OferecerCarona)
        label_Bairro1.configure(text="Bairro :", fg='darkblue', font=('Arial','9'))
        label_Bairro1.grid(row=2, column=0, sticky="nsew")
        
        self.Bairro1 = tk.Entry(self.Tela_OferecerCarona)
        self.Bairro1.grid(row=2, column=1, padx=20, sticky="ew")
        
        label_Horario1 = tk.Label(self.Tela_OferecerCarona)
        label_Horario1.configure(text="Horario :", fg='darkblue', font=('Arial','9'))
        label_Horario1.grid(row=3, column=0, sticky="nsew")
        
        self.Horario1 = tk.Entry(self.Tela_OferecerCarona)
        self.Horario1.grid(row=3, column=1, padx=20, sticky="ew")
        
        fonte1=('Arial','10')
        botao_oferecer_carona = tk.Button(self.Tela_OferecerCarona)
        botao_oferecer_carona.configure(text="Oferecer carona", width=10, font=fonte1)
        botao_oferecer_carona.configure(command=self.botao_oferecer_carona_clicado)
        botao_oferecer_carona.grid(row=4, column=1, sticky="nsew")
        
        
    def botao_oferecer_carona_clicado(self):
        bairro1 = self.Bairro1.get()
        horario1 = self.Horario1.get()
        dados_cadastrais = self.app.cadastro[self.app.usuario][:3]
        self.app.cadastro[self.app.usuario] = dados_cadastrais + (bairro1, horario1)
        with open('database.pickle', 'wb') as u:
            pickle.dump(self.app.cadastro, u)
        print('Carona Oferecida')            
        self.app.mostra_Tela_Final2()
            
    def mostra(self):
        self.Tela_OferecerCarona.tkraise()
                
                
## TELA PROCURA CARONA
        
class Tela_Procura_Carona:
    def __init__(self, app):
        self.app = app
         
        self.tela_procura_carona = tk.Frame(self.app.window)
        self.tela_procura_carona.rowconfigure(0, minsize=50)
        self.tela_procura_carona.rowconfigure(1, minsize=50)
        self.tela_procura_carona.rowconfigure(2, minsize=50)
        self.tela_procura_carona.rowconfigure(3, minsize=50)
        self.tela_procura_carona.rowconfigure(4, minsize=50)
        self.tela_procura_carona.rowconfigure(5, minsize=50)
        self.tela_procura_carona.columnconfigure(0, minsize=100)
        self.tela_procura_carona.columnconfigure(1, minsize=200)
        self.tela_procura_carona.grid(row=0, column=0, sticky="nsew")
         
         
        label_Destino = tk.Label(self.tela_procura_carona)
        label_Destino.configure(text="Destino :", fg='darkblue', font=('Arial','9'))
        label_Destino.grid(row=1, column=0, sticky="nsew")
         
        self.destino = tk.Entry(self.tela_procura_carona)
        self.destino.grid(row=1, column=1, padx=20, sticky="ew")
         
        label_Horario = tk.Label(self.tela_procura_carona)
        label_Horario.configure(text="Horario:", fg='darkblue', font=('Arial','9'))
        label_Horario.grid(row=2, column=0, sticky="nsew")
         
        self.horario = tk.Entry(self.tela_procura_carona)
        self.horario.grid(row=2, column=1, padx=20, sticky="ew")
         
        fonte2=('Arial','10')
        botao_procurar = tk.Button(self.tela_procura_carona)
        botao_procurar.configure(text="Procurar ofertas", width=10, font=fonte2)
        botao_procurar.configure(command=self.botao_procurar_clicado)
        botao_procurar.grid(row=4, column=1, sticky="nsew")      
         
    def botao_procurar_clicado(self):
#        local=[]
        destino = self.destino.get()
        horario = self.horario.get()
#        local.append(destino)
#        local.append(horario)
        with open('database.pickle', 'rb') as u:
            x = pickle.load(u)
            if destino in x :
                print('encontrou destino')
                for pessoa in u:
                    self.app.cadastro[self.app.usuario] = self.app.motorista
                    self.app.cadastro[self.app.usuario][1] = self.app.contato
                print("tem carona!")
                self.app.mostra_tela_Final()
            else:
                print("sem caronas!")
        
    def mostra(self):
        self.tela_procura_carona.tkraise()
        
## TELA FINAL
        
class Tela_Final:
    
    def __init__(self, app):
        self.app = app
        self.tela_final = tk.Frame(self.app.window)
        self.tela_final.rowconfigure(0, minsize=300)
        self.tela_final.columnconfigure(0, minsize=300)
        self.tela_final.grid(row=0, column=0, sticky="nsew")
        
        
        texto = tk.Label(self.tela_final)
        texto.configure(text='self.app.Tela_Procura_Carona.motorista ,self.app.Tela_Procura_Carona.contato ', fg='black', font=('Arial', '9') )
        texto.grid(row=0, column=0, sticky="nsew")
        
    def mostra(self):
        self.tela_final.tkraise()
        

class Tela_Final2:
    
    def __init__(self, app):
        self.app = app
        self.Tela_Final2 = tk.Frame(self.app.window)
        self.Tela_Final2.rowconfigure(0, minsize=300)
        self.Tela_Final2.columnconfigure(0, minsize=300)
        self.Tela_Final2.grid(row=0, column=0, sticky="nsew")
        
        texto = tk.Label(self.Tela_Final2)
        texto.configure(text='O passageiro entrará em contato', fg='black', font=('Arial', '14') )
        texto.grid(row=0, column=0, sticky="nsew")
        
        
        
    def mostra(self):
        self.Tela_Final2.tkraise()
    
app = AplicativoCarona()
app.iniciar()