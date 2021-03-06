'''
python是一门动态解释性的强类型定义语言


编译器是把源程序的每一条语句都编译成机器语言,并保存成二进制文件,这样运行时计算机可以直接以机器语言来运行此程序,
速度很快; 

而解释器则是只在执行程序时,才一条一条的解释成机器语言给计算机来执行,所以运行速度是不如编译后的程序运行的快的.


动态语言和静态语言
通常我们所说的动态语言、静态语言是指动态类型语言和静态类型语言。
（1）动态类型语言：动态类型语言是指在运行期间才去做数据类型检查的语言，
    也就是说，在用动态类型的语言编程时，永远也不用给任何变量指定数据类型，
    该语言会在你第一次赋值给变量时，在内部将数据类型记录下来。Python和Ruby就是一种典型的动态类型语言，
    其他的各种脚本语言如VBScript也多少属于动态类型语言。
（2）静态类型语言：静态类型语言与动态类型语言刚好相反，它的数据类型是在编译其间检查的，
    也就是说在写程序时要声明所有变量的数据类型，C/C++是静态类型语言的典型代表，其他的静态类型语言还有C#、JAVA等。


强类型定义语言和弱类型定义语言
（1）强类型定义语言：强制数据类型定义的语言。也就是说，一旦一个变量被指定了某个数据类型，如果不经过强制转换，
    那么它就永远是这个数据类型了。举个例子：如果你定义了一个整型变量a,那么程序根本不可能将a当作字符串类型处理。
    强类型定义语言是类型安全的语言。
（2）弱类型定义语言：数据类型可以被忽略的语言。它与强类型定义语言相反, 一个变量可以赋不同数据类型的值。

    强类型定义语言在速度上可能略逊色于弱类型定义语言，但是强类型定义语言带来的严谨性能够有效的避免许多错误。
    另外，“这门语言是不是动态语言”与“这门语言是否类型安全”之间是完全没有联系的！
    例如：Python是动态语言，是强类型定义语言（类型安全的语言）; VBScript是动态语言，是弱类型定义语言（类型不安全的语言）
    JAVA是静态语言，是强类型定义语言（类型安全的语言）。

'''