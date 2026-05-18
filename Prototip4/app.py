from flask import Flask, request, jsonify
from dao import UserDAO

app = Flask(__name__)
user_dao = UserDAO()


@app.route("/login", methods=["POST"])
def login_endpoint():
    auth_header = request.headers.get("Authorization")

    if auth_header:
        token = auth_header.strip()
        user = user_dao.login_with_token(token)
        if user:
            return jsonify({
                "id": user["id"],
                "username": user["username"],
                "email": user["email"],
                "token": user["token"],
                "idrole": str(user["idrole"]),
                "msg": "Usuari Ok",
                "coderesponse": "1",
            }), 200
        return jsonify({"coderesponse": "0", "msg": "No validat"}), 400

    payload = request.get_json(silent=True) or {}
    username = payload.get("username")
    password = payload.get("password")

    if not username or not password:
        return jsonify({"coderesponse": "0", "msg": "No validat"}), 400

    user = user_dao.login(username, password)
    if user:
        return jsonify({
            "coderesponse": "1",
            "data": {
                "email": user["email"],
                "id": user["id"],
                "idrole": user["idrole"],
                "password": password,
                "token": user["token"],
                "username": user["username"],
            },
            "msg": "Authenticated",
        }), 200

    return jsonify({"coderesponse": "0", "msg": "No validat"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
