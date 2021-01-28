import sqlite3
import flask
from flask import request, jsonify

#Cria uma nova entrada na database 'nome_aluno.db'.
def create_aluno(conn):
	nome = request.args['nome']
	sql = 'INSERT INTO nome_aluno(nome) VALUES (?)'
	cur = conn.cursor()
	cur.execute(sql, [nome])
	conn.commit()
	return cur.lastrowid