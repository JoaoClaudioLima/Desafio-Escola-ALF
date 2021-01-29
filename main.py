import flask
from flask import request, jsonify
import sqlite3
from sqlite3 import Error
from db_handling.metodo_cria_conexão import create_connection
from db_handling.metodo_cadastro_aluno import create_aluno
from db_handling.metodo_cadastro_resposta import create_resposta
from db_handling.metodo_cadastro_gabarito import create_gabarito
from db_handling.metodo_corrige_prova import corrige_prova
from db_handling.metodo_calcula_media import calcula_media

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

#Retorna o database 'nome_aluno.db' em caso do request.method ser um GET. Caso seja um POST, inclui na database de respostas.
@app.route('/aluno_cadastro', methods=['GET', 'POST'])
def api_aluno_database():
    if request.method == 'GET':
        database = 'db/nome_aluno.db'
        conn = create_connection(database)
        conn.row_factory = dict_factory
        cur = conn.cursor()
        sql = 'SELECT * FROM nome_aluno;'
        alunos_database = cur.execute(sql).fetchall()

        return jsonify(alunos_database)

    elif request.method == 'POST':
        if request.args['nome']!="":
            database = 'db/nome_aluno.db'
            conn = create_connection(database)
            conn.row_factory = dict_factory
            create_aluno(conn)
        
            return 'Aluno(a) %s cadastrado(a) com sucesso.' %request.args['nome'], 201
        else: 
            return 'Cadastro do aluno(a) falhou. Nome do(a) aluno(a) não informado.', 400

#Retorna o database 'resposta.db' em caso do request.method ser um GET. Caso seja um POST, inclui na database de respostas.
@app.route('/respostas', methods=['GET', 'POST'])
def api_respostas_database():
    if request.method == 'GET':
        database = 'db/resposta.db'
        conn = create_connection(database)
        conn.row_factory = dict_factory
        cur = conn.cursor()
        sql = 'SELECT * FROM resposta;'
        resposta_database = cur.execute(sql).fetchall()

        return jsonify(resposta_database)
        
    elif request.method == 'POST':
        if request.args['id_prova']!="" and request.args['id_aluno']!="" and request.args['resposta']!="":
            database = 'db/resposta.db'
            conn = create_connection(database)
            conn.row_factory = dict_factory
            create_resposta(conn)
            
            return 'Respostas da prova de ID: %s do aluno(a) de ID: %s cadastradas com sucesso.' %(request.args['id_prova'], request.args['id_aluno']), 201
        else:
            return 'Cadastro da resposta falhou. Alguma das informações não foi fornecida.', 400

#Retorna o database 'gabarito.db' em caso do request.method ser um GET. Caso seja um POST, inclui na database de respostas.
@app.route('/gabarito', methods=['GET', 'POST'])
def api_gabarito_database():
    if request.method == 'GET':
        database = 'db/gabarito.db'
        conn = create_connection(database)
        conn.row_factory = dict_factory
        cur = conn.cursor()
        sql = 'SELECT * FROM gabarito;'
        gabarito_database = cur.execute(sql).fetchall()

        return jsonify(gabarito_database)

    elif request.method == 'POST':
        pesos = list(request.args['peso'])
        gabaritos = list(request.args['gabarito'])
        if len(pesos)!=len(gabaritos):
            return 'Cadastro do gabarito falhou. Cada gabarito deve ter um peso e o peso deve ser um valor inteiro menor que 10.', 400
        else:
            if request.args['id_prova']!="" and request.args['gabarito']!="" and request.args['peso']!="":
                database = 'db/gabarito.db'
                conn = create_connection(database)
                conn.row_factory = dict_factory
                create_gabarito(conn)
                        
                return ('Gabarito da prova de ID: %s cadastrado com sucesso.' %request.args['id_prova']), 201

#Calcula a média de cada aluno e retorna os alunos aprovados.
@app.route('/aprovados', methods=['GET'])
def api_aprovados():
	database = 'db/nome_aluno.db'
	conn = create_connection(database)
	#conn.row_factory = dict_factory
	cursor = conn.cursor()

	id_alunos = cursor.execute('SELECT id FROM nome_aluno').fetchall()
	alunos_aprovados = []
	nome_aprovados = []

	for aluno in id_alunos:
		if calcula_media(str(aluno[0]))>=0.7:
			alunos_aprovados.append(aluno[0])


	for aluno in alunos_aprovados:
		aprovados = cursor.execute('SELECT nome FROM nome_aluno WHERE id = ?', str(aluno)).fetchall()
		nome_aprovados.append(aprovados)

	return jsonify(nome_aprovados)

#Erro
@app.errorhandler(404)
def page_not_found(e):
	return "<h1>404</h1><p>Página não encontrada.</p>", 404

app.run()