import functools

import jwt as pyjwt
from flask import current_app, g, jsonify, request

def _get_bearer_token():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return None
    if auth_header.startswith("Bearer "):
        return auth_header[len("Bearer "):]
    return auth_header

def login_required(roles = None):
    def decorator(view_func):
        @functools.wraps(view_func)
        def wrapper(*args, **kwargs):
            jwt_manager = current_app.config["JWT_MANAGER"]
            db_manager = current_app.config["DB_MANAGER"]

            token = _get_bearer_token()
            if token is None:
                return jsonify(error = "Missing authorization token"), 401
            try:
                decoded = jwt_manager.decode(token)
            except pyjwt.ExpiredSignatureError:
                return jsonify (error = "Token expired"),401
            except pyjwt.InvalidTokenError:
                return jsonify(error = "Invalid Token"), 401
            except Exception:
                return jsonify(error = "Internal server error"), 500
            
            if not decoded or "id" not in decoded:
                return jsonify(error = "Invalid Token"), 401
            
            if decoded.get("type") != "access":
                return jsonify(error = "Invalid Token"), 401
            
            try:
                user = db_manager.get_user_by_id(decoded["id"])
            except Exception:
                return jsonify(error = "Internal server error"), 500
            
            if user is None:
                return jsonify(error= "Invalid token" ), 401
            
            g.user_id = user.id
            g.username = user.username
            g.role = user.role

            if roles is not None and g.role not in roles:
                return jsonify(error = "Forbidden: insufficient permissions"), 403
            
            return view_func(*args, **kwargs)
        return wrapper
    return decorator

            