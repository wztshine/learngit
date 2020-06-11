import shutil

f1 = open('a.txt','r')
f2 = open('b.txt','w')

# shutil.copyfileobj(fsrc, fdst[, length])  把fsrc复制到一个新文件fdst里，length代表每次读取的大小，防止内存溢出
shutil.copyfileobj(f1,f2,1024)

# copy(src, dst, *, follow_symlinks=True)复制一个文件的路径，到另一个路径(可以为路径或者文件名)，follow_symlinks在linux生效，具体搜索硬连接和软连接
shutil.copy('a.txt','../b.txt')

# chown(path, user=None, group=None) 改变给定path的所有者和组权限，似乎在linux生效
# shutil.chown()

# copy2(src, dst, *, follow_symlinks=True) 复制数据和数据的状态信息
shutil.copy2('a.txt','../b.txt')

# copymode(src, dst, *, follow_symlinks=True) 仅拷贝权限。内容、组、用户均不变
shutil.copymode()

# copystat(src, dst, *, follow_symlinks=True) 拷贝状态的信息，包括：mode bits, atime, mtime, flags
shutil.copystat()

# copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2,
#              ignore_dangling_symlinks=False) 复制一个文件夹及其内容到另一个文件夹下,ignore过滤条件，可以多个
# 注意，必须要指定一个文件夹，即把a文件夹的内容，复制到父目录的b里面（b一定不能事先存在）
shutil.copytree('a','../b',ignore=shutil.ignore_patterns('*.bat','*.py'))

# 获取一个路径的磁盘占用，返回一个三元组(total,used,free)
print(shutil.disk_usage('D:\\'))

# 显示支持的打包格式/解压包的格式
print(shutil.get_archive_formats())
print(shutil.get_unpack_formats())

# 打包文件 (包名，格式，要打包的路径)
shutil.make_archive('a_zip','zip','a')

# 移动文件或文件夹到另一路径: (源文件路径，目标路径)
shutil.move('a','../')

# 注册一个新的打包方式？
shutil.register_archive_format()
shutil.register_unpack_format()

# 删除文件夹及其内容,选择是否忽略错误(默认false，没有要删除的文件夹会报错)
shutil.rmtree('a',ignore_errors=True)
# (文件名，[,解压路径，解压方式]) unpack_archive(filename, extract_dir=None, format=None)
shutil.unpack_archive('a.zip','a')

# shutil.unregister_archive_format()
# shutil.unregister_unpack_format()