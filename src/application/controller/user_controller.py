













































    
    @staticmethod
    def login():
        data = request.get_json()
        email = data.get('email')
        senha = data.get('senha')

        if not email or not senha:
            return make_response(jsonify({"erro": "Campos obrigatórios ausentes"}), 400)  # Mensagem em português

        token = UserService.authenticate_seller(email, senha)
        return make_response(jsonify({"access_token": token}), 200)