import sqlite3

#Cria as databases que serão manipuladas pela main.

conn = sqlite3.connect('nome_aluno.db')
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS nome_aluno (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		nome TEXT NOT NULL
);
""")

conn = sqlite3.connect('resposta.db')
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS resposta (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		id_aluno INTEGER NOT NULL,
		id_prova INTEGER NOT NULL,
		resposta TEXT,
		FOREIGN KEY (id_aluno) REFERENCES nome_aluno(id)
);
""")

conn = sqlite3.connect('gabarito.db')
cursor = conn.cursor()


cursor.execute("""

CREATE TABLE IF NOT EXISTS gabarito (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		id_prova INTEGER NOT NULL,
		peso TEXT,
		gabarito TEXT,
		FOREIGN KEY(id_prova) REFERENCES resposta(id_prova)
);
""")

conn.close