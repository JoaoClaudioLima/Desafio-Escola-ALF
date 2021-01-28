import sqlite3
import flask
from flask import request, jsonify

#Cria uma nova entrada na database 'resposta.db'.
def create_resposta(conn):
	id_prova = request.args['id_prova']
	id_aluno = request.args['id_aluno']
	resposta = request.args['resposta']
	sql = 'INSERT INTO resposta(id_aluno,id_prova,resposta) VALUES (?,?,?)'
	cur = conn.cursor()
	cur.execute(sql, ([id_aluno, id_prova, resposta]))
	conn.commit()
	return cur.lastrowid
