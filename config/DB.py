from flask_mysqldb import MySQL


def DBconnection (app):
     
        app.config['MYSQL_USER'] = 'root'
        app.config['MYSQL_HOST'] = 'localhost'
        app.config['MYSQL_PASSWORD'] = '1234'
        app.config['MYSQL_DB'] = 'dbtodo'
        app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
        app.config['JWT_SECRET_KEY']='secret'
        print("DB CONNECTED")
        
        return MySQL(app)
   
    
  