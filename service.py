import psycopg2
from flask import request, jsonify

user = 'postgres'
password = 'postgres'
host = 'localhost'
port = 5432
database = 'Books'  

def Database_Connection():
    conn = psycopg2.connect(database="Books", user='postgres',
        password='postgres', host='localhost', port='5432')
    return conn

def create_table():
    conn = Database_Connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS books (Id SERIAL PRIMARY KEY, Name TEXT, Author TEXT, Available BOOLEAN)')
    conn.commit()
    conn.close()

    return conn


def View():
    
    conn = Database_Connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books')
    rows = cur.fetchall()
    conn.close()

    book_list = []

    # for row in rows :
    #     row=dict(row)
    #     print('dict response, ',row)
    #     book_list.append(row)

    for row in rows:
        dict_data={}
        for i,col in enumerate(cur.description):
            dict_data[col[0]]=row[i]
        book_list.append(dict_data)  

    return jsonify({'book_list':book_list})

def Insert():
    data = request.get_json()

    conn = Database_Connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO books (Id,Name, Author, Available) VALUES (%s,%s, %s, %s)',
                (data['id'],data['name'], data['author'], data['available']))
    conn.commit()
    conn.close()

    return jsonify({'message':'data added sucessfully'})

def Update():
    data = request.get_json()

    conn = Database_Connection()
    cur = conn.cursor()
    cur.execute('UPDATE books SET Name=%s  WHERE Id=%s',
                (data['name'],data['id']))
    conn.commit()
    conn.close()

    return jsonify({'message':'data updated sucessfully'})

def Delete():
    data=request.get_json()
    conn =Database_Connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM books WHERE Id = %s',(data['id']))  
    conn.commit()
    conn.close()

    return jsonify({'message':'data deleted sucessfully'})

