from src.config.data_base import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """Classe que representa a tabela `users` no banco de dados.
    
    Attributes:
        - `id` (int): ID do usuário. Chave primária.
        - `name` (str): Nome do usuário. Obrigatório.
        - `email` (str): E-mail do usuário. Obrigatório e único.
        - `password_hash` (str): Hash da senha do usuário. Obrigatório.
        - `cnpj` (str): CNPJ do usuário. Único.
        - `celular` (str): Celular do usuário. Único.
        - `status` (str): Status do usuário. Padrão 'Inativo', após ativação do código, é atualizado para 'Ativo'.
        - `activation_code` (str): Código de ativação do usuário.
    """
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    cnpj = db.Column(db.String(20), unique=True, nullable=True)
    celular = db.Column(db.String(15), unique=True, nullable=True)
    status = db.Column(db.String(20), default="Inativo")
    activation_code = db.Column(db.String(4), nullable=True)

    def set_password(self, password):
        """Criptografa a senha em hash, à partir da senha informada."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica se a senha informada é válida, à partir do hash da senha."""
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Retorna um dicionário com os atributos do usuário."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "cnpj": self.cnpj,
            "celular": self.celular,
            "status": self.status
        }