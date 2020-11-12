from flask import Blueprint, jsonify, request, json

from config.DB import DBconnection
from middleware.Authmid import  Authmid  

from flask_cors import CORS

from flask_jwt_extended import get_jwt_identity , jwt_required

def Projects(app, mysql):
 
   CORS(app)
   
   @app.route('/projects', methods=['GET'])
   def get_projects( ):  
      cur = mysql.connection.cursor()
      Email = Authmid.JwtR()
      cur.execute("SELECT * FROM Projects AS p INNER JOIN Users AS u ON p.ID_User = u.ID WHERE u.Email='"+str(Email)+"'" ) 
      rv= cur.fetchall()
      return jsonify(rv)
   
   @app.route('/projects', methods=['POST']) 
   def add_projects():
       cur = mysql.connection.cursor()
       Email = Authmid.JwtR()
       NameP = request.get_json()['NameP']
       if(not cur.execute("SELECT * FROM projects where NameP='"+str(NameP)+"'")):
        cur.execute("INSERT INTO Projects (NameP,ID_User) VALUES ('" + str(NameP) + "', (select ID from Users where Email = '"+str(Email)+"'))")
        mysql.connection.commit()
        result = {'NameP': NameP}
        
       else :
          result = " Project already exist"
          
       return jsonify({"result": result}) 
    
   @app.route('/projects', methods=['DELETE'])
   def delete_projects():
      cur = mysql.connection.cursor()
      ID = request.get_json()['ID']
      cur.execute("delete from Projects where ID = "+ ID )
      mysql.connection.commit()
      result = "Delete Complete"
      return jsonify({"result": result})
   
   