import inspect

frame = None


def foo():
    bar()


def bar():
    global frame
    frame = inspect.currentframe()


"""
    python中函数的工作原理
        python.exe(这个可执行文件是用c语言写的) PyEval_EvalFramEx(C函数)去执行foo函数
        首先会创建一个栈帧(实际是上下文 Load_Global(bar))
        当foo调用子函数bar 又会创建一个栈帧 
        这些栈帧都是分配在堆内存中 这就决定了栈帧可以独立于调用者存在
        运行完成还可以找到栈帧
        又因为python中一切皆对象 栈帧对象 字节码对象
"""
import dis

print(dis.dis(foo))
foo()
print(frame.f_code.co_name)  # bar
caller_frame = frame.f_back
print(caller_frame.f_code.co_name)  # foo


def gen_func():
    yield 1
    name = "bobby"
    yield 2
    age = 30
    return "Imooc"  # 生成器函数也是可以return值的




"""
    运行完成还可以找到栈帧
        决定有变量保存最后一次运行的位置 
    生成器函数每次遇到yield都会停止 
    在底层就是栈帧对象就会保存最近执行代码的字节码的位置 
        通俗来说 就是保存这次执行完之后的位置 下次还从这走 再执行一次
    
    可以独立于调用者存在 只要拿到栈帧对象可以重新调用栈帧对象 继续生成栈帧对象
    也就是说 拿到生成器对象 就可以继续控制它向前走 拿到他 恢复他
    核心就是说 整个函数的控制和暂停 f_lasti和f_locals
        
"""
