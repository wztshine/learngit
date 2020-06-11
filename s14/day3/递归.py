'''
递归特性:

1. 必须有一个明确的结束条件
2. 每次进入更深一层递归时，问题规模相比上次递归都应有所减少
3.  递归效率不高，递归层次过多会导致栈溢出（每进行一次函数调用，计算机为了保存程序当前的状态，会将当前状态入栈，
以便函数返回时，能恢复函数调用之前的状态，栈的大小是有限的，所以当调用过多时，可能会导致栈溢出。）

'''

data = [1, 3, 6, 7, 9, 12, 14, 16, 17, 18, 20, 21, 22, 23, 30, 32, 33, 35]


def binary_search(dataset, find_num):
    print(dataset)
    if len(dataset) > 1:
        mid = int(len(dataset) / 2)
        if dataset[mid] == find_num:  # find it
            print("找到数字", dataset[mid])
        elif dataset[mid] > find_num:  # 找的数在mid左面
            print("\033[31;1m找的数在mid[%s]左面\033[0m" % dataset[mid])
            return binary_search(dataset[0:mid], find_num)
        else:  # 找的数在mid右面
            print("\033[32;1m找的数在mid[%s]右面\033[0m" % dataset[mid])
            return binary_search(dataset[mid + 1:], find_num)
    else:
        if dataset[0] == find_num:  # find it
            print("找到数字啦", dataset[0])
        else:
            print("没的分了,要找的数字[%s]不在列表里" % find_num)


binary_search(data, 17)