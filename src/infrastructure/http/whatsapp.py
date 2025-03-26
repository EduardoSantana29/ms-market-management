from twilio.rest import Client
import os

class WhatsAppService:
    """
    Classe que gerencia o serviço de envio de mensagens via WhatsApp.

    Attributes:
        - `account_sid` (str): SID da conta Twilio.
        - `auth_token` (str): Token de autenticação Twilio.
        - `from_whatsapp_number` (str): Número do WhatsApp que envia a mensagem.
        - `client` (Client): Cliente Twilio.
        - `message` (Message): Mensagem enviada.
    """

    @staticmethod
    def send_code(phone, activation_code):
        """Envia o código de ativação à partir do número do WhatsApp 
        cadastrado na Twilio, para o número de telefone informado no
        corpo da requisição."""
        
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        from_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')
        
        client = Client(account_sid, auth_token)
        
        message = client.messages.create(
            from_=f'whatsapp:{from_whatsapp_number}',
            body=f'Seu código de ativação é: {activation_code}',
            to=f'whatsapp:{phone}'
        )
        
        return message.sid
