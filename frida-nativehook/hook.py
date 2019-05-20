# -*- coding: UTF-8 -*-
import frida, sys, time

def message(message, data):
    if message["type"] == 'send':
        print(u"[*] {0}".format(message['payload']))
    else:
        print(message)

process = frida.get_remote_device().attach("com.xiaojianbang.app")
with open("./script.js") as f:
    script = process.create_script(f.read())
script.on("message", message)
script.load()

sys.stdin.read()
#input()