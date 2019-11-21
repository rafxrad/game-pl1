class interface:
	"""docstring for """

	lista = []

	def __init__(self):
		pass

	def getListaDeNomes(self):
		#ler arquivos do arquivo de nomes e salva na lista
		arq = open('nomes.txt','r')

		for i in arq:
			self.lista.append(i)

		arq.close()

	def exibirNomes(self):
		#retorna uma string para ser exibida numa massegebox
		listaNomes = ''

		#limpa a lista e adicionar o ranking atualizado
		self.lista.clear()
		self.getListaDeNomes()

		listaTuplas = []
		guardaPosicao = 0
		numeros = ''
		nomeJogador = ''

		for i in self.lista:
			for pos,j in enumerate(i):
				if j == ' ':
					guardaPosicao = pos
					break
								
			for k in range(0,guardaPosicao):
				numeros += i[k]

			for letra in range(guardaPosicao+1, len(i)):
				nomeJogador += i[letra]
				
			listaTuplas.append((float(numeros),nomeJogador))

			guardaPosicao = 0
			numeros = ''	
			nomeJogador = ''	

		#ordena a lista de forma descrescente
		novaLista = sorted(listaTuplas, reverse=True)

		for pos,i in enumerate(novaLista):
			if pos < 10:
				listaNomes += '{}° - {}    \n      {}\n\n'.format(pos+1, i[1].replace('\n',''), i[0])

		return listaNomes

	def setNome(self,nome):
		#armazena um nome temporario para ser utilizado por jogoMiInterface
	 	arq = open('nomeTemp.txt','w')
	 	arq.write(nome)
	 	arq.close()

	def setRanking(self,nome,pontos):
		#adicionando os pontos de um novo usuario
		arq = open('nomes.txt','a')
		arq.write('{} {}\n'.format(pontos,nome))
		arq.close()
                
	def verificaNome(self, nome):
		#verifica se o nome existe, caso contrário salva
		status = False

		arq = open('nomes.txt','r')

		for i in arq:
			if nome in i:
				status = True
				break

		arq.close()
		return status

	def verificaPlayerTop(self):
		#retorna o player top 1
		self.exibirNomes()
		return self.lista[0]
		
