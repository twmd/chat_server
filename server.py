# TODO: Переделать все на функции, возможно классы. Добавить исключения. Добавить тесты
import select
import socket
import lib.libsrv as libsrv
import lib.common as common

def client_connection():
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
    # chat_client_out = []

    while chat_client_in:
        data = {}
        soc_client_r, soc_client_w, soc_client_e = select.select(chat_client_in, chat_client_in, chat_client_in, 1)

        # Получает данные от клиента
        for s in soc_client_r:
            if s is server_socket:
                sock, addr = s.accept()
                chat_client_in.append(sock)
            else:
                try:
                    data = libsrv.get_data_from_socket(s)
                except Exception as e:
                    chat_client_in.remove(s)
                    print(e)

        # Отсылает данные клиенту
        for s in soc_client_w:
            if data:
                try:
                    # print(s)
                    libsrv.send_message_all_in_chat(s, data.get('message'))
                    # print(data.get('message'))
                except Exception as e:
                    print(e)
                    chat_client_in.remove(s)

        # Удаляет ошибочные сокеты
        for s in soc_client_e:
            chat_client_in.remove(s)
            s.close()

if __name__ == '__main__':
    client_connection()
