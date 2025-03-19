from src.infrastructure.model.user import User
from src.infrastructure.http.whatsapp import WhatsAppService
from src.config.data_base import db
import random
import jwt
from datetime import datetime, timedelta

class UserService:
    @staticmethod
    def create_seller(nome, cnpj, email, celular, senha):
        existing_seller = User.query.filter_by(email=email).first()
        if existing_seller:
            raise Exception("E-mail já cadastrado")

        activation_code = str(random.randint(1000, 9999))
        new_seller = User(name=nome, cnpj=cnpj, email=email, celular=celular)
        new_seller.set_password(senha)  
        new_seller.activation_code = activation_code  # Código armazenado para ativação

        db.session.add(new_seller)
        db.session.commit()

        # Enviar código via WhatsApp
        WhatsAppService.send_code(celular, activation_code)

        return new_seller

    @staticmethod
    def verify_activation_code(celular, codigo):
        seller = User.query.filter_by(celular=celular).first()
        if not seller:
            raise Exception("Celular não encontrado")

        if seller.activation_code != codigo:
            raise Exception("Código inválido")

        seller.status = "Ativo"
        seller.activation_code = None
        db.session.commit()

        return {"message": "Conta ativada com sucesso!"}

    @staticmethod
    def authenticate_seller(email, senha):
        try:
            seller = User.query.filter_by(email=email).first()

            if not seller or not seller.check_password(senha):
                return {"erro": "E-mail ou senha inválidos"}, 401

            if seller.status != "Ativo":
                return {"erro": "Conta inativa. Complete a ativação antes de acessar."}, 403

            # Gerar token JWT
            token = jwt.encode({
                'seller_id': seller.id,
                'exp': datetime.utcnow() + timedelta(hours=1)
            }, 'sua_chave_secreta', algorithm='HS256')

            return token  # Retornar apenas o token
        except Exception as e:
            return {"erro": str(e)}, 500
