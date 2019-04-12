import time
import frida

device = frida.get_usb_device()
//要hook的进程包名
pid = device.spawn(["com.roysue.demo02"])	
device.resume(pid)
time.sleep(1)  # 没有它，Java.perform将失败
session = device.attach(pid)
with open("s1.js") as f:
    script = session.create_script(f.read())
script.load()

# python script结束
raw_input()
