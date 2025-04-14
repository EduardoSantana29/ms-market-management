import jwt
import datetime
from flask import request, jsonify, make_response, current_app
from src.application.service.user_service import UserService
from src.infrastructure.model.user import User

class UserController:
    @staticmethod
    def register_seller():
        try:
            data = request.get_json() or request.form

            nome = data.get('nome')
            cnpj = data.get('cnpj')
            email = data.get('email')
            celular = data.get('celular')
            senha = data.get('senha')

            if not nome or not cnpj or not email or not celular or not senha:
                return make_response(jsonify({"erro": "Todos os campos são obrigatórios"}), 400)

            seller = UserService.create_seller(nome, cnpj, email, celular, senha)

            return make_response(jsonify({
                "mensagem": "Seller salvo com sucesso! Redirecionando...",
                "redirect": "/activate"
            }), 201)

        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 400)

    @staticmethod
    def activate_seller():
        data = request.get_json()
        celular = data.get('celular')
        codigo = data.get('codigo')

        if not celular or not codigo:
            return make_response(jsonify({"erro": "Campos obrigatórios ausentes"}), 400)

        response = UserService.verify_activation_code(celular, codigo)
        return make_response(jsonify(response), 200)

    @staticmethod
    def login():
        data = request.get_json()
        email = data.get('email')
        senha = data.get('senha')

        if not email or not senha:
            return make_response(jsonify({"erro": "Campos obrigatórios ausentes"}), 400)

        user = User.query.filter_by(email=email).first()

        if not user or not user.check_password(senha):
            return make_response(jsonify({"erro": "Credenciais inválidas"}), 401)

        if user.status != "Ativo":
            return make_response(jsonify({"erro": "Conta não ativada"}), 403)

        # Gerar token JWT
        payload = {
            "user_id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        }

        token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

        return make_response(jsonify({
            "mensagem": "Login bem-sucedido",
            "access_token": token
        }), 200)