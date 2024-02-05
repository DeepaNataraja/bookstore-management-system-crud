import psycopg2
from flask import jsonify


def Database_Connection():
    try:
        conn = psycopg2.connect(database="Books", user='postgres',
            password='postgres', host='localhost', port='5432')
        return conn
    
    except Exception as e:
        print(e)
        raise 
def create_table():
    try:
        conn = Database_Connection()
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS books (Id SERIAL PRIMARY KEY, Name TEXT, Author TEXT, Available BOOLEAN)')
        conn.commit()
        return conn
    
    except Exception as e:
        print(e)

    finally:
        conn.close()

def View(table_name,context):

    try:
        conn = Database_Connection()
        cur = conn.cursor()

        string_query = f'SELECT * FROM {table_name}'
        conditions= f' WHERE '  

        if (type(context) == dict and len(context.keys())>0):
            print(context)
            condition_list=[]
            for key in context.keys():
                condition_list.append(f"{key}='{context[key]}'")
            conditions+=' AND '.join(condition_list)
            print('Condition Query ',conditions)
            string_query += conditions

        cur.execute(string_query,tuple(context.values()))
        rows = cur.fetchall() 
        
        result = []
        for row in rows:
            d = {}
            for i, col in enumerate(cur.description):
                d[col[0]] = row[i]
            result.append(d)
            print(result)

            return result
            
    except Exception as e:
        print(e)
        raise

    finally:
        conn.commit()
        conn.close()

def Delete(table_name,context):
    try:
        conn =Database_Connection()
        cur = conn.cursor()

        string_query = f'DELETE FROM {table_name}'
        conditions= f' WHERE '  

        if (type(context) == dict and len(context.keys())>0):
            print(context)
            condition_list=[]
            for key in context.keys():
                condition_list.append(f"{key}='{context[key]}'")
            conditions+=' AND '.join(condition_list)
            print('Condition Query ',conditions)
            string_query += conditions

            cur.execute(string_query,tuple(context.values()))

            return {'message':'data deleted sucessfully'}
    
    except Exception as e:
        print(e)
        return jsonify({'error': 'An error occurred during deletion'})

    finally:
        conn.commit()
        conn.close()

def Update(table_name,context):
    try:
        conn = Database_Connection()
        cur = conn.cursor()

        string_query = f'UPDATE {table_name} SET Name = %s'
        conditions= f' WHERE '  
        if 'id' in context:
            id = context['id']
        if (type(context) == dict and len(context.keys())>0):
            print(context)
            condition_list=[]
            for key in context.keys():
                condition_list.append(f"{key}='{context[key]}'")
            conditions+=' AND '.join(condition_list)
            
            print('Condition Query ',conditions)
            string_query += conditions

            cur.execute(string_query,tuple(context.values()))
            return {'id':id,'Message':"Message updated successfully"}

        
    except Exception as e:
        print(e)
        
    
    # finally:
    #     conn.commit()
    #     conn.close()

# def Insert():
#     try:
        

#         conn = Database_Connection()
#         cur = conn.cursor()
#         cur.execute('INSERT INTO books (Id,Name, Author, Available) VALUES (%s,%s, %s, %s)',
#                     (data['id'],data['name'], data['author'], data['available']))
        
#         return jsonify({'message':'data added sucessfully'})
    
#     except Exception as e:
#         print(e)

#     finally:
#         conn.commit()
#         conn.close()