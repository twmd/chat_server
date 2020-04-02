import json
import datetime
from lib.common import log as log

# TODO: Доделать по выбору action.
# Принимаеет сообщение от клиента, смотрит на поле action, выбирает дальнейшее действие

@log
def get_data_from_socket(sock):
    client_data_buf = sock.recv(1024)
    client_data = json.loads(client_data_buf.decode())
    return client_data


# обрабатывае какое сообщение отсылать Описанны типы сообщений.
# Заготовка
@log
def action_from_client(action):
    pass
    action_dist = {
        'presence': None,
        'prоbe': None,
        'msg': None,
        'quit': None,
        'authenticate': None,
        'join': None,
        'leave': None

    }


# Отсылает ответ клиенту. В зависимости от типа allert или error
@log
def response_message(sock, type='alert'):
    msg = {
        'response': '',
        'time': datetime.datetime.now().timestamp(),
    }
    if type == 'alert':
        msg.update({'alert': ''})
    elif type == 'error':
        msg.update({'error': ''})

    msg_json = json.dumps(msg)
    buf = msg_json.encode()
    sock.send(buf)


if __name__ == '__main__':
    pass
