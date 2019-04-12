# -*- coding: UTF-8 -*-
import frida,sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


js_code = '''
    Java.perform(function(){
		var MainActivity = Java.use("com.yusakul.myapplication.MainActivity");
		MainActivity.getString.implementation = function(v1){
			var result = this.getString(v1);

			console.log("functionArg:"+v1);
			console.log("return:"+result);
			console.log("-----------------------------------------------------")
			return result;
		}
});
'''
session = frida.get_usb_device().attach("com.yusakul.myapplication")
script = session.create_script(js_code)
script.on('message',on_message)
script.load()
sys.stdin.read()