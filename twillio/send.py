from twilio.rest import Client
from decouple import config


ACCOUNT_SID = config('T_ACCOUNT_SID')
AUTH_TOKEN = config('T_AUTH_TOKEN')
TWILIO_NUMBER = config('T_TWILIO_NUMBER')

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send_sms(to, message):
    message = client.messages.create(
        to=to,
        from_=TWILIO_NUMBER,
        body=message
    )
    print(message.sid)