from twilio.rest import Client
from decouple import config


# FROM_NUMBER = config('T_TWILIO_NUMBER')
# ACCOUNT_SID = config('T_ACCOUNT_SID')
# AUTH_TOKEN = config('T_AUTH_TOKEN')

# client = Client(T_ACCOUNT_SID, T_AUTH_TOKEN)


# def send_sms(phone_number, message):
#     message = client.messages.create(
#         from_=T_TWILIO_NUMBER,
#         body=message,
#         to=phone_number
#     )
#     print(message.sid)
