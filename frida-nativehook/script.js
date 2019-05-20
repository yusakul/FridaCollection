console.log("Script loaded successfully ");
Java.perform(function(){
	
	var nativePointer = Module.findExportByName("libhello.so", "Java_com_xiaojianbang_app_NativeHelper_add");
	send("native: " + nativePointer);
	Interceptor.attach(nativePointer, {
		onEnter: function(args){
			send(args[0]);
			send(args[1]);
			send(args[2].toInt32());
			send(args[3].toInt32());
			send(args[4].toInt32());
		},
		onLeave: function(retval){
			send(retval.toInt32());
		}
	});
	
});