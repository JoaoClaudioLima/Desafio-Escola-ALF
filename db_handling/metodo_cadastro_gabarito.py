import sqlite3
import flask
from flask import request, jsonify

#Cria uma nova entrada na database 'gabarito.db'.
def create_gabarito(conn):
	id_prova = request.args['id_prova']
	peso = request.args['peso']
	gabarito = request.args['gabarito']
	sql = 'INSERT INTO gabarito(id_prova,peso, gabarito) VALUES (?,?,?)'
	cur = conn.cursor()
	cur.execute(sql, ([id_prova, peso, gabarito]))
	conn.commit()
	return cur.lastrowid