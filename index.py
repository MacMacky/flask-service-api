from flask import Flask,jsonify,render_template,render_template_string
import requests
import mysql.connector as connection
from settings import DBHOST,DBPASS,DBPORT,DBUSER
from helpers.queries import Query
from typing import Tuple

app = Flask(__name__)

def slice(listo=[],start =0, stop=1):
   result = []
   lengtho = len(listo)
   for i in range(lengtho):
        if start == stop:
            break
        else:
           result.append(listo[i])
           start += 1
   return result

@app.route('/')
@app.route('/home')
def index():
   r = requests.get('https://jsonplaceholder.typicode.com/todos')
   result = slice(r.json(),1,5)
   print(result)
   return render_template('main.html',todos=result,title="Flask App")
   #return render_template_string(template)

@app.route('/herro-world')
def sample():
   return "Herro Worl2d!"


@app.route('/route-with-param/<name>')
def route_with_param(name:str):
    return "Hello," + name 

@app.route('/send-json')
def send_json():
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    return jsonify(r.json())

@app.route('/get_db_data')
def get_db_data():
  con = connection.connect(host=DBHOST,port=DBPORT,user=DBUSER,password=DBPASS)
  result = []
  try:  
    cursor = con.cursor()
    cursor.execute(Query(0))
    result = cursor.fetchall()
  except (connection.Error,ArithmeticError) as e:
    print(e.msg)
    pass
  finally:
     msg = "Is Connected to DB." if con.is_connected() else "Not Connected to DB"
     con.close()
     return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True);

