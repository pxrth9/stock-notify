import sys
sys.path.insert(0, 'E:/WorkSpace/stock-notify/twillio')

from send import send_sms

if __name__ == '__main__':
    TO = '+19085241817'
    BODY = 'Hello, this is a test message.'
    send_sms(TO, BODY)
