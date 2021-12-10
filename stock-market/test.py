# from Twillio.Twillio import send_sms
import os

if __name__ == "__main__":
    print(os.getenv("T_TWILIO_NUMBER"))
    # send_sms("+19085241817", "Hello World!")
