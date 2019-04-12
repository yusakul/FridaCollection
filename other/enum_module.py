# 枚举某个进程加载的所有模块以及模块中的导出函数
import frida
#rdev = frida.get_remote_device()
#session = rdev.attach("com.android.browser")  #如果存在两个一样的进程名可以采用rdev.attach(pid)的方式

session = frida.get_remote_device().attach("com.android.browser")

print (session)
Module = session.enumerateModules()
print (Module)
for module in Module:
    print (module)
    export_funcs = module.enumerate_exports()
    print ("\tfunc_name\tRVA")
    for export_func in export_funcs:
        print ("\t%s\t%s"%(export_func.name,hex(export_func.relative_address)))