# TODO: Переделать все на функции, возможно классы. Добавить исключения. Добавить тесты
import select
import socket
import lib.libsrv as libsrv
import lib.common as common

# Получить адресс и порт из функции
address, port = common.getting_arguments()
server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
# Вызывает exception если адресс или порт указанны неверно.
try:
    server_socket.bind((address, port))
except OSError:
    print('Неправельно указан адрес или порт')
server_socket.listen(100)
chat_client_in = [server_socket]
chat_client_out = []

while chat_client_in:
    soc_client_r, soc_client_w, soc_client_e = select.select(chat_client_in, chat_client_out, chat_client_in, 1)
    for s in soc_client_r:
        if s is server_socket:
            sock, addr = s.accept()
            chat_client_in.append(sock)
        else:
            try:
                data = libsrv.get_data_from_socket(s)
                if data.get('action') == 'msg':
                    print(data.get('message'))
                    if s not in chat_client_out:
                        chat_client_out.append(s)
            except:
                chat_client_in.remove(s)
# while True:
#     sock, addr = server_socket.accept()
#     # Создаем список сокетов
#     chat_client.append(sock)
#     # Очищаем стандартный список после прохождение цикла
#     soc_client_r = []
#     soc_client_w = []
#     # присваеваем списку, активных клиентов что могут читать и писать
#     _ , soc_client_w, _ = select.select([], chat_client, [], 1)
#     # проходимся по списку что нам что то прислали
#     for r_client in soc_client_w:
#         print('r_client = {}'.format(r_client))
#         try:
#             # Тест для вывода сообщений сервера
#             data = libsrv.get_data_from_socket(r_client)
#             if data.get('action') == 'msg':
#                 print(data.get('message'))
#                 # for w_client in soc_client_w:
#                 #     print(data.get('message'))
#                     # libsrv.send_message_all_in_chat(w_client, data.get('message'))
#         except:
#             # удаляем если вернулась ошибка из общего списка
#             chat_client.remove(r_client)
#             print('error')
