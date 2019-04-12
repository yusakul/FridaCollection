console.log("Script loaded successfully ");
Java.perform(function x() { 
	//此文件是被pyhthon文件加载,这里执行java层函数
    console.log("Inside java perform function");
    //获取要hook的类
    var my_class = Java.use("com.roysue.demo02.MainActivity");
    console.log("Java.Use.Successfully!");
    //用我们的自定义函数替换原始函数
    my_class.fun.implementation = function(x,y){
    //打印原始参数
	console.log( "original call: fun("+ x + ", " + y + ")");
    //调用原函数，并传参2,5
	var ret_value = this.fun(2, 5);
	return ret_value;
    }
});
