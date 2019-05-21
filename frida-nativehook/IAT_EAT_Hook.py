# -*- coding: UTF-8 -*-
import frida, sys

jsCode = """

Java.perform(function(){

	//遍历导入表 获取指定api的地址
    var imports = Module.enumerateImportsSync("lib-netsdk.so");
    for(var i = 0; i < imports.length; i++) {
        if(imports[i].name == 'strncat'){
            send(imports[i].name + ": " + imports[i].address);
            break;
        }
    }

	//遍历导出表 获取指定api的地址
    var exports = Module.enumerateExportsSync("lib-netsdk.so");
    for(var i = 0; i < exports.length; i++) {
        if(exports[i].name.indexOf('add') != -1){
            send(exports[i].name + ": " + exports[i].address);
            break;
        }
    }
	
	//遍历并打印导入表
    for(var i = 0; i < imports.length; i++) {
            send(imports[i].name + ": " + imports[i].address);
        }

	//遍历并打印导出表
	for(var i = 0; i < exports.length; i++) {
			send(exports[i].name + ": " + exports[i].address);
    }

});

    """
	
def on_message(message, data):
    if message['type'] == 'error':
        print("[!] " + message['stack'])
    elif message['type'] == 'send':
        print("[i] " + message['payload'])
    else:
        print(message)

process = frida.get_remote_device().attach("cn.xxxxx.android")
script= process.create_script(jsCode)
script.on("message", on_message)
script.load()
sys.stdin.read()
