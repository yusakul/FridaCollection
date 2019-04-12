import time
import frida

def my_message_handler(message, payload):
    print message
    print payload
    if message["type"] == "send":
        print message["payload"]
    
		data = “被发送的数据”
		
        script.post({"my_data": data})  # send JSON object
        print "Modified data sent"

device = frida.get_usb_device()
pid = device.spawn(["com.roysue.demo04"])
device.resume(pid)
time.sleep(1)
session = device.attach(pid)
with open("s4.js") as f:
    script = session.create_script(f.read())
script.on("message", my_message_handler)  # register the message handler
script.load()
raw_input()
