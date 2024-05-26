import requests
import time
import zmq


def convert_currency(amount, from_currency, to_currency):
    # Input 'api_key' with your actual API key from https://app.exchangerate-api.com/dashboard/
    api_key = ''
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'

    response = requests.get(url)
    data = response.json()

    if 'error' in data:
        return None, data['error']

    if to_currency not in data['conversion_rates']:
        return None, f'Invalid currency code: {to_currency}'

    exchange_rate = data['conversion_rates'][to_currency]
    converted_amount = amount * exchange_rate

    return converted_amount, None


if __name__ == "__main__":
    while True:
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:5555")

        #  Wait for next request from client
        message = socket.recv()
        print("Received request: %s" % message)

        #  Do some 'work'
        time.sleep(1)
        message = message.decode()
        message = message.split()
        message[0] = float(message[0])
        converted_amount, error = convert_currency(message[0], message[1], message[2])
        if error:
            reply = "Conversion failed:", error
        else:
            reply = f"{message[0]} {message[1]} is equal to {converted_amount:.2f} {message[2]}"

        #  Send reply back to client
        socket.send(str.encode(reply))
