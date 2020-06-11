import re

formulate = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
geui = formulate.replace(' ','')
def rep(con,res,txt):
    # print(re.sub(con,res,txt,count=1))
    return re.sub(con,res,txt,count=1)

def mulit(geui):
    '''首先把乘除计算出结果，替换'''
    con = r'(\d+\.?\d*)(\*|/)(\d+\.?\d*)'
    res = re.search(con,geui)
    if res != None:  # 如果还有乘除，则继续递归
        print(res.group(),' result: ',eval(res.group()))
        res = str(eval(res.group()))
        return mulit(rep(con,res,geui))
    else:  # 否则返回最终的字符串
        return geui

jxjm = mulit(geui)
print(jxjm)

def brac(geui):
    con = r'\((-?\d+(\.?\d*)?)*\)'
    res = re.findall(con, geui)
    print(res)
    if res != None:
        print('brac',res.group(), ' result: ', eval(res.group()))
        res = str(eval(res.group()))
        mulit(rep(con, res, geui))

brac(jxjm)








