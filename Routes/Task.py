from flask import Blueprint, jsonify, request, json

from middleware.Authmid import  Authmid  

from flask_cors import CORS

from flask_jwt_extended import get_jwt_identity , jwt_required

def Task(app, mysql):
 
   CORS(app)
   
   @app.route('/task', methods=['GET'])
   def get_task():  
      cur = mysql.connection.cursor()
      ID = request.get_json()['ID']
      cur.execute("SELECT * FROM Task AS t INNER JOIN projects AS p ON T.ID_Project = p.ID where p.ID ="+ID ) 
      rv= cur.fetchall()
      return jsonify(rv)
   
   @app.route('/task', methods=['POST']) 
   def add_task():
       cur = mysql.connection.cursor()
       NameT = request.get_json()['Name_Task']
       ID = request.get_json()['ID']
       if(not cur.execute("SELECT * FROM Task where Name_Task='"+str(NameT)+"'")):
        cur.execute("INSERT INTO Task (Name_Task,ID_Project,completed) VALUES ('"+str(NameT)+"', "+ ID +", false)")
        mysql.connection.commit()
        result = {'NameT': NameT}
        
       else :
          result = " Task already exist"
          
       return jsonify({"result": result}) 
    
   @app.route('/task', methods=['DELETE'])
   def delete_task():
      cur = mysql.connection.cursor()
      ID = request.get_json()['ID']
      cur.execute("delete from Task where ID = "+ ID )
      mysql.connection.commit()
      result = "Delete Complete"
      return jsonify({"result": result})
   
   