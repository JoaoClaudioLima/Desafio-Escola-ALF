import sqlite3
from db_handling.metodo_corrige_prova import corrige_prova

def calcula_media(id_aluno):

	conn = sqlite3.connect('db/resposta.db')
	cursor = conn.cursor()

	confere_provas = cursor.execute('SELECT count(id) FROM resposta')

	if confere_provas != 0:
		Provas = cursor.execute('SELECT id_prova FROM resposta WHERE id_aluno = ?', id_aluno).fetchall()
		n_provas = len(Provas)
		media = 0.0
		for i in range(n_provas):
			media += float(corrige_prova(id_aluno,str(Provas[i][0])))
		
		calculo_media = media/n_provas
		return calculo_media	
	else:
		return 'A database de respostas está vazia.'