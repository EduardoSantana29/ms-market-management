from flask import request, jsonify, make_response
from src.application.service.user_service import UserService

class UserController:
    @staticmethod
    def register_seller():
        """Cadastra um vendedor na aplicação.
        Caso os dados obrigatórios não sejam informados, retorna um erro 400 (Bad Request).
        Caso o cadastro seja realizado com sucesso, retorna um código 201 (Created) com o ID do vendedor cadastrado."""
        
        try:
            data = request.get_json()
            nome = data.get('nome')
            cnpj = data.get('cnpj')
            email = data.get('email')
            celular = data.get('celular')
            senha = data.get('senha')

            if not nome or not cnpj or not email or not celular or not senha:
                return make_response(jsonify({"erro": "Todos os campos são obrigatórios"}), 400)

            seller = UserService.create_seller(nome, cnpj, email, celular, senha)

            return make_response(jsonify({
                "mensagem": "Seller salvo com sucesso!",
                "seller_id": seller.id
            }), 201)

        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 400)