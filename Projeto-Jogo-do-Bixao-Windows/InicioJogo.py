from tkinter import *
from tkinter import messagebox
from random import randint
from interfaceConexao import *
#from interfacePictureImage import *
import os

janela = Tk()
janela.geometry('400x400')
janela.title('Cadastro de Player')
janela['bg'] = '#4F4F4F'

lista = []

#criar um objeto do tipo picture
#imagem = picture()

#objeto do tipo interface
inter = interface()

def listaDeNomes():
	inter.getListaDeNomes()

def exibirListaNomes():
    #Exibe a lista de Nomes
	messagebox.showinfo('RANKING',inter.exibirNomes())

def getTexto():
	nome = tbNomeNovo.get().upper()

	if inter.verificaNome(nome):
		messagebox.showinfo('','Nome já Existe !')

	#Verifica se o nome existe e garante que o USER só possa clicar uma vez por execução	
	elif inter.verificaNome(nome) == False:
		#salvar o nome caso não exista
		salvarNovoNome(nome)

		messagebox.showinfo('','Bem Vindo ao Jogo {}!'.format(nome))
		os.system('call jogoMiInterface.py')

		if messagebox.askquestion('','Deseja Continuar?') == 'no':
			janela.destroy()

		else:
			#apaga todo o texto do textBox
			tbNomeNovo.delete(0, last=END)
		
def salvarNovoNome(nome):
	inter.setNome(nome)


#Label de Cadastro
lblJogo = Label(text='JOGO DO BIXÃO', font='Courier 26 bold', fg = 'yellow', bg ='#4F4F4F')
lblJogo.place(x=75,y=70)

#Label de Usuario
lblNome = Label(text='Nick de Jogador:', font='Courier 10 bold', bg = '#4F4F4F', fg='white')
lblNome.place(x=110,y=150)

#janela nome
tbNomeNovo = Entry(janela, font='Courier 12', fg='yellow', background='black')
tbNomeNovo.place(x=110,y=170)

#adicionar usuario
btAdicionar = Button(text='Iniciar Jogo', command=getTexto, background='black', font='Courier 12 bold', fg='white')
btAdicionar.place(x=150,y=220)

btVerRank = Button(text='Ver Ranking', command=exibirListaNomes, font='Courier 12 bold', background='black', fg='white')
btVerRank.place(x=240,y=350)

#btVerRank = Button(text='Tirar Foto', command=lambda: imagem.capturaExibe(), font='Courier 12 bold', background='black', fg='white')
#btVerRank.place(x=20,y=350)

#exibirListaNomes()
janela.mainloop()
