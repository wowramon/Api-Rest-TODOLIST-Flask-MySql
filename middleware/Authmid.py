from flask import jsonify, request, json
from flask_jwt_extended import get_jwt_identity , jwt_required
 

class Authmid():
  
  def JwtR():
    @jwt_required
    def protected():
      # Access the identity of the current user with get_jwt_identity
            current_user = get_jwt_identity().get('email')
            return str(current_user)
    return protected()
  
 
