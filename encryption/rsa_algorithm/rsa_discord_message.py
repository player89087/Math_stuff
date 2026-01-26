import requests
import json

global e
e = None
global d
d = None
global n
n = None

channel_id = " "
authorization = " "

def retrieve_msg(channel_id):
    headers = {
        "Authorization": authorization 
    }
    r = requests.get(
        f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=50",
        headers=headers
    )
    jsonn = json.loads(r.text)
    global message1, message2, message3
    message1 = jsonn[0]["content"]
    message2 = jsonn[1]["content"]
    message3 = jsonn[2]["content"]

def send_msg(channel_id, message):
    headers = {
        "Authorization": authorization
    }
    payload = {
        "content": message
    }
    dc_channel = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    requests.post(dc_channel, payload, headers=headers)

def rsa_decrypt(message):
    global n, d
    if n is None:
        n = int(input("What is the value of the public key n: "))
    if d is None:
        d = int(input("What is your public key d (decryption): "))
    secret_msg = list(map(int, message.split()))
    clear_message = []
    for i in range(len(secret_msg)):
        clear_message.append(pow(secret_msg[i], d, n))
        print(chr(clear_message[i]), end="")
    print()

def rsa_encrypt(n, e):
    global secret_msg
    if n is None:
        n = int(input("What is the value of the public key n: "))
    print("\n")
    if e is None:
        e = int(input("What is your public key e (encryption): "))
    message_sending = input("Type in the message you want to decrypt: ")
    unicode = []
    for i in range(len(message_sending)):
        unicode.append(ord(message_sending[i]))
    secret_msg = []
    for i in range(len(message_sending)):
        secret_msg.append(pow(unicode[i], e, n))
    print(f"secret message = {secret_msg}")
    send_msg(channel_id, " ".join(map(str, secret_msg)))

def main():
    de_en = int(input("Decrypt 1, encrypt 2: "))
    if de_en == 1:
        retrieve_msg(channel_id)
        print(f"1. {message1},\n")
        print(f"2. {message2},\n")
        print(f"3. {message3},\n")
        dcs = int(input("Which message would you like to decrypt (1,2,3): "))
        if dcs == 1:
            rsa_decrypt(message1)
        elif dcs == 2:
            rsa_decrypt(message2)
        elif dcs == 3:
            rsa_decrypt(message3)
    elif de_en == 2:
        rsa_encrypt(n, e)

while True:
    main()
