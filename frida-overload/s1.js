console.log("Script loaded successfully ");
Java.perform(function x() {
    console.log("Inside java perform function");
    var my_class = Java.use("com.roysue.demo02.MainActivity");
    my_class.fun.overload("int", "int").implementation = function (x, y) { //hook第1个重载函数
        console.log("original call: fun(" + x + ", " + y + ")");
        var ret_value = this.fun(2, 5);
        return ret_value;
    };
    var string_class = Java.use("java.lang.String");
    my_class.fun.overload("java.lang.String").implementation = function (x) { //hook第2个重载函数
        console.log("*************************************")
        var my_string = string_class.$new("My TeSt String#####");
        console.log("Original arg: " + x);
        var ret = this.fun(my_string);
        console.log("Return value: " + ret);
        console.log("*************************************")
        return ret;
    };
    Java.choose("com.roysue.demo02.MainActivity", {//hook 没有被调用的函数
        onMatch: function (instance) {
            console.log("Found instance: " + instance);
            console.log("Result of secret func: " + instance.secret());
        },
        onComplete: function () { }
    });
});
