from src.infrastructure.model.user import User
from src.infrastructure.http.whatsapp import WhatsAppService
from src.config.data_base import db
import random
import jwt
from datetime import datetime, timedelta

class UserService:
    """Classe que gerencia o serviço de usuários da aplicação."""

    @staticmethod
    def create_seller(nome, cnpj, email, celular, senha):
        """Cadastra o usuário no banco de dados.\n
        Valida se o usuário não foi cadastrado anteriormente, à partir do e-mail.\n
        Gera um código de ativação randômico e envia à partir da instância do serviço do WhatsApp."""

        existing_seller = User.query.filter_by(email=email).first()
        if existing_seller:
            raise Exception("E-mail já cadastrado")

        activation_code = str(random.randint(1000, 9999))
        new_seller = User(name=nome, cnpj=cnpj, email=email, celular=celular)
        new_seller.set_password(senha)  
        new_seller.activation_code = activation_code

        db.session.add(new_seller)
        db.session.commit()

        WhatsAppService.send_code(celular, activation_code)

        return new_seller

    @staticmethod
    def verify_activation_code(celular, codigo):
        """Verifica se o celular e código de ativação enviado é válido.\n
        Atualiza o status do usuário para 'Ativo' no banco de dados."""

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
        """Autentica o usuário à partir do e-mail e senha informados.\n
        Gera um token JWT com expiração de 1 hora, à partir do ID do usuário."""
        try:
            seller = User.query.filter_by(email=email).first()

            if not seller or not seller.check_password(senha):
                return {"erro": "E-mail ou senha inválidos"}, 401

            if seller.status != "Ativo":
                return {"erro": "Conta inativa. Complete a ativação antes de acessar."}, 403

            token = jwt.encode({
                'seller_id': seller.id,
                'exp': datetime.utcnow() + timedelta(hours=1)
            }, senha, algorithm='HS256')

            return token
        except Exception as e:
            return {"erro": str(e)}, 500