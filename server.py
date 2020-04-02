#TODO: Переделать все на функции, возможно классы. Добавить исключения. Добавить тесты
import select
import socket
import lib.libsrv as libsrv
import lib.common as common

# Получить адресс и порт из функции
address, port = common.getting_arguments()
server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
chat_client = []
# Вызывает exception если адресс или порт указанны неверно.
try:
    server_socket.bind((address, port))
except OSError:
    print('Неправельно указан адрес или порт')
server_socket.listen(100)

while True:
    sock, addr = server_socket.accept()
    # Создаем список сокетов
    chat_client.append(sock)
    # Очищаем стандартный список после прохождение цикла
    in_client = []
    out_client = []
    # присваеваем списку, активных клиентов что могут читать и писать
    in_client, out_client, _ = select.select(chat_client, chat_client, [], 1)
    #проходимся по списку что нам что то прислали
    for l_client in in_client:
        try:
            # Тест для вывода сообщений сервера
            print(libsrv.get_data_from_socket(l_client))
        except:
            #удаляем если вернулась ошибка из общего списка
            chat_client.remove(l_client)
    # проходимся по списку клиентов на отправку
    for l_client in out_client:
        try:
            # Функция отсылает данные
            libsrv.response_message(l_client)
        except:
            chat_client.remove(l_client)
