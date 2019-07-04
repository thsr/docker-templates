from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(host="postgres", user="user", password="pass", database="db")

@app.route('/createtable')
def createtable():
    with conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, num integer, data varchar);")
    return jsonify("ok")

@app.route('/insert')
def insert():
    with conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (999, "foo", ))
            cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (747, "bar", ))
    return jsonify("ok")

@app.route('/select')
def select():
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM test;")
            res = cur.fetchall()
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)