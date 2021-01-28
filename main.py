import flask
from flask import request, jsonify
import sqlite3
from sqlite3 import Error
from db_handling.metodo_cria_conexão import create_connection

#Retorna itens da database como dicionários.
def dict_factory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Home.
@app.route('/', methods=['GET'])
def home():
    return "<h1>Desafio Escola Alf</h1><p>Este site é um protótipo para graduar notas de alunos da escola Alf</p>"

#Retorna o database 'nome_aluno.db'.
@app.route('/aluno_cadastro', methods=['GET'])
def api_aluno_database():
	database = 'db/nome_aluno.db'
	conn = create_connection(database)
	conn.row_factory = dict_factory
	cur = conn.cursor()
	sql = 'SELECT * FROM nome_aluno;'
	alunos_database = cur.execute(sql).fetchall()

	return jsonify(alunos_database)


#Retorna o database 'resposta.db'.
@app.route('/respostas', methods=['GET'])
def api_respostas_database():
    database = 'db/resposta.db'
    conn = create_connection(database)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    sql = 'SELECT * FROM resposta;'
    resposta_database = cur.execute(sql).fetchall()

    return jsonify(resposta_database)

#Retorna o database 'gabarito.db'.
@app.route('/gabarito', methods=['GET'])
def api_gabarito_database():
	database = 'db/gabarito.db'
	conn = create_connection(database)
	conn.row_factory = dict_factory
	cur = conn.cursor()
	sql = 'SELECT * FROM gabarito;'
	gabarito_database = cur.execute(sql).fetchall()

	return jsonify(gabarito_database)

#Erro
@app.errorhandler(404)
def page_not_found(e):
	return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()