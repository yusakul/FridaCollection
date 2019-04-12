# hook 浏览器（com.android.chrome）进程
import frida
import sys

rdev = frida.get_remote_device()
session = rdev.attach("com.android.chrome") #如果存在两个一样的进程名可以采用rdev.attach(pid)的方式


scr = """
Interceptor.attach(Module.findExportByName("libdvm.so" , "dvmResolveClass"), {
    onEnter: function(args) {
        send("open called!");
    },
    onLeave:function(retval){
    
    }
});
"""
def on_message(message ,data):
    print(message['payload'])


script = session.create_script(scr)
script.on("message" , on_message)
script.load()
sys.stdin.read()