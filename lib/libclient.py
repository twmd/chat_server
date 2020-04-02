# TODO: Сделать все через словарь. Вызов методов
import json
import datetime
import lib.libException as libException
from lib.common import log as log

# Принимаеет сообщение от сервера, смотрит на поле action, выбирает дальнейшее действие
@log
def get_data_from_socket(sock):
    server_data_buf = sock.recv(1024)
    server_data = json.loads(server_data_buf.decode())
    return server_data


# обрабатывае какое сообщение отсылать Описанны типы сообщений.
@log
def action_function(action, sock):
    if len(action) <= 15:
        action_dist = {
            'presence': presence_message,
            'prоbe': None,
            'msg': None,
            'quit': None,
            'authenticate': None,
            'join': None,
            'leave': None

        }
        # print()
        sock.send(action_dist[action]())
    else:
        raise libException.ActionLenght


# TODO: Добавить проверку типов
# Формирует presence сообщение клиента
@log
def presence_message(account_name='slava', status_msg=''):
    msg = {
        'action': 'presence',
        'time': datetime.datetime.now().timestamp(),
        'type': 'status',
        'user': {
            'account_name': str(account_name),
            'status': str(status_msg)}
    }
    msg_json = json.dumps(msg)
    buf = msg_json.encode()
    # sock.send(buf)
    return buf


if __name__ == '__main__':
    pass
