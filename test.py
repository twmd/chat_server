# import subprocess
# #test
# proc_list = []
# args = ["ping", "www.yahoo.com"]
# proc_list.append(subprocess.Popen(args, creationflags=subprocess.CREATE_NEW_CONSOLE).communicate())
# print(proc_list)

msg = {
    "action": 'msg',
    "time":  'Time',
    "to": 'all',
    "from": 'all',
    "encoding": "ascii",
    "message": 'Message 123'
}

print(msg.get('action'))