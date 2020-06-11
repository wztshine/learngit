# # 第一种，定位到s14文件夹,project文件夹
# import os
# import sys
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# print(BASE_DIR)
# sys.path.append(BASE_DIR)
# for i in sys.path:
#     print(i)
#
# from day5.test.package import package_test
#
# print(package_test.name)


# 第二种，定位到两者的父目录:test
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
sys.path.append(BASE_DIR)
for i in sys.path:
    print(i)

from package import package_test
print(package_test.name)