import sqlite3

def corrige_prova(id_aluno, id_prova):
	conn_resposta = sqlite3.connect('db/resposta.db')
	cursor_resposta = conn_resposta.cursor()

	conn_gabarito = sqlite3.connect('db/gabarito.db')
	cursor_gabarito = conn_gabarito.cursor()


	confere_pesos = cursor_gabarito.execute('SELECT count(peso) FROM gabarito')



	if confere_pesos != 0:
		Respostas = cursor_resposta.execute('SELECT resposta FROM resposta WHERE id_aluno = ? AND id_prova = ?', (id_aluno, id_prova)).fetchone()

		Gabaritos = cursor_gabarito.execute('SELECT gabarito FROM gabarito WHERE id_prova = ?', id_prova).fetchone()
		Pesos = cursor_gabarito.execute('SELECT peso FROM gabarito WHERE id_prova = ?', id_prova).fetchone()
		nota=0
		peso=0
		for i in range(len(Respostas[0])):
			peso+= int(Pesos[0][i])
			if Respostas[0][i] == Gabaritos[0][i]:
				nota+=1*int(Pesos[0][i])
			
		nota_ponderada=nota/peso
		return nota_ponderada	

	else:
		return 'A base de dados está vazia.'
