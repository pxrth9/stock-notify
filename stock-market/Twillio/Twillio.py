from twilio.rest import Client
import os

T_ACCOUNT_SID = os.environ['T_ACCOUNT_SID']
T_AUTH_TOKEN = os.environ['T_AUTH_TOKEN']
T_TWILIO_NUMBER = os.environ['T_TWILIO_NUMBER']

client = Client(T_ACCOUNT_SID, T_AUTH_TOKEN)


def send_sms(phone_number, message):
    message = client.messages.create(
        from_=T_TWILIO_NUMBER,
        body=message,
        to=phone_number
    )
    print(message.sid)
