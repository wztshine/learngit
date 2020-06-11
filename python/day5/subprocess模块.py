import subprocess


# 默认接受['程序名','参数']的列表；shell=True表示直接调用系统的shell来执行字符串参数
# print(subprocess.run('dir',shell=True))  # 执行指定的命令，等待命令执行完成后返回一个包含执行结果的CompletedProcess类的实例。
# print(subprocess.call('dir',shell=True)) # 执行指定的命令，返回命令执行状态，其功能类似于os.system(cmd)
# print(subprocess.check_call('dir',shell=True)) #执行指定的命令，如果执行成功则返回状态码，否则抛出异常。其功能等价于subprocess.run(..., check=True)。
# print(subprocess.check_output('dir',shell=True)) #执行指定的命令，如果执行状态码为0则返回命令执行结果(二进制字节形式的)，否则抛出异常。
# print(subprocess.getoutput('dir')) # 接收字符串格式的命令，执行命令并返回执行结果，其功能类似于os.popen(cmd).read()和commands.getoutput(cmd)。
# print(subprocess.getstatusoutput('dir')) #执行字符串命令，返回一个元组(命令执行状态, 命令执行结果输出)

'''
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, 
        shell=False, timeout=None, check=False, universal_newlines=False)
subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)
subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)
subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False, timeout=None)
subprocess.getstatusoutput(cmd)
subprocess.getoutput(cmd)

参数说明：
args：  要执行的shell命令，默认应该是一个字符串序列，如['df', '-Th']或('df', '-Th')，
        也可以是一个字符串，如'df -Th'，但是此时需要把shell参数的值置为True。
shell： 如果shell为True，那么指定的命令将通过shell执行。如果我们需要访问某些shell的特性，
        如管道、文件名通配符、环境变量扩展功能，这将是非常有用的。
        当然，python本身也提供了许多类似shell的特性的实现，如glob、fnmatch、os.walk()、
        os.path.expandvars()、os.expanduser()和shutil等。
check： 如果check参数的值是True，且执行命令的进程以非0状态码退出，
        则会抛出一个CalledProcessError的异常，且该异常对象会包含 参数、退出状态码、以及stdout和stderr(如果它们有被捕获的话)。
stdout, stderr：input： 该参数是传递给Popen.communicate()，通常该参数的值必须是一个字节序列，
        如果universal_newlines=True，则其值应该是一个字符串。
    run()函数默认不会捕获命令执行结果的正常输出和错误输出，如果我们向获取这些内容需要传递subprocess.PIPE，
        然后可以通过返回的CompletedProcess类实例的stdout和stderr属性或捕获相应的内容；
    call()和check_call()函数返回的是命令执行的状态码，而不是CompletedProcess类实例，
        所以对于它们而言，stdout和stderr不适合赋值为subprocess.PIPE；
    check_output()函数默认就会返回命令执行结果，所以不用设置stdout的值，
        如果我们希望在结果中捕获错误信息，可以执行stderr=subprocess.STDOUT。
universal_newlines： 该参数影响的是输入与输出的数据格式，比如它的值默认为False，此时stdout和stderr的输出是字节序列；
        当该参数的值设置为True时，stdout和stderr的输出是字符串。
'''




# subprocess.Popen()
'''
class subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, 
    preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=False,
    startup_info=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=())
    
参数：
args： 要执行的shell命令，可以是字符串，也可以是命令各个参数组成的序列。
        当该参数的值是一个字符串时，该命令的解释过程是与平台相关的，因此通常建议将args参数作为一个序列传递。
bufsize： 指定缓存策略，0表示不缓冲，1表示行缓冲，其他大于1的数字表示缓冲区大小，负数 表示使用系统默认缓冲策略。
stdin, stdout, stderr： 分别表示程序标准输入、输出、错误句柄。
preexec_fn： 用于指定一个将在子进程运行之前被调用的可执行对象，只在Unix平台下有效。
close_fds： 如果该参数的值为True，则除了0,1和2之外的所有文件描述符都将会在子进程执行之前被关闭。
shell： 该参数用于标识是否使用shell作为要执行的程序，如果shell值为True，
        则建议将args参数作为一个字符串传递而不要作为一个序列传递。
cwd： 如果该参数值不是None，则该函数将会在执行这个子进程之前改变当前工作目录。
env： 用于指定子进程的环境变量，如果env=None，那么子进程的环境变量将从父进程中继承。
        如果env!=None，它的值必须是一个映射对象。
universal_newlines： 如果该参数值为True，则该文件对象的stdin，stdout和stderr将会作为文本流被打开，
        否则他们将会被作为二进制流被打开。
startupinfo和creationflags： 这两个参数只在Windows下有效，它们将被传递给底层的CreateProcess()函数，
        用于设置子进程的一些属性，如主窗口的外观，进程优先级等。
       
方法： 
Popen.poll()	用于检查子进程（命令）是否已经执行结束，没结束返回None，结束后返回状态码。
Popen.wait(timeout=None) 等待子进程结束并返回状态码；如果在timeout指定的秒数之后进程还没有结束，将抛出TimeoutExpired异常。
Popen.communicate(input=None, timeout=None)	该方法可用来与进程进行交互，比如发送数据到stdin，从stdout和stderr读取数据，直到到达文件末尾。
    该方法中的可选参数 input 应该是将被发送给子进程的数据，或者如没有数据发送给子进程，该参数应该是None。input参数的数据类型必须是字节串，如果universal_newlines参数值为True，则input参数的数据类型必须是字符串。
    该方法返回一个元组(stdout_data, stderr_data)，这些数据将会是字节穿或字符串（如果universal_newlines的值为True）。
    如果在timeout指定的秒数后该进程还没有结束，将会抛出一个TimeoutExpired异常。捕获这个异常，然后重新尝试通信不会丢失任何输出的数据。但是超时之后子进程并没有被杀死，为了合理的清除相应的内容，一个好的应用应该手动杀死这个子进程来结束通信。
    需要注意的是，这里读取的数据是缓冲在内存中的，所以，如果数据大小非常大或者是无限的，就不应该使用这个方法。
    communicate()是Popen对象的一个方法，该方法会阻塞父进程，直到子进程完成
Popen.send_signal(signal)	发送指定的信号给这个子进程。
Popen.terminate()	停止该子进程。
Popen.kill()	杀死该子进程。

eg.
child = subprocess.Popen('ping -c4 blog.linuxeye.com',shell=True)
child.wait()
child.kill()
'''


p = subprocess.Popen('dir', stdout=subprocess.PIPE, shell=True,universal_newlines=True)
print(p.stdout.read())

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
obj.stdin.write('print(1) \n')
out,err = obj.communicate()
print(out,err)

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
out,err = obj.communicate(input='print(1) \n')
print(out)
print(err)


# linux的命令，构成管道：前一个命令的结果作为后一个命令的参数
p1 = subprocess.Popen(['df', '-Th'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'data'], stdin=p1.stdout, stdout=subprocess.PIPE)
out,err = p2.communicate()
print(out)






