import smtplib
import requests
from typing import Any
from flask_caching import Cache
from helpers.logger import logging
from helpers import queries, db, main,res_msg
from flask import Flask, jsonify, render_template, render_template_string, request

cache = Cache(config={"CACHE_TYPE":"simple"})
app = Flask(__name__)
cache.init_app(app)

MAIN_URL:str = '/mlshopadmin/api/v1/'

@app.route("/")
@app.route(f"{MAIN_URL}checkConnection")
@cache.cached(timeout=100)
def check_connection():
  try:   
    con = db.pool.get_connection()
    if con.is_connected():
      return main.resJson(ResponseCode=200,ResponseMessage="Success in connecting to Database.")
    else :
      return main.resJson(ResponseCode=200,ResponseMessage="Failed in connecting to Database.")
  except db.MySQLError  as e:
      return main.resJson(500,e.msg)
  finally:
      con.close()


@app.route(f"{MAIN_URL}disableSeller",methods=['POST'])
def disable_seller():
     con = db.pool.get_connection();
     cursor = con.cursor();
     try:
        body = dict(request.form)
        email  = body.get('email'); id = body.get('merchantID')
        msg = res_msg.index(18); code = 200
        if main.is_none(email) or main.is_none(id):
           msg = res_msg.index(5); code =463
        else:
           cursor.execute(queries.Query(1),[id,email])
           con.commit()
     except BaseException as e:
         msg = e.msg; code = 500
         con.rollback()
     finally:
        con.close();cursor.close()
        return main.resJson(ResponseCode=code,ResponseMessage=msg);


@app.route(f"{MAIN_URL}denySeller",methods=['POST'])
def deny_seller():
  con = db.pool.get_connection();
  cursor = con.cursor();
  try:
     body = dict(request.form)
     email  = body.get('email'); id = body.get('merchantID')
     msg = res_msg.index(200); code = 200
     if main.is_none(email) or main.is_none(id):
        msg = res_msg.index(5); code =463
     else:
        cursor.execute(queries.Query(4),[id,email])
        con.commit()
  except BaseException as e:
      msg = e.msg; code = 500
      con.rollback()
  finally:
     con.close();cursor.close()
     return main.resJson(ResponseCode=code,ResponseMessage=msg);

@app.route(f"{MAIN_URL}changePassword")
def change_password():
    con = db.pool.get_connection()
    cursor  = con.cursor()
    code:int = 200 ;msg:str = res_msg.index(200); result = []
    try:
      qry = dict(request.args);
      email = qry.get('email');new_pass = qry.get('newPassword');id = qry.get('merchantID')
      if main.is_none(email) or main.is_none(new_pass) or main.is_none(id):
           msg = res_msg.index(5); code = 463
      else:
           msg = res_msg.index(200); code =200
    except BaseException as e:
       code = 500 ; msg =e.msg
    finally:
       con.close();cursor.close();
       return main.resJson(ResponseCode=code,ResponseMessage=msg)


@app.route("/send-json")
def send_json():
    r = requests.get("https://jsonplaceholder.typicode.com/todos")
    return jsonify(r.json())

@app.route(f"{MAIN_URL}searchSeller")
def search_by_seller():
    con = db.pool.get_connection()
    cursor = con.cursor()
    try:
        qry_str = dict(request.args); msg:str = res_msg.index(200)
        code = 200; result = []
        if main.is_none(qry_str.get('sellerName')):
           msg = res_msg.index(5); code = 463
        else:
           cursor.execute(queries.Query(6),[qry_str.get('sellerName')])
           result = cursor.fetchall()
           result = main.result_dict(cursor.column_names,result)
           msg = res_msg.index(200); code = 200
    except BaseException as e:
        msg = e.msg; code = 500
    finally:
        con.close();cursor.close()
        return main.resJson(ResponseCode=code,ResponseMessage=msg,result=result)



@app.route(f"{MAIN_URL}displaySellers")
def display_sellers():
    result = []
    con = db.pool.get_connection()
    code = 200; msg  = res_msg.index(200)
    cursor : Any
    try:
        cursor = con.cursor()
        cursor.execute(queries.Query(0))
        result = cursor.fetchall()
        result = main.result_dict(cursor.column_names,result)
    except db.MySQLError as e:
       code = 500; msg = e.msg
    finally:
        con.close(); cursor.close()
        return main.resJson(ResponseCode=code,ResponseMessage=msg,Seller_List=result)

if __name__ == "__main__":
    app.run(debug=True)

