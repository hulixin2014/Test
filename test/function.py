# coding=utf-8
from operator import add


def my_max(seq):
    return reduce(max, seq)


# 返回最小值
def my_min(seq):
    return reduce(min, seq)


# 变长参数
def printf(a, *tuples, **dicts):
    print a
    for each in tuples:
        print each
    for key in dicts.keys():
        print '%s:%s' % (key, dicts[key])


# map()函数
def zipfunc(list1, list2):
    def together(x, y):
        return (x, y)

    return map(together, list1, list2)


# 判断是否为闰年
def isLeapYear(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def getleaplist(yearlist):
    return filter(isLeapYear, yearlist)


# 累加
def average(seq):
    return reduce(add, seq) / float(len(seq))


# 乘法
def mult(x, y):
    return x * y


# 阶乘
def n_mult(n):
    if n >= 2:
        a = range(1, n + 1)
        return reduce(mult, a)
    elif n == 0:
        return 1
    else:
        print '负数不存在阶乘'


def n_mult1(n):
    if n >= 2:
        a = range(1, n + 1)
        return reduce(lambda x, y: x * y, a)
    elif n == 0:
        return 1
    else:
        print '负数不存在阶乘'

def print_hello(str):
    print("hello "+str)
    

a = 1


def _show():
    print a


# 网络编程模块服务端TCP
import socket  # socket模块
# from time import *
# HOST='172.31.102.75'
# PORT=50007
# s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #定义socket类型，网络通信，TCP
# s.bind((HOST,PORT))   #套接字绑定的IP与端口
# s.listen(5)         #开始TCP监听
# while 1:
#        conn,addr=s.accept()   #接受TCP连接，并返回新的套接字与IP地址
#        print'Connected by',addr    #输出客户端的IP地址
#        while 1:
#             data=conn.recv(1024)    #把接收的数据实例化
#             if not data:
#                 conn.close()  # 关闭连接
#                 break
#             else:
#                 message="[%s:] %s"%(ctime(),data)
#                 conn.sendall(message)   #否则就把结果发给对端（即客户端）
# s.close()

# 网络编程模块客户端TCP
# HOST='172.31.102.75'
# PORT=50007
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
# s.connect((HOST,PORT))       #要连接的IP与端口
# while 1:
#        cmd=raw_input("Please input cmd:")       #与人交互，输入命令
#        s.sendall(cmd)      #把命令发送给对端
#        if not cmd:
#            s.close()  # 关闭连接
#            break
#        else:
#            data=s.recv(1024)     #把接收的数据定义为变量
#            print data         #输出变量

# 网络编程模块服务端UDP
# HOST='172.31.102.75'
# PORT=50007
# s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   #定义socket类型，网络通信，TCP
# s.bind((HOST,PORT))   #套接字绑定的IP与端口
#
# while 1:
#        print "waiting for message..."
#        data,addr=s.recvfrom(1024)
#        s.sendto("[%s] %s"%(ctime(),data),addr)
#        print "...recieved from and return to:",addr
# s.close()

# 网络编程模块客户端UDP
# HOST='172.31.102.75'
# PORT=50007
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      #定义socket类型，网络通信，TCP
#
# while 1:
#     cmd=raw_input("Please input cmd:")       #与人交互，输入命令
#     if not cmd:
#         break
#     s.sendto(cmd,(HOST,PORT))  # 把命令发送给对端
#     data,addr=s.recvfrom(1024)
#     if not data:
#         break
#     print data,addr
# s.close()
