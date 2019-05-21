import frida
import sys

session = frida.get_remote_device().attach("com.xiaojianbang.app")

src = """
var nativePointer = Module.findExportByName("libhello.so", "Java_com_xiaojianbang_app_NativeHelper_add");
	send("native: " + nativePointer);
	Interceptor.attach(nativePointer, {
		onEnter: function(args){	
			send(args[2]);	//add参数1
			send(args[3]);
			send(args[4]);		
		},
		onLeave: function(retval){
			send(retval);	//返回值
			send("-----------");
		}
	});


"""

nativehook = """
Interceptor.attach(Module.findExportByName("libhello.so" , "Java_com_xiaojianbang_app_NativeHelper_add"), {
    onEnter: function(args) {
        send("open called!");
    },
    onLeave:function(retval){
     send("open Leave!");
    }
});
"""


script = session.create_script(src)

def on_message(message, data):
    if message['type'] == 'error':
        print("[!] " + message['stack'])
    elif message['type'] == 'send':
        print("[i] " + message['payload'])
    else:
        print(message)
		
script.on('message', on_message)
script.load()
sys.stdin.read()
