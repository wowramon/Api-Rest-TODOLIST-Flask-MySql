from flask import Blueprint, jsonify, request, json
from middleware.Authmid import  Authmid  
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity , jwt_required
from datetime import datetime




def Users(app, mysql):
    

    bcrypt = Bcrypt(app)
    JWTManager(app)
    CORS(app)
    created = datetime.utcnow()
    

    @app.route('/register', methods=['POST'])
    def register():
        cur = mysql.connection.cursor()
        email = request.get_json()['email']
        password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
        name = request.get_json()['name']
    

        if(not cur.execute("SELECT * FROM users where email='"+str(email)+"'")):
            cur.execute("INSERT INTO users (email,password,name,Udate) VALUES ('"+
            str(email) + "', '" + 
            str(password) + "', '" + 
            str(name) + "', '"+
            str(created) + "')")
            
            mysql.connection.commit()
            
            result ={
                "name": name,
                "email": email,
                "password": password
            }
            
        else:
            result = "email already exist"
            
        return jsonify({"result":result})

    @app.route('/Login', methods=['POST'])
    def login():
        cur = mysql.connection.cursor()
        email = request.get_json()['email']
        password = request.get_json()['password']
        result = ""
        
        if cur.execute("SELECT * from users where email='" + str(email)+"'"):
            rv = cur.fetchone()
            
            if bcrypt.check_password_hash(rv['Password'], password):
                access_token = create_access_token(identity= {'id':rv['ID'],'name': rv['name'], 'email': rv['Email'], 'Udate': rv['Udate']})
                result = jsonify({"Token": access_token})
            
                
            else:
                result = jsonify({"Error":"Invalid  Password"})
        else:
            result = jsonify({"Error":"Invalid Username"})
    
   
            
        return result
    

        
 
   