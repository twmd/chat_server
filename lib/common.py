from sys import argv
import ipaddress
import logging
import logging.config
from functools import wraps

LOG_ON = True


logging.config.fileConfig(fname='log_config.py')
logger = logging.getLogger('filesLogger')
##########

# TODO: Переделать что бы данные отоброжались не в виде сообщения.
def log(func):
    @wraps(func)
    def log_wrap(*args, **kwargs):
        if LOG_ON:
            logger.info('{} - {}, with argument: {} \n'.format(log_wrap.__module__, log_wrap.__name__, locals().items()))
        res = func(*args, **kwargs)
        return res

    return log_wrap


# TODO: Добавить справку
# TODO: Перепесать на argvars
# Принимает аргументы параметров запуска, проверяет на корректность, и возвращает адрес и порт. Если аргументов нет, то отправляются 0.0.0.0
@log
def getting_arguments():
    server_addr = '0.0.0.0'
    server_port = 7777
    i = 1
    if len(argv) == 3 or len(argv) == 5:
        while i < len(argv):
            if argv[i] == '-p':
                server_port = int(argv[i + 1])

            elif argv[i] == '-a':
                server_addr = argv[i + 1]
            i += 1
            if ipaddress.ip_address(server_addr) and server_port in range(1, 65535):
                return server_addr, server_port
    elif len(argv) == 1:
        if ipaddress.ip_address(server_addr) and server_port in range(1, 65535):
            return server_addr, server_port
    else:
        print('Неправельное кол-во параметров')


if __name__ == '__main__':
    # getting_arguments()
    pass
