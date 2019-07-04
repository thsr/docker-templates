from flask import Flask, jsonify
from py2neo import Graph

app = Flask(__name__)

conn = psycopg2.connect(host="postgres", user="user", password="pass", database="db")

@app.route('/initdb')
def initdb():
    with conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
            cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def", ))
            return jsonify("ok")

@app.route('/query')
def query():
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM test;")
            res = cur.fetchall()
            return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)