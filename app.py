from flask import Flask
from Routes.Users import Users
from Routes.Projects import Projects
from Routes.Task import Task

from config.DB import DBconnection



app = Flask(__name__)
mysql = DBconnection(app)

Users(app, mysql)
Projects(app, mysql)
Task(app,mysql)


if __name__ == '__main__':
    app.run(debug=True)
   
   