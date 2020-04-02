[loggers]
keys=root,filesLogger

[handlers]
keys=fileHandler,consoleHandler

[formatters]
keys=myFormatter

[logger_root]
level=CRITICAL
handlers=consoleHandler

[logger_filesLogger]
level=INFO
handlers=fileHandler
qualname=filesLogger

[handler_consoleHandler]
class=StreamHandler
level=CRITICAL
formatter=myFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
formatter=myFormatter
args=("log.txt",)

[formatter_myFormatter]
# format=%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s
format=%(asctime)s - %(levelname)s - %(message)s
