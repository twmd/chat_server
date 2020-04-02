import socket
import lib.common as common
import lib.libclient as libclient

# Получить адресс и порт из функции
address, port = common.getting_arguments()
client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
client_socket.connect((address, port))
#Отсылает в функцию что должно уйти сообщение presence
libclient.action_function('presence', client_socket)
#Тест. Выводит ответ сервера в консоль
print(libclient.get_data_from_socket(client_socket))
client_socket.close()
