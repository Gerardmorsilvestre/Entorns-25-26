from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/user',methods=['GET'])
def user():
    resposta=""
    # Parametres
    username = request.args.get("username",default="")
    # Si els paràmetres OK
    if username != "":
    # Anar al DAO Server i cercar User per username
    # respondre amb dades Ususari si trobat
        resposta="username=" + username
    else:  #  Si els paràmetres NO ok 
        # respondre error
        resposta="username No Informat"
    
    return resposta


if __name__ == '__main__':
    app.run(debug=True)