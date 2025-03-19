from twilio.rest import Client
import os

class WhatsAppService:
    @staticmethod
    def send_code(celular, codigo):
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        from_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')
        
        client = Client(account_sid, auth_token)
        
        message = client.messages.create(
            from_=f'whatsapp:{from_whatsapp_number}',
            body=f'Seu código de ativação é: {codigo}',
            to=f'whatsapp:{celular}'
        )
        
        return message.sid
