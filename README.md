# Market Management

O projeto Market Management é um sistema de gerenciamento de vendas.
O software foi desenvolvido em `Python`, à partir do framework `Flask`, usando o
banco de dados `SQLite` para persistência dos dados, e futuramente, será
implementado `ReactJS` para a definição da interface gráfica.

A aplicação é integrada com a API da `Twilio` que permite enviar mensagens de texto por WhatsApp.

## Instalação

Para instalar o projeto, siga os passos abaixo:

1. Clone o repositório:
```bash
git clone https://github.com/EduardoSantana29/ms-market-management.git
```

2. Acesse o diretório do projeto:
```bash
cd ms-market-management
```

3. Crie um ambiente virtual:
```bash
python -m venv venv
```

4. Ative o ambiente virtual:
```bash
./venv/bin/activate
```

5. Instale as dependências:
```bash
pip install -r requirements.txt
```

6. Configure as variáveis de ambiente, no arquivo `.env`:
```bash
TWILIO_ACCOUNT_SID= `O SID da sua conta Twilio`
TWILIO_AUTH_TOKEN= `O Token de Autenticação da sua conta Twilio`
TWILIO_WHATSAPP_NUMBER= `O número de WhatsApp da sua conta Twilio`
```

7. Execute a aplicação à partir do arquivo `run.py`.
Esse arquivo é responsável por inicializar a aplicação e criar o banco de dados.
```bash
python run.py
```

8. Teste a aplicação, fazendo uma requisição GET para o endpoint `/api`.
Esse endpoint valida o status da aplicação.

## Autores
👤 **Nicholas Costa P.**
- GitHub: https://github.com/nicholascostap

👤 **Eduardo Santana**
- GitHub: https://github.com/EduardoSantana29

👤 **Gabriel Rodrigues da Silva**
- GitHub: https://github.com/gabrieldevrs

👤 **Renato**
- GitHub: https://github.com/Renato-FSilva

👤 **Vinicius**
- GitHub: https://github.com/Vinicius-oliveira-lima

## 🤝 Contribuições

👤 **Carlos Rafael Magalhães**
- Orientador
- GitHub: https://github.com/carlosrmfernandes